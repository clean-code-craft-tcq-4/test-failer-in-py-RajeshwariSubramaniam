def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print("{:<2} | {:<6} | {}".format((i * 5 + j) + 1,
                                              major,
                                              minor))
    return len(major_colors) * len(minor_colors)

