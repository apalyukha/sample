class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False

    def toggle(self):
        self.status = not self.status


class SquareButton(Button):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


b = SquareButton(10, 20, 200)
