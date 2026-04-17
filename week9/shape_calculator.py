import geometry_utils

shape_area = {
    "circle":    geometry_utils.circle_area,
    "rectangle": geometry_utils.rectangle_area,
    "triangle":  geometry_utils.triangle_area,
}

print("Available shapes: circle, rectangle, triangle")
shape = input("Enter shape type: ").strip().lower()

if shape not in shape_area:
    print("Input Error: Invalid shape.")
else:
    if shape == "circle":
        radius = float(input("Enter radius: "))
        result = shape_area[shape](radius)
    elif shape == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        result = shape_area[shape](width, height)
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = shape_area[shape](base, height)

    if result is not None:
        print(f"Area: {result}")