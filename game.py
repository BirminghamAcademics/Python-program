from browser import document, window

# Set up the canvas
canvas = document["gameCanvas"]
context = canvas.getContext("2d")

# Game variables
x, y = 100, 100  # Initial position of the circle
radius = 20
speed = 5

def draw_circle():
    # Clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height)
    # Draw a new circle
    context.beginPath()
    context.arc(x, y, radius, 0, 2 * window.Math.PI)
    context.fillStyle = "blue"
    context.fill()
    context.closePath()

def move_circle(event):
    global x, y

    if event.keyCode == 37:  # Left arrow
        x -= speed
    elif event.keyCode == 38:  # Up arrow
        y -= speed
    elif event.keyCode == 39:  # Right arrow
        x += speed
    elif event.keyCode == 40:  # Down arrow
        y += speed

    draw_circle()

# Attach event listener for arrow keys
window.addEventListener("keydown", move_circle)

# Initial draw
draw_circle()
