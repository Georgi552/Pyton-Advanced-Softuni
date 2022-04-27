def fill_the_box(height, length, width, *args):
    size_of_box = height * length * width
    cubes_in_box = 0
    total_cubes = 0
    for el in args:
        if el != "Finish":
            cubes_in_box += el
            total_cubes += el
            if cubes_in_box >= size_of_box:
                cubes_in_box = size_of_box
        else:
            break

    if size_of_box > cubes_in_box:
        return f"There is free space in the box. You could put {size_of_box - cubes_in_box} more cubes."
    if size_of_box <= cubes_in_box:
        return f"No more free space! You have {total_cubes - size_of_box} more cubes."




print(fill_the_box(2, 8, 1, 2, 1, 7, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5,"Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
