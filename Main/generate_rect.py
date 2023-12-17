import numpy as np

def generate_rectangles(target_area):
    rectangles = []
    current_area = 0

    while current_area < target_area:
        width = np.random.randint(10, 40)
        height = np.random.randint(10, 40)

        if current_area + width * height <= target_area:
            rectangles.append((width, height))
            current_area += width * height

    return rectangles

target_area = 4000
rectangles = generate_rectangles(target_area)

for i, rectangle in enumerate(rectangles, 1):
    print(f"{i}. Dikdörtgen: {rectangle[0]} x {rectangle[1]}")

total_area = sum(width * height for width, height in rectangles)
print(f"\nToplam Alan: {total_area} birim kare")
