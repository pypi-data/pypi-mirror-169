from PySVG import Section


class Scatter(Section):
    def __init__(self, plot):
        super().__init__(plot.x, plot.y)

