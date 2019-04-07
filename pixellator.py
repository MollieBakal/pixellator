import Image
import sys
import argparser
import math

parser = argparse.ArgumentParser(description = "Convert images to pixel squares and hexagons")
parser.add_argument("--filename", metavar = 'f', help = "The file which you want to input")
parser.add_argument("--mode", metavar = 'm', help = "The mode which you want to run in; h for hexagon, s for square")
parser.add_argument("--rows", metavar = 'r', help = "The number of rows you want of shapes", type = int)
args = parser.parse_args()
arg = vars(args)
(int) rows = arg['--rows']
image = Image.open(arg['--filename']).load()
hperrow = image.size[1]/rows
if arg['--mode'] == "h":
    #hex mode
    #with flat-top, becaus epointy top was a headache.
    i = 1/2
    currLEdge = 0
    rad = (hperrow/sqrt(3))
    centerList = [,]
    while i < rows:
        #hperrow is height of 1 hexagon in pixels, or rad*sqrt(3)
        #width needs to be rad
        centerList.append((currLEdge + rad, i*hperrow))
        i = i + 1
    #Now for generating the other columns.
    currLEdge = currLEdge + 
    while(currLEdge + 2*rad) < image.size[0] :
        
        


elif arg['--mode'] == "s":
    
