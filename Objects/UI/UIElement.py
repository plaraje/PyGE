class UIElement:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.enabled = True
        self.parent = None
        self.children = []
        self.z_index = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return child

    def remove_child(self, child):
        if child in self.children:
            child.parent = None
            self.children.remove(child)

    def get_absolute_position(self):
        x, y = self.x, self.y
        current = self.parent
        while current:
            x += current.x
            y += current.y
            current = current.parent
        return x, y

    def handle_event(self, event):
        if not self.visible or not self.enabled:
            return False
        
        for child in reversed(self.children):
            if child.handle_event(event):
                return True
        return False

    def update(self, delta_time):
        if not self.visible or not self.enabled:
            return
        
        for child in self.children:
            child.update(delta_time)

    def render(self, render_context):
        if not self.visible:
            return
        
        for child in sorted(self.children, key=lambda x: x.z_index):
            child.render(render_context)

    def contains_point(self, x, y):
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)
