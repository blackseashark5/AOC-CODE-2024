import numpy as np
from scipy.stats import chisquare


def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    robots = []
    for line in lines:
        p, v = line.split(" v=")
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v.split(","))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robots(robots, size, t):
    width, height = size
    positions = []
    for (px, py), (vx, vy) in robots:
        new_x = (px + vx * t) % width
        new_y = (py + vy * t) % height
        positions.append((new_x, new_y))
    return positions

def analyze_coordinates(robots, size, axis, period):
    positions = [
        [pos[axis] for pos in move_robots(robots, size, t)]
        for t in range(period)
    ]
    chi_scores = []
    for t, coords in enumerate(positions):
        counts, _ = np.histogram(coords, bins=np.arange(-0.5, size[axis] + 0.5))
        chi, _ = chisquare(counts)
        chi_scores.append((t, chi))
    chi_scores.sort(key=lambda x: x[1], reverse=True)  # Sort by chi-square value
    return chi_scores[0][0]  # Return time with max chi-square value

def extended_gcd(a, b):
    """Extended GCD to solve the diophantine equation."""
    if b == 0:
        return a, 1, 0
    gcd_, x1, y1 = extended_gcd(b, a % b)
    return gcd_, y1, x1 - (a // b) * y1

def solve_diophantine(a1, r1, a2, r2):
    """Find intersection of t = a1 * m + r1 and t = a2 * n + r2."""
    g, x, y = extended_gcd(a1, a2)
    if (r2 - r1) % g != 0:
        return None
    lcm = (a1 * a2) // g
    t = (r1 + (r2 - r1) * x * (a1 // g)) % lcm
    return t % lcm

def find_alignment(file_path):
    size = (101, 103)  # Periodicity of x and y coordinates
    robots = parse_input(file_path)

    # Analyze x and y coordinates independently
    x_peak = analyze_coordinates(robots, size, axis=0, period=size[0])
    y_peak = analyze_coordinates(robots, size, axis=1, period=size[1])

    # Solve for t using Chinese Remainder Theorem
    t = solve_diophantine(size[0], x_peak, size[1], y_peak)
    return t

if __name__ == "__main__":
    input_file = "input.txt"
    t = find_alignment(input_file)
    print(f"The first alignment occurs at t = {t}")
