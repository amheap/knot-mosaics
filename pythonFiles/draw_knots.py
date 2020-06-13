#!opt/anaconda3/bin/python
"""
This file uses functions from mosaic_drawing.py to draw knots from a given csv file, or individual knots from a given
matrix

IF YOU ARE DRAWING KNOTS FROM A CSV FILE:
Comment out the section for drawing an individual knot at the end of the script
We assume the csv is of a specific format, with columns: (OtherName), Name, Vector, Crossings, Mosaic, TileNum
  - That is, the first column is not used, the second is the name of the knots, the third is the vector that filled in
  the layout for the knot, the fourth is the number of crossings in the mosaic, the fifth is the size of the mosaic, and
  the sixth is the number of non-blank tiles used

Make sure to set table_path to your own path to the csv

IF YOU ARE DRAWING ONE KNOT:
Comment out the section for drawing from a csv at the beginning of the script
Specify the mosaic size, how large to scale the image, the layout, the vector to fill in the layout, and the save path

James Canning, May 2020
"""

from mosaic_drawing import *
import pandas as pd

# defining layouts
m4_12 = np.array([[0,  2,  1,  0],
                  [2, -1, -1,  1],
                  [3, -1, -1,  1],
                  [0,  3,  4,  0]])
m5_17 = np.array([[0,  2,  1,  0,  0],
                  [2, -1, -1,  1,  0],
                  [3, -1, -1, -1,  1],
                  [0,  3, -1, -1,  4],
                  [0,  0,  3,  4,  0]])
m6_22 = np.array([[0,  2,  1,  0,  0,  0],
                  [2, -1, -1,  1,  0,  0],
                  [3, -1, -1, -1,  1,  0],
                  [0,  3, -1, -1, -1,  1],
                  [0,  0,  3, -1, -1,  4],
                  [0,  0,  0,  3,  4,  0]])
m6_24 = np.array([[0,  0,  2,  1,  0,  0],
                  [0,  2, -1, -1,  1,  0],
                  [2, -1, -1, -1, -1,  1],
                  [3, -1, -1, -1, -1,  4],
                  [0,  3, -1, -1,  4,  0],
                  [0,  0,  3,  4,  0,  0]])
m6_27 = np.array([[0,  2,  1,  2,  1,  0],
                  [2, -1, -1, -1, -1,  1],
                  [3, -1, -1, -1, -1,  4],
                  [0,  3, -1, -1, -1,  1],
                  [0,  0,  3, -1, -1,  4],
                  [0,  0,  0,  3,  4,  0]])
m6_32 = np.array([[0,  2,  1,  2,  1,  0],
                  [2, -1, -1, -1, -1,  1],
                  [3, -1, -1, -1, -1,  4],
                  [2, -1, -1, -1, -1,  1],
                  [3, -1, -1, -1, -1,  4],
                  [0,  3,  4,  3,  4,  0]])
m7_27 = np.array([[0,  2,  1,  0,  0,  0,  0],
                  [2, -1, -1,  1,  0,  0,  0],
                  [3, -1, -1, -1,  1,  0,  0],
                  [0,  3, -1, -1, -1,  1,  0],
                  [0,  0,  3, -1, -1, -1,  1],
                  [0,  0,  0,  3, -1, -1,  4],
                  [0,  0,  0,  0,  3,  4,  0]])
m7_29 = np.array([[0,  2,  1,  0,  0,  0,  0],
                  [2, -1, -1,  1,  0,  0,  0],
                  [3, -1, -1, -1,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1,  4,  0],
                  [0,  3, -1, -1,  4,  0,  0],
                  [0,  0,  3,  4,  0,  0,  0]])
m7_31 = np.array([[0,  0,  2,  1,  0,  0,  0],
                  [0,  2, -1, -1,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3, -1, -1, -1, -1,  4],
                  [0,  0,  3, -1, -1,  4,  0],
                  [0,  0,  0,  3,  4,  0,  0]])
m7_32 = np.array([[0,  2,  1,  0,  0,  0,  0],
                  [2, -1, -1,  1,  0,  0,  0],
                  [3, -1, -1, -1,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3,  4,  3, -1, -1,  4],
                  [0,  0,  0,  0,  3,  4,  0]])
