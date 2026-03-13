🚀 Enemy Dodger (Pygame)

Enemy Dodger is a simple arcade-style game built with Python and Pygame.
The player controls a spaceship and must avoid incoming enemy ships while collecting power-ups to temporarily increase movement speed.

🎮 Gameplay

Control a yellow spaceship at the bottom of the screen.

Enemy ships fall from the top of the screen.

Avoid colliding with enemies.

Collect power-ups to temporarily increase your spaceship's speed.

Survive as long as possible to increase your score.

If you collide with an enemy ship, the game ends and displays DEFEAT before restarting.

🕹 Controls
Key	Action
⬅ Left Arrow	Move left
➡ Right Arrow	Move right
❌ Close Window	Quit game
⚡ Power-Ups

Power-ups increase your spaceship speed temporarily.

Normal Speed: 5

Power-Up Speed: 10

Duration: 3 seconds

A timer appears on the screen while the power-up is active.

📦 Requirements

Make sure you have the following installed:

Python 3.x

Pygame

Install pygame with:

pip install pygame
📁 Project Structure
Enemy-Dodger/
│
├── main.py
├── README.md
└── Assets/
    ├── space.png
    ├── spaceship_yellow.png
    ├── spaceship_red.png
    └── power_block.gif
▶️ How to Run

Clone the repository:

git clone https://github.com/yourusername/enemy-dodger.git

Navigate to the folder:

cd enemy-dodger

Run the game:

python main.py
🧠 Game Features

Countdown before the game starts

Falling enemy ships with random speeds

Collectable power-ups

Power-up timer display

Collision detection

Score tracking

Automatic game reset after defeat

🛠 Built With

Python

Pygame

📈 Future Improvements

Possible features to add:

Sound effects and music

Different enemy types

Increasing difficulty over time

High score system

Start menu and restart button

Animations

👨‍💻 Author

Created by [Your Name]
