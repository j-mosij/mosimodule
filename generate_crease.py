#!/usr/bin/env python3
"""
Pure Python 3 helper to generate golden-ratio Fibonacci crease coordinates.
No external dependencies. Output can be used for further visualization or export.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def fibonacci_spiral_points(n=200, scale=1.0):
    points = []
    for i in range(n):
        theta = i * 2 * math.pi / PHI  # golden angle
        r = math.sqrt(i) * scale
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    return points

if __name__ == "__main__":
    pts = fibonacci_spiral_points(100, 0.2)
    print("# Mosimodule golden ternary Fibonacci points")
    for p in pts:
        print(f"{p[0]:.6f},{p[1]:.6f}")
