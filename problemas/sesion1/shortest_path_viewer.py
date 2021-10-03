from shortest_path import process
from labyrinthviewer import LabyrinthViewer
g, path = process(40, 60)
lv = LabyrinthViewer(g, canvas_width=600, canvas_height=400, margin=10)
lv.add_path(path)
lv.run()