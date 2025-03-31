from browser import document, window
import random

# Set up the canvas
canvas = document["gameCanvas"]
context = canvas.getContext("2d")

# Game variables
x, y = 100, 100  # Initial position of the circle
radius = 20
speed = 5
game_over = False
score = 0

# Obstacle variables
obstacle_width = 50
obstacle_height = 50
obstacles = []

# Functions to draw things
def draw_background():
    context.fillStyle = "lightblue"
    context.fillRect(0, 0, canvas.width, canvas.height)

def draw_circle():
    context.beginPath()
    context.arc(x, y, radius, 0, 2 * window.Math.PI)
    context.fillStyle = "blue"
    context.fill()
    context.closePath()

def draw_obstacles():
    global obstacles
    context.fillStyle = "red"
    for obstacle in obstacles:
        context.fillRect(obstacle["x"], obstacle["y"], obstacle_width, obstacle_height)

def draw_score():
    context.font = "20px Arial"
    context.fillStyle = "black"
    context.fillText(f"Score: {score}", 10, 30)

def move_circle(event):
    global x, y, score, game_over
    
    if game_over:
        return

    if event.keyCode == 37:  # Left arrow
        x -= speed
    elif event.keyCode == 38:  # Up arrow
        y -= speed
    elif event.keyCode == 39:  # Right arrow
        x += speed
    elif event.keyCode == 40:  # Down arrow
        y += speed

    # Check for collision with boundaries
    if x - radius < 0:
        x = radius
    if x + radius > canvas.width:
        x = canvas.width - radius
    if y - radius < 0:
        y = radius
    if y + radius > canvas.height:
        y = canvas.height - radius

    check_collision()

def check_collision():
    global score, game_over
    # Check for collision with obstacles
    for obstacle in obstacles:
        if (x + radius > obstacle["x"] and x - radius < obstacle["x"] + obstacle_width and
            y + radius > obstacle["y"] and y - radius < obstacle["y"] + obstacle_height):
            game_over = True
            show_game_over()

    # Increase score if no collision
    if not game_over:
        score += 1

def add_obstacles():
    # Add new obstacles at random positions
    if random.random() < 0.02:  # 2% chance of adding a new obstacle
        new_obstacle = {
            "x": random.randint(0, canvas.width - obstacle_width),
            "y": random.randint(0, canvas.height - obstacle_height)
        }
        obstacles.append(new_obstacle)

def show_game_over():
    context.clearRect(0, 0, canvas.width, canvas.height)
    context.fillStyle = "black"
    context.font = "40px Arial"
    context.fillText("Game Over!", canvas.width // 3, canvas.height // 3)
    context.font = "20px Arial"
    context.fillText(f"Final Score: {score}", canvas.width // 3, canvas.height // 2)

def reset_game():
    global x, y, game_over, score, obstacles
    x, y = 100, 100
    game_over = False
    score = 0
    obstacles = []
    draw_game()

def draw_game():
    if game_over:
        return

    draw_background()
    draw_circle()
    draw_obstacles()
    draw_score()

# Game loop (update every 16ms)
def game_loop():
    if not game_over:
        add_obstacles()
        draw_game()
    window.setTimeout(game_loop, 16)

# Event listener for keypresses
window.addEventListener("keydown", move_circle)

# Start the game
game_loop()
