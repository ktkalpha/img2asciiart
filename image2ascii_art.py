from PIL import Image

# img = Image.open("./cat.png").convert('L')
img = Image.open("./cat.png")
img = img.resize((32, 32))

bw = 127
counter = 0
# print(list(img.getdata()))
for c in list(img.getdata()):
    col = list(c)
    col.append('')
    col[3] = col[3] if isinstance(col[3], int) else 255
    if counter >= 32:
        print("")
        counter = 0
    if col[3] > 220 and col[0] < bw and col[1] < bw and col[2] < bw:
        print("##", end="")
    else:
        print("  ", end="")
    counter+=1
# img.show()