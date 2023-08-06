from PySVG.Draw import Rect
from PySVG import Section


class Bar(Rect):
    def __init__(self, fill=(0, 0, 0), fill_opacity=1, stroke=None, stroke_width=1):
        super().__init__(0, 0, 0, 0)
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.stroke = stroke
        self.stroke_width = stroke_width

        self.index = 0
        self.value = 0


class Group(Section):
    def __init__(self, parent):
        super().__init__(0, 0)
        self.plot = parent
        self.index = 0
        self.bars = []
        self.filled = 0.50

        self.width = 1

    @property
    def max_index(self):
        bar_indices = [bar.index for bar in self.bars]
        if bar_indices:
            return max(bar_indices)

        return 0

    @property
    def bar_width(self):
        return self.width * self.filled / self.max_index

    @property
    def bar_space(self):
        max_index = self.max_index
        return self.width * (1 - self.filled) / (max_index + 1)

    def add_bar(self, bar: Bar, x: int, y: float):
        bar = bar.copy()
        bar.index = x
        bar.value = y
        self.bars.append(bar)

    def set_bars(self):
        n = self.max_index
        s = self.bar_space
        w = self.bar_width
        exes = [(i + 1) * s + i * w for i in range(n)]

        zero = self.plot.cart2pixel_y([0])[0]

        for bar in self.bars:
            bar.x, bar.w = self.plot.cart2pixel_x([exes[bar.index - 1], w])
            y = self.plot.cart2pixel_y([bar.value])[0]
            bar.y = y
            bar.h = zero - y

            self.add_child(bar)

    def construct(self):
        self.x = self.plot.cart2pixel_x([self.index - self.width/2])[0]
        self.set_bars()

        return super().construct()
