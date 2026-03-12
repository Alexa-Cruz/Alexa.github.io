import turtle


# Building Block Functions


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_polygon(t, sides, length, color):
    t.color(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

def draw_square(t, size, color):
    draw_polygon(t, 4, size, color)


# Scene Drawing Function


def draw_scene():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Solar System (Static)")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Sun 
    jump_to(t, 0, -40)
    draw_circle(t, 40, "yellow")

    # Orbit Rings (not filled)
    t.color("white")
    for r in [80, 120, 160, 200]:
        jump_to(t, 0, -r)
        t.circle(r)

    # Mercury 
    jump_to(t, 80, 0)
    draw_circle(t, 6, "gray")

    #  Venus 
    jump_to(t, 120, 0)
    draw_circle(t, 8, "orange")

    #  Earth 
    jump_to(t, 160, 0)
    draw_circle(t, 9, "forestgreen")

    #  Mars 
    jump_to(t, 200, 0)
    draw_circle(t, 7, "red")

    #  Background Stars (using squares) 
    star_positions = [(-200, 150), (150, 180), (-150, -120), (180, -160), (0, 200)]
    for x, y in star_positions:
        jump_to(t, x, y)
        draw_square(t, 5, "lightyellow")

    turtle.done()


# Run the Scene

draw_scene()
