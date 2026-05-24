class point:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"x = {self.x}, y = {self.y}")

class circle(point):
    def __init__ (self, x = 0, y = 0, r = 5):
        super().__init__(x, y)
        self.r = r

p = point(10)
triga = circle(r = 1)
print(triga.r, triga.x, triga.y)
p.show()
triga.show()