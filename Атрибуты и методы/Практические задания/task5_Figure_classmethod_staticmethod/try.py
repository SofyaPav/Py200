import math

class TriangleCalculator:
    @staticmethod
    def area_by_angle(a, b, angle):
        return 0.5 * a * b * math.sin(angle)

print(TriangleCalculator.area_by_angle(3, 4, math.radians(90)))