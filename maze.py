import random

def draw_diagonal(x, y, x2, y2, color='black'):
	#format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" \
            y2="{y2}" stroke="{color}" />'

with open("maze.xml", "w") as xml:
    print("file created")

def file_write(data):
    with open("maze.xml", "a") as xml_file:
        xml_file.write(data)

def make_maze(num, color = "black" , height = 500):
	#num is the number of diagonals across and down
	#filename is the output file name
    width = height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    step=height // num
    #write the header for the file
    print(header)
    file_write(header)
    #loop through 
    for row in range(0, height, step):
      for col in range(0, width, step):
        #choose a random direction for the diagonal line
        if random.choice([0, 1]) == 0:
        	#write the line
            print(draw_diagonal(col, row, col + step, row + step, color))
            file_write(draw_diagonal(col, row, col + step, row + step, color))
        else:
        	#write the line
            print(draw_diagonal(col + step, row, col, row + step, color))
            file_write(draw_diagonal(col + step, row, col, row + step, color))
    #write the footer
    footer = f'</svg>'
    print(footer)
    file_write(footer)

if __name__ == "__main__":
    make_maze(50, color="darkviolet" )
