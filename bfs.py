"""
Breadth-first Ssearch
"""
import time
import tkinter as tk
from typing import Dict, Union, Set, List, Tuple

# Data types used in this script
Vertex = Union[int, str]
Graph = Dict[Vertex, Set[Vertex]]
PositionMap = Dict[Vertex, Tuple[Union[int, float]]]
Path = List[Vertex]

# Graph data for demonstration
demo_root: Vertex = "A"
demo_goal: Vertex = "G"
demo_graph: Graph = {
  "A": {"B", "D"},
  "B": {"C"},
  "C": {"G"},
  "D": {"C", "E"},
  "E": {"F"},
  "F": {},
  "G": {"F"},
}
node_positions: PositionMap = {
  "A": (100, 100),
  "B": (200, 100),
  "C": (200, 200),
  "D": (100, 200),
  "E": (200, 300),
  "F": (300, 300),
  "G": (300, 200),
}

"""
Performs Breadth-first Search on a graph and returns true if the goal was found.

Args:
- root (Vertex): A vertex in the graph with which to start the search from
- goal (Vertex): The vertex that is the goal of the search
- graph (Graph): The graph that is the search-space of the search algorithm

Returns:
  True, if the goal was found, else False
"""
def perform_bfs(root: Vertex, goal: Vertex, graph: Graph, canvas) -> bool:
  que: List[Vertex] = [root]
  vis: List[Vertex] = [root]

  while que:
    v = que.pop(0)
    print(v)

    draw_path(canvas, [v], color="orange")
    time.sleep(.5)

    if v == goal:
      draw_path(canvas, [v], color="green")
      return True

    for av in graph[v]:
      if not av in vis:
        que.append(av)
        vis.append(av)

  return False

def draw_path(canvas, path: Path, color=None):
  start = path[0]

  for i in range(1, len(path)):
    end = path[i]

    x1, y1 = node_positions[start]
    x2, y2 = node_positions[end]

    # Draw line from start to end
    canvas.create_line(x1, y1, x2, y2)

    # Draw start node
    canvas.create_oval(x1-20, y1-20, x1+20, y1+20, fill=color if color else "black")
    canvas.create_text(x1, y1, text=start, fill="black" if color else "white")
    canvas.update()
    time.sleep(.5)

    start = end

  x1, y1 = node_positions[start]

  # Draw start node
  canvas.create_oval(x1-20, y1-20, x1+20, y1+20, fill=color if color else "black")
  canvas.create_text(x1, y1, text=start, fill="black" if color else "white")
  canvas.update()

def draw_graph(canvas, graph: Graph):
  for v in graph:
    for n in graph[v]:
      draw_path(canvas, [v, n])

if __name__ == "__main__":
  window = tk.Tk()
  window.title("Breadth-first Search UI demo")

  canvas = tk.Canvas(window, width=500, height=500)
  canvas.pack()

  # input("[PRESS ENTER TO START]")

  draw_graph(canvas, demo_graph)

  # Perform the algorithm
  print(perform_bfs(demo_root, demo_goal, demo_graph, canvas))

  # Show the window
  window.mainloop()