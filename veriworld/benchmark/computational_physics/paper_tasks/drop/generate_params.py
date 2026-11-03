"""Generate surface + target parameters for drop-to-target test."""
import json
import random
import math
import os

def generate(seed=0):
    rng = random.Random(seed)

    # Flat surface at some height
    surface_z = rng.uniform(350, 500)

    # Ball starts at center of surface
    ball_x = 0.0
    ball_y = 0.0

    # Target circle on the ground — offset from directly below the ball
    # So the agent must tilt/curve the surface to aim
    angle = rng.uniform(0, 2 * math.pi)
    dist = rng.uniform(150, 350)
    target_x = round(ball_x + dist * math.cos(angle), 1)
    target_y = round(ball_y + dist * math.sin(angle), 1)
    target_z = 15.0  # ground level
    target_radius = rng.uniform(40, 80)

    return {
        "seed": seed,
        "surface_z": round(surface_z, 1),
        "ball_start": [round(ball_x, 1), round(ball_y, 1), round(surface_z + 25, 1)],
        "target": [target_x, target_y, target_z],
        "target_radius": round(target_radius, 1),
        "grid_n": 40,
        "grid_spacing": 12.0,
        "ball_radius": 15.0,
    }

if __name__ == "__main__":
    import sys
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    p = generate(seed)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "params.json")
    with open(out, "w") as f:
        json.dump(p, f, indent=2)
    print(f"Generated (seed={seed}):")
    print(f"  Surface Z={p['surface_z']}")
    print(f"  Ball start={p['ball_start']}")
    print(f"  Target={p['target']}, radius={p['target_radius']}")
