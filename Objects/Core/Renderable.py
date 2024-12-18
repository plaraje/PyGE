class Renderable:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = 0
        self.scale = 1
        self.z_index = 0
        self.visible = True

    def render(self, ctx):
        pass 

    def update(self, delta_time):
        pass 

    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

    def get_center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)

    def display(self, ctx):
        if self.visible:
            self.render(ctx)
