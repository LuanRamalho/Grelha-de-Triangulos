import turtle

a = turtle.Screen()
turtle.speed(0)

def triângulo(posx, posy,lado):
    turtle.showturtle()
    # posicioan
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

    # desenha
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
    turtle.hideturtle()

def grelha(n,posx, posy,lado,cor):

    # inicialização
    turtle.pencolor(cor)
    for i in range(n):

        # desenha linha i
        for j in range(n):
            triângulo(turtle.xcor(),turtle.ycor(), lado)
            turtle.setx(turtle.xcor()+lado)

        # muda de linha
        turtle.penup()
        turtle.goto(posx,turtle.ycor()-lado)
        turtle.pendown()
    turtle.hideturtle()


triângulo(-100,280,50)
grelha(6,-100,280,50,'darkgreen')

a.exitonclick()