m7_34 = np.array([[0,  2,  1,  0,  0,  0,  0],
                  [2, -1, -1,  1,  0,  0,  0],
                  [3, -1, -1, -1,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3, -1, -1, -1, -1,  4],
                  [0,  0,  3,  4,  3,  4,  0]])
m7_36 = np.array([[0,  2,  1,  2,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [2, -1, -1, -1, -1, -1,  4],
                  [3, -1, -1, -1, -1,  4,  0],
                  [0,  3, -1, -1,  4,  0,  0],
                  [0,  0,  3,  4,  0,  0,  0]])
m7_37 = np.array([[0,  2,  1,  2,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1,  4,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3,  4,  3, -1, -1,  4],
                  [0,  0,  0,  0,  3,  4,  0]])
m7_39 = np.array([[0,  2,  1,  2,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1,  4,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3, -1, -1, -1, -1,  4],
                  [0,  0,  3,  4,  3,  4,  0]])
m7_41 = np.array([[0,  2,  1,  2,  1,  0,  0],
                  [2, -1, -1, -1, -1,  1,  0],
                  [3, -1, -1, -1, -1, -1,  1],
                  [2, -1, -1, -1, -1, -1,  4],
                  [3, -1, -1, -1, -1, -1,  1],
                  [0,  3, -1, -1, -1, -1,  4],
                  [0,  0,  3,  4,  3,  4,  0]])

layoutDict = {"4-12": m4_12, "5-17": m5_17, "6-22": m6_22, "6-24": m6_24, "6-27": m6_27, "6-32": m6_32, "7-27": m7_27,
              "7-29": m7_29, "7-31": m7_31, "7-32": m7_32, "7-34": m7_34, "7-36": m7_36, "7-37": m7_37, "7-39": m7_39,
              "7-41": m7_41}

# ****************************************
''' For drawing knots from a csv file '''
# ****************************************

"""
# path to csv file
table_path = "C://Users//Owner//Documents//Geneseo//Heap Research//files//7_1-sorted-trimmed.csv"
df = pd.read_csv(table_path)
newVectors = []
# takes the string vectors and converts them to numpy arrays
for v in df.Vector:
    newVectors.append(np.array(list(map(np.int, v.strip().replace('[', '').replace(']', '').split(',')))))
df.Vector = newVectors

# Set the scale of the knot, AKA the size
tile_scale = 10

# the following block can be used to sort the DataFrame and remove duplicates
'''
# the order in which to sort the columns
df = df.sort_values(['Layout', 'Crossings'])
df = df.drop_duplicates(['Name'])
'''


# Path to folder where images will be saved
save_path = "C://Users//Owner//Documents//Geneseo//Heap Research//images//knots//7-29//eps//"

for i in range(df.shape[0]):
    row = df.values[i]
    _, name, vector, crossings, mosaic_size, tile_number = row
    name = name.strip()
    filename = save_path + str(name) + ".eps"
    mTemp = layoutDict[str(mosaic_size) + '-' + str(tile_number)].copy()
    mTemp[mTemp == -1] = vector
    # Use the following for making png files
    #surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, mosaic_size * tile_scale, mosaic_size * tile_scale)
    # Use the following for making eps files
    surface = cairo.PSSurface(filename,  mosaic_size * tile_scale, mosaic_size * tile_scale)
    draw_knot(mTemp, surface, tile_scale, mosaic_size)
    # If creating png files, uncomment the next line (this can be done in addition to the eps files)
    #surface.write_to_png(save_path + str(name) + ".png")
"""


# ****************************************
''' For drawing knots from a given set of vectors'''
# ****************************************

# Specify size of mosaic and how large to scale the image
mosaic_size = 7
tile_scale = 50
# Choose your layout
m = layoutDict['7-29'].copy()
# Add your vector
v = [10,9,9,10,7,10,7,10,7,9,7,9,8,9,10]
m[m == -1] = v

save_path = "C://Users//Owner//Documents//Geneseo//Heap Research//images//knots//test3"
# Use the following line for making eps files (comment out otherwise)
surface = cairo.PSSurface(save_path + '.eps', mosaic_size * tile_scale, mosaic_size * tile_scale)

# Use the following line if you are ONLY making a png file (comment out otherwise)
#surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, mosaic_size * tile_scale, mosaic_size * tile_scale)

draw_knot(m, surface, tile_scale, mosaic_size)
# If creating a png file, uncomment the next line (you can run this line while also creating an eps file)
surface.write_to_png(save_path + ".png")

