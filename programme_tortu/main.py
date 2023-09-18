import turtle

def escalier(taille, nb, rotate):
    for i in range(0, nb):
        t.forward(taille)
        t.left(rotate)
        t.forward(taille)
        t.right(rotate)
        taille = taille-3
    t.forward(taille)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)
        t.speed(10)

t = turtle.Turtle()
#escalier(30, 20, 90)
a = 50
for i in range(0, 100):
    carre(a)
    a = a+2
turtle.done()