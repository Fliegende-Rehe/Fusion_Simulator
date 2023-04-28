from .fusion import *


class Trajectory:
    def __init__(self, spline, tolerance: float) -> None:
        strokes = spline.geometry.evaluator.getStrokes(0.0, 1.0, tolerance)[1]
        self.points = [list(s.asArray()) for s in strokes]
        logger(f'The trajectory consists of {len(self.points)} points')

    def update_points(self, origin: list[float]) -> list[list[float]]:
        self.points = [list(map(sum, zip(origin, p))) for p in self.points]
        return self.points