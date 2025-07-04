import turtle
import time
import random

delay = 0.1


# Score
score = 0
high_score = 0

# Setting up the Screen
win = turtle.Screen()
win.title("Snake Valhalla")
win.bgcolor("#FFF5F5")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off the screen updates

# The Snake's Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)              # Set the initial position of the snake's head
head.direction = "stop"      # Set the initial direction of the snake's head


#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments =[]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 20, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main Game Loop
while True:
    win.update()
    
    # Check for Border Collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        # Clear the segments
        segments.clear()
        
        # Reset the Score
        score = 0
        
        # Reset the Delay
        delay = 0.1
        
        # Update the score display
        pen.clear()    
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    
    # Food Collision Check
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-290, 290, 20)
        y = random.randrange(-290, 290, 20)
        food.goto(x,y)
        
        # Add a Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the Delay
        delay -= 0.001
        
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        
        # Update the score display
        pen.clear()    
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
        
    # Move the Segments in reverse order, Start point ==> end
    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)
        
    # Move Segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()
    
    # Check for head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            # Clear the segments
            segments.clear()
    
    
            # Reset the Score
            score = 0
            
            # Reset the Delay
            delay = 0.1
            
            # Update the score display
            pen.clear()    
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    
    
    time.sleep(delay)
    
    
win.mainloop()
