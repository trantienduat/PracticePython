# import turtle library
import turtle
import random


def main():
    turtle_obj = turtle.Turtle()
    colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black', 'pink', 'gray']

    # configure turtle object
    turtle_obj.screen.colormode(255)
    turtle_obj.color(get_random_color(), get_random_color())
    turtle_obj.shape('turtle')

    # set pen width
    turtle_obj.width(2)

    # Fill in shape with color
    turtle_obj.begin_fill()
    turtle_obj.circle(50)
    turtle_obj.end_fill()

    turtle_obj.penup()
    turtle_obj.forward(100)

    # first argument is the pen color, second arg is filled color
    turtle_obj.color(get_random_color(), get_random_color())
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    for i in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)
    turtle_obj.end_fill()

    # Create 5 random circles with different size
    for i in range(5):
        # penup for moving pen to random position
        turtle_obj.penup()
        turtle_obj.setpos(get_random_pos(), get_random_pos())

        # set random color and pendown to start drawing
        turtle_obj.color(get_random_color(), get_random_color())
        turtle_obj.pendown()

        turtle_obj.begin_fill()
        turtle_obj.circle(get_random_angle())
        turtle_obj.end_fill()


    # Fix automatically close the program in command line
    # input('Press any to close')


def get_random_color():
    R = int(random.randrange(0, 255))
    G = int(random.randrange(0, 255))
    B = int(random.randrange(0, 255))
    return R, G, B


def get_random_pos():
    random_num = random.randrange(-300, 300)
    return random_num


def get_random_angle():
    angle = int(random.randrange(0, 90))
    return angle


if __name__ == "__main__":
    main()
