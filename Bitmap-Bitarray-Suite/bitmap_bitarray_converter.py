#
# Author: Kılıçarslan SIMSIKI
#


import pygame


def main(height, width, barray):
    pygame.init()

    # create a screen:
    pxsize = 20

    screen_height = height*pxsize
    screen_width = width*pxsize
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bitmap Bitarray Converter")

    # (red, green, blue)
    c = (0, 150, 255)
    color_ledoff = (0, 0, 0)
    color_ledon = (255, 255, 0)

    # create a 2D list to keep track of the cell colors
    if len(barray) > 0:
        # read the matrix from the 2D array
        cell_colors = [[color_ledon if barray[y][x] == 1 else color_ledoff for y in range(height)] for x in range(width)]
    else:
        # create a 2D array
        cell_colors = [[color_ledoff for y in range(height)] for x in range(width)]

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # check if Ctrl+S keys were pressed
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    write_grid_to_file(height, width, cell_colors, color_ledon)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the mouse position
                pos = pygame.mouse.get_pos()
                # determine the column and row of the cell that was clicked
                col = pos[0] // pxsize
                row = pos[1] // pxsize
                # toggle the color of the cell
                if cell_colors[col][row] == color_ledoff:
                    cell_colors[col][row] = color_ledon
                else:
                    cell_colors[col][row] = color_ledoff

        # draw the cells
        for x in range(0, screen_width, pxsize):
            for y in range(0, screen_height, pxsize):
                # get the color of the cell
                color = cell_colors[x // pxsize][y // pxsize]
                pygame.draw.rect(screen, color, pygame.Rect(x, y, pxsize, pxsize))

                # draw the grid lines
                pygame.draw.line(screen, c, (x, y), (x + pxsize, y), 1) # horizontal line
                pygame.draw.line(screen, c, (x, y), (x, y + pxsize), 1) # vertical line
                    
        pygame.display.update()
    
    pygame.quit()

# function to read from file into a 2D array
def read_grid_from_file():
    barray = [] # will contain lists. e.g [[1,0,1,0], [0,0,0,1]]
    row = []
    with open("grid.cpp", "r") as f:
        for _ in range(3):
            f.readline()
        while True:
            line = f.readline()
            if not line:
                # Reached the end of the file
                break
            if line != "};":
                row = line.strip().split("},")[0].split("{")[1].split(",")
                if row[-1].endswith("}"):
                    # remove the last character '}'
                    row[-1] = row[-1][:-1] 
                row = [int(x) for x in row]
                barray.append(row)
            
    main(len(barray), len(barray[0]), barray)
    
    

# function to write the current grid to a file
def write_grid_to_file(height, width, cell_colors, color_ledon):
    with open("grid.cpp", "w") as f:
        f.write(f"// {height}x{width}\n")
        f.write("std::vector<std::vector<int>> PatternAnimator::grid ="+"\n")
        f.write("{"+"\n")
        for y in range(height):
            f.write("\t{")
            for x in range(width):
                if cell_colors[x][y] == color_ledon:
                    if x != width-1:
                        f.write("1,")
                    else:
                        f.write("1")
                else:
                    if x != width-1:
                        f.write("0,")
                    else:
                        f.write("0")
            if y != height-1:
                f.write("},")
            else:
                f.write("}")
            f.write("\n")
        f.write("};")
