import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, WIN_WIDTH, C_YELLOW, C_RED
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Explosion import Explosion
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode, player_score, players=None):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Background
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        if players is None:
            players = {}

        # Player1
        if 'Player1' in players:
            player1 = players['Player1']
        else:
            player1 = EntityFactory.get_entity('Player1')
        if player_score['Player1_health'] is not None:
            player1.health = player_score['Player1_health']
        self.entity_list.append(player1)
        players['Player1'] = player1

        # Player2 (se modo 2P)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            if 'Player2' in players:
                player2 = players['Player2']
            else:
                player2 = EntityFactory.get_entity('Player2')
            if player_score['Player2_health'] is not None:
                player2.health = player_score['Player2_health']
            self.entity_list.append(player2)
            players['Player2'] = player2

        # Enemies
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Geração de evento
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100s, decrementar até chegar em 0 e encerrar o level

    def clear_level(self):
        """Limpa todas as entidades e desliga os timers do nível."""
        self.entity_list.clear()
        pygame.time.set_timer(EVENT_ENEMY, 0)
        pygame.time.set_timer(EVENT_TIMEOUT, 0)
        pygame.mixer.music.stop()  # opcional, se quiser parar a música sempre

    def run(self, player_score: list[int]):
        pygame.mixer.music.load('./assets/snd/level1.mp3')
        pygame.mixer.music.play(-1)  # tocar indefinidamente
        clock = pygame.time.Clock()  # Executar no tempo especifico

        while True:
            clock.tick(60)  # 60 FPS, taxa de atualização
            for ent in self.entity_list:
                if ent is None:
                    continue  # evita erro se houver None

                ent.move()  # primeiro atualiza posição

                # desenha a entidade
                if isinstance(ent, Explosion):
                    ent.draw(self.window)
                else:
                    self.window.blit(ent.surf, ent.rect)

                # dispara se for jogador ou inimigo
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shoot()  # chama apenas uma vez
                    if shot:
                        # ajusta a posição do tiro para sair da frente do inimigo/jogador
                        if isinstance(ent, Enemy):
                            shot.rect.left = ent.rect.left - 10
                            shot.rect.centery = ent.rect.centery
                        self.entity_list.append(shot)

                # Mostra status dos jogadores
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN,(10, 25)) # Texto superior
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))

                # Atualiza pontuação no dicionário
                if isinstance(ent, Player):
                   player_score[f'{ent.name}'] = ent.score
                   player_score[f'{ent.name}_health'] = ent.health
                # for ent in self.entity_list:
                #     if isinstance(ent, Player):
                #         if ent.name == 'Player1':
                #             player_score['Player1'] = ent.score
                #             player_score['Player1_health'] = ent.health
                #         if ent.name == 'Player2':
                #             player_score['Player2'] = ent.score
                #             player_score['Player2_health'] = ent.health

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score

                        self.clear_level()

                        return True  # Level concluído

                # Verifica se há players vivos
                if not any(isinstance(ent, Player) for ent in self.entity_list):
                    self.clear_level()
                    # Para a música do nível
                    pygame.mixer.music.stop()

                    self.clear_level()

                    # Retorna imediatamente para exibir Game Over depois
                    return False

            # printed text
            self.level_text(14, f'{self.name} + Timeout: {self.timeout / 1000 :.1f}s', C_WHITE,
                            (10, 5))  # Texto superior
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))  # Quantidade de imagens no background
            pygame.display.flip()

            # Colisão direta entre Player e Enemy
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    for enemy in self.entity_list:
                        if isinstance(enemy, Enemy) and ent.rect.colliderect(enemy.rect):
                            ent.health -= enemy.damage  # Player recebe dano
                            enemy.health = 0  # inimigo é destruído na colisão
                            EntityMediator.explosion_snd.play()  # som da colisão

            # Collisions e remoção de entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Remove explosões concluídas
            self.entity_list[:] = [e for e in self.entity_list if not (isinstance(e, Explosion) and e.finished)]

    def game_over_screen(self, player_score: dict):
        self.window.fill((0, 0, 0))  # fundo preto

        # Fonte grande para GAME OVER
        font_large = pygame.font.SysFont("Lucida Sans Typewriter", 48)
        text_surf = font_large.render("GAME OVER", True, C_RED)
        text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 50))
        self.window.blit(text_surf, text_rect)

        # Pontuação final (em branco)
        font_score = pygame.font.SysFont("Lucida Sans Typewriter", 25)
        score_text = f"Player1: {player_score.get('Player1', 0)}"

        # Adiciona Player2 apenas se ele estiver ativo (modo 2P)
        if 'Player2_health' in player_score and player_score['Player2_health'] is not None:
            score_text += f"  |  Player2: {player_score.get('Player2', 0)}"

        score_surf = font_score.render(score_text, True, C_WHITE)
        score_rect = score_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20))
        self.window.blit(score_surf, score_rect)

        # Mensagem inferior
        font_small = pygame.font.SysFont("Lucida Sans Typewriter", 20)
        continue_surf = font_small.render("Press any key to continue.", True, C_YELLOW)
        continue_rect = continue_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self.window.blit(continue_surf, continue_rect)

        pygame.display.flip()

        # Espera o jogador pressionar qualquer tecla
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
