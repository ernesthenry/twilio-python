import turtle


# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor('red')

#     ernest = turtle.Turtle()
#     ernest.shape('turtle')
#     ernest.speed(2)

#     ernest.forward(100)
#     ernest.right(90)
#     ernest.forward(100)
#     ernest.right(90)
#     ernest.forward(100)
#     ernest.right(90)
#     ernest.forward(100)
#     ernest.right(90)

#     henry = turtle.Turtle()
#     henry.shape('arrow')
#     henry.color('blue')
#     henry.circle(100)

#     Kato = turtle.Turtle()
#     Kato.shape('arrow')
#     Kato.color('green')
#     Kato.triangle(100)

#     window.exitonclick()


# draw_square()


# making changes to make code reusable

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    # create the turtle ernest - draws a square

    for i in range(1, 37):
        ernest = turtle.Turtle()
        ernest.shape('turtle')
        ernest.speed(2)

        draw_square(ernest)
        ernest.right(10)
        print(i)

    # create a turtle henry - draws a circle

    henry = turtle.Turtle()
    henry.shape('arrow')
    henry.color('blue')
    henry.circle(100)
    draw_square(henry)

    window.exitonclick()
