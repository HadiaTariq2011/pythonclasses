import random

size = 5

maze = []

for i in range(size):
    row = []
    for j in range(size):
        if random.randint(1, 4) == 1:
            row.append("#")  # Wall
        else:
            row.append(".")  # Path
    maze.append(row)

maze[0][0] = "P"      # Player
maze[size-1][size-1] = "E"  # Exit

x, y = 0, 0

while True:
    for row in maze:
        print(" ".join(row))

    move = input("Move (W/A/S/D): ").upper()

    nx, ny = x, y

    if move == "W":
        nx -= 1
    elif move == "S":
        nx += 1
    elif move == "A":
        ny -= 1
    elif move == "D":
        ny += 1

    if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] != "#":

        if maze[nx][ny] == "E":
            print("🎉 Congratulations! You escaped the maze!")
            break

        maze[x][y] = "."
        x, y = nx, ny
        maze[x][y] = "P"

    print()