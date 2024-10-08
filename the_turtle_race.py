import random  # Import the random module to generate random numbers
from turtle import Turtle, Screen  # Import Turtle and Screen classes from the turtle module
import race_art

# Create a screen for the turtle graphics
screen = Screen()  # Initialize the screen
screen.bgcolor('black')  # Set the background color of the screen to black
screen.setup(width=1500, height=650)  # Set the size of the screen
screen.title("The Turtle Race")  # Set the title of the screen

print(race_art.logo)
print(race_art.credit_of_project)

# Create five turtle objects for the race
a = Turtle()  # Create turtle A
b = Turtle()  # Create turtle B
c = Turtle()  # Create turtle C
d = Turtle()  # Create turtle D
e = Turtle()  # Create turtle E

# Hide the turtles initially
a.hideturtle()  # Hide turtle A
b.hideturtle()  # Hide turtle B
c.hideturtle()  # Hide turtle C
d.hideturtle()  # Hide turtle D
e.hideturtle()  # Hide turtle E

# Draw the finish line using turtle A
a.teleport(700, 300)  # Move turtle A to the position (700, 300)
a.width(5)  # Set the width of the line to 5
a.color('white')  # Set the color of the line to white
a.right(90)  # Turn turtle A to face downward
a.forward(600)  # Draw the vertical line downwards for 600 units
a.width(0)  # Reset the width of the turtle to 0 (no line)
a.left(90)  # Turn turtle A back to the right

# Set up turtle A (Red)
a.shape('turtle')  # Set the shape of turtle A to a turtle
a.shapesize(2.5, 2.5)  # Increase the size of turtle A
a.teleport(-700, 200)  # Move turtle A to the starting position (-700, 200)
a.color('red')  # Set the color of turtle A to red

# Set up turtle B (Green)
b.shape('turtle')  # Set the shape of turtle B to a turtle
b.shapesize(2.5, 2.5)  # Increase the size of turtle B
b.teleport(-700, 100)  # Move turtle B to the starting position (-700, 100)
b.color('green')  # Set the color of turtle B to green

# Set up turtle C (Blue)
c.shape('turtle')  # Set the shape of turtle C to a turtle
c.shapesize(2.5, 2.5)  # Increase the size of turtle C
c.teleport(-700, 0)  # Move turtle C to the starting position (-700, 0)
c.color('blue')  # Set the color of turtle C to blue

# Set up turtle D (Yellow)
d.shape('turtle')  # Set the shape of turtle D to a turtle
d.shapesize(2.5, 2.5)  # Increase the size of turtle D
d.teleport(-700, -100)  # Move turtle D to the starting position (-700, -100)
d.color('yellow')  # Set the color of turtle D to yellow

# Set up turtle E (Violet)
e.shape('turtle')  # Set the shape of turtle E to a turtle
e.shapesize(2.5, 2.5)  # Increase the size of turtle E
e.teleport(-700, -200)  # Move turtle E to the starting position (-700, -200)
e.color('violet')  # Set the color of turtle E to violet

# Show the turtles on the screen
a.showturtle()  # Make turtle A visible
b.showturtle()  # Make turtle B visible
c.showturtle()  # Make turtle C visible
d.showturtle()  # Make turtle D visible
e.showturtle()  # Make turtle E visible

# Ask the user to place a bet on a turtle
choice = screen.textinput(title="The Turtle Race", prompt="Place Your bet: "
                                                          "( red / yellow / green / blue / violet ): ").lower()

# Function to handle the race
def race():
    while True:  # Infinite loop to keep the race going
        a.forward(random.randint(1, 10))  # Move turtle A forward by a random distance between 1 and 10
        if a.xcor() >= 700:  # Check if turtle A has reached or passed the finish line
            return "red"  # Return the winning turtle's color

        b.forward(random.randint(1, 10))  # Move turtle B forward by a random distance
        if b.xcor() >= 700:  # Check if turtle B has reached the finish line
            return "green"  # Return the winning turtle's color

        c.forward(random.randint(1, 10))  # Move turtle C forward by a random distance
        if c.xcor() >= 700:  # Check if turtle C has reached the finish line
            return "blue"  # Return the winning turtle's color

        d.forward(random.randint(1, 10))  # Move turtle D forward by a random distance
        if d.xcor() >= 700:  # Check if turtle D has reached the finish line
            return "yellow"  # Return the winning turtle's color

        e.forward(random.randint(1, 10))  # Move turtle E forward by a random distance
        if e.xcor() >= 700:  # Check if turtle E has reached the finish line
            return "violet"  # Return the winning turtle's color

# Start the race and get the result
result = race()  # Call the race function and store the result

# Check if the player's bet matches the winning turtle
if choice == result:  # If the player's choice matches the winning turtle
    print("\nYou won...!!!")  # Inform the player they won
else:
    print("\nYou lose...!!!")  # Inform the player they lost

# Wait for the user to click before closing the screen
screen.exitonclick()  # Close the window when the user clicks on it
