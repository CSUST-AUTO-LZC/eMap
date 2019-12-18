import turtle


def draw_branch(branch_length):
    if branch_length > 5:
        if branch_length < 10:
            turtle.pencolor('red')
        else:
            turtle.pencolor('green')

        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length-10)
        turtle.left(40)
        draw_branch(branch_length-10)
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pencolor('green')
    draw_branch(80)
    turtle.exitonclick()


if __name__ =="__main__":
    main()
