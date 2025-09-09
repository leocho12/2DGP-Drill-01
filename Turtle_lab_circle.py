import turtle

def draw_circe(x,y,z):
    turtle.penup()
    turtle.goto(x,y)
    turtle.stamp()
    turtle.goto(x,y-z)
    turtle.pendown()
    turtle.circle(z)

turtle.shape('turtle')
draw_circe(0,0,50)
draw_circe(200,200,100)
draw_circe(100,-100,50)