import matplotlib.pyplot as plt
import os
import sys

while True:
    route_file = input("Please enter the route filename or type 'stop' to end the program:")
    if route_file.lower() == "stop":
        sys.exit()
    elif not os.path.isfile(route_file):
        print("File not found. Please enter a valid filename or 'stop' to exit the program.")
        continue

    with open(route_file, "r") as readfile:
        route = readfile.read()
        directions = route.split("\n")

    start_x = int(directions[0])
    start_y = int(directions[1])
    start_coords = [start_x, start_y]
    print("Start coordinates:", start_coords)

    coord_x = start_x
    coord_y = start_y

    del directions[0:2]

    def plot_grid(coord_x, coord_y):
        coordinates = []
        for item in directions:
            if coord_x < 1 or coord_x > 12:
                print("Error: X-axis coordinate is out of limits.")
                break
            elif coord_y < 1 or coord_y > 12:
                print("Error: Y-axis coordinate is out of limits.")
                break
            else:
                if item == "N":
                    coord_y += 1
                elif item == "S":
                    coord_y -= 1
                elif item == "E":
                    coord_x += 1
                elif item == "W":
                    coord_x -= 1
                coordinates.append([coord_x, coord_y])
        return coordinates

    coordinates = plot_grid(coord_x, coord_y)
    print(plot_grid(coord_x, coord_y))
    print("Finish coordinates:", coordinates[-1])

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)

    for coord in coordinates:
        x, y = coord
        ax.plot(x, y, 'bo')

    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_title('Route Guidance Grid')

    plt.grid(True)
    plt.show()