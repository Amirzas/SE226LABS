import geometry_utils

shape_functions = {
    "circle_area":         geometry_utils.circle_area,
    "circle_perimeter":    geometry_utils.circle_perimeter,
    "rectangle_area":      geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area":       geometry_utils.triangle_area,
}

shape_inputs = {
    "circle_area":         ["radius"],
    "circle_perimeter":    ["radius"],
    "rectangle_area":      ["width", "height"],
    "rectangle_perimeter": ["width", "height"],
    "triangle_area":       ["base", "height"],
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation = input("Enter the operation you want to perform: ").strip().lower()

if operation not in shape_functions:
    print("Input Error: Invalid operation.")
else:
    dims = []
    valid = True
    for dim_name in shape_inputs[operation]:
        value = input(f"Enter {dim_name}: ")
        if value.lstrip("-").replace(".", "").isdigit():
            dims.append(float(value))
        else:
            print("Input Error: Please enter a valid number.")
            valid = False
            break

    if valid:
        result = shape_functions[operation](*dims)
        if result is not None:
            print(f"Result: {result}")