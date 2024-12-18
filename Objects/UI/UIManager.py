class UIManager:
    def __init__(self):
        self.elements = []
        self.focused_element = None

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            if self.focused_element == element:
                self.focused_element = None

    def handle_event(self, event):
        for element in reversed(self.elements):  # Procesar desde el elemento superior
            if element.visible and element.enabled:
                element.handle_event(event)

    def update(self, delta_time):
        for element in self.elements:
            if element.visible and element.enabled:
                element.update(delta_time)

    def render(self, render_context):
        for element in self.elements:
            if element.visible:
                element.render(render_context)

    def clear(self):
        self.elements.clear()
        self.focused_element = None
