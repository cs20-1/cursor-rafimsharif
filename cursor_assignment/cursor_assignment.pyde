def setup():
    size(500, 500)


def target(x, y):
    fill(255, 0, 0)
    circle(x, y, 100)
    fill(255)
    circle(x, y, 75)
    fill(255, 0, 0)
    circle(x, y, 50)
    fill(255)
    circle(x, y, 25)


def draw():
    background(0)
    target(mouseX-50, mouseY-50)
    
