length = 14
width = 11
tiles_needed = length * width
extra_tiles = tiles_needed * 0.10
total_tiles = tiles_needed + extra_tiles

boxes = total_tiles // 12
remainder = total_tiles % 12

if remainder > 0:
    boxes = boxes + 1
print(f"I need {boxes} boxes")