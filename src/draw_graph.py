"""Draw the city graph as an image (odd nodes on top, even nodes on bottom).

Usage:
    python src/draw_graph.py            # N = 10
    python src/draw_graph.py 8          # N = 8
"""

import os
import sys

import matplotlib.pyplot as plt

from graph import build_graph

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def node_position(i):
    """Odd nodes on the top row, even nodes on the bottom row (like the PDF figure)."""
    x = (i - 1) // 2
    y = 1 if i % 2 == 1 else 0
    return x, y


def draw(n):
    graph = build_graph(n)
    pos = {i: node_position(i) for i in graph}

    fig, ax = plt.subplots(figsize=(max(6, n * 0.9), 4))

    # Each undirected edge once (i < j); weights are symmetric.
    for i, edges in graph.items():
        for j, w in edges:
            if i >= j:
                continue
            (x1, y1), (x2, y2) = pos[i], pos[j]
            ax.plot([x1, x2], [y1, y2], color="#9aa5b1", linewidth=1, zorder=1)
            # Label closer to the smaller node so crossing edges don't overlap.
            t = 0.3
            lx, ly = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
            ax.text(lx, ly, str(w), fontsize=8, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"), zorder=2)

    for i, (x, y) in pos.items():
        ax.scatter(x, y, s=600, color="#ffffff", edgecolors="#d64545", linewidths=2, zorder=3)
        ax.text(x, y, str(i), fontsize=11, ha="center", va="center", color="#d64545",
                fontweight="bold", zorder=4)

    ax.set_title(f"City graph (N={n}): edge if |i-j| <= 3, weight w_ij = i + j")
    ax.set_xlim(-0.5, max(x for x, _ in pos.values()) + 0.5)
    ax.set_ylim(-0.4, 1.4)
    ax.axis("off")
    fig.tight_layout()

    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.abspath(os.path.join(OUT_DIR, f"graph_N{n}.png"))
    fig.savefig(path, dpi=150)
    print(f"Saved: {path}")


if __name__ == "__main__":
    draw(int(sys.argv[1]) if len(sys.argv) > 1 else 10)
