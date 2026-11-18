# COMP 303 Project 2

Dijkstra vs A* shortest path algorithms.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/dijkstra.py      # Part 1: reads N (< 20), S, D
python src/astar.py         # Part 2: reads N (< 20), S, D
python src/experiments.py   # Items 3 & 6: N = 10 ... 2000, saves plots to figures/
python src/draw_graph.py 10 # Draw the graph for N = 10
```
