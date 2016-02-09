import math

pic = "P3 500 500 255 "
for y in range(500):
    for x in range(500):
        r = (math.ceil((math.sqrt(abs(256-x)**3))))%255
        g = (math.ceil(math.sqrt(abs(256-y)**3)))%255
        b = (math.ceil((math.sqrt((abs(256-x)**3) + (abs(256-y)**3)))))%255
        pic += str(r) + " " + str(g) + " " + str(b) + " "

f = open("pic.ppm", "w")
f.write(pic)
f.close()
