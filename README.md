🚀 Space Defender
Um jogo desenvolvido em Python com Pygame, onde o jogador controla uma nave espacial para destruir inimigos, acumular pontos e avançar por fases desafiadoras.

🎮 Sobre o Jogo
O Space Defender é um jogo de tiro 2D estilo arcade.
O objetivo é eliminar o maior número possível de inimigos, desviar de projéteis e sobreviver até o final das fases.

🧠 Desenvolvido do zero com Pygame
🎵 Efeitos sonoros e trilha sonora personalizados
🌌 Diferentes modos de jogo: 1 Jogador, Coop e Versus
🏆 Sistema de pontuação e ranking com banco de dados SQLite
💥 Explosões animadas e efeitos visuais
💾 Salvamento automático das pontuações

🕹️ Controles
Ação	Tecla
Mover para a esquerda	←
Mover para a direita	→
Atirar	Espaço
Pausar o jogo	Esc
Confirmar / Avançar	Enter

⚙️ Requisitos
Python 3.10+
Pygame 2.5+

Instale as dependências:
pip install pygame

▶️ Como jogar
Execute o arquivo principal:
python main.py
Escolha o modo de jogo (1P, Coop ou Versus)
Destrua os inimigos e avance pelas fases
Digite seu nome ao final para salvar sua pontuação

🧱 Estrutura do Projeto
Game/
│
├── assets/
│   ├── img/         # Imagens e sprites
│   ├── snd/         # Efeitos sonoros e músicas
│
├── code/
│   ├── Game.py      # Classe principal do jogo
│   ├── Menu.py      # Tela de menu
│   ├── Level.py     # Lógica de fases
│   ├── Score.py     # Sistema de pontuação
│   ├── EntityMediator.py  # Controle de entidades e colisões
│   ├── BDProxy.py   # Banco de dados SQLite
│   └── Const.py     # Constantes globais
│
└── main.py          # Ponto de entrada do jogo

🧠 Futuras Melhorias
 Adicionar power-ups e bônus
 Criar novos níveis com inimigos diferentes
 Implementar sistema de “vidas extras”
 Modo Boss final
 Suporte a joystick

👨‍💻 Autor
Emerson Santos
Desenvolvido como parte do curso de Tecnólogo em Análise e Desenvolvimento de Sistemas da UNINTER.

📚 Projeto didático — aprendizado de lógica, Pygame e estrutura de jogos 2D.

🪐 Licença
Este projeto é de uso educacional e livre para estudo.
© 2025 — Emerson Santos
