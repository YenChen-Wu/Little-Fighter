import os,sys
import Image
from PIL import Image


img = Image.open('lf2.png')
print "Image size :", img.size

bar1 = list(img.crop((57, 16, 180, 25)).getdata())
bar2 = list(img.crop((255, 16, 378, 25)).getdata())
maxbar = len(bar1)

blood1 = 0
blood2 = 0
for i in range(maxbar):
    if bar1[i][0] == 255:
        blood1 += 1
    if bar2[i][0] == 255:
        blood2 += 1

print "Player 1 Blood :", (blood1*1.0)/maxbar*500
print "Player 2 Blood :", (blood2*1.0)/maxbar*500

gray = img.crop((0, 108, 793, 549))
gray = gray.resize( (200, 200), Image.ANTIALIAS ).convert('L')
#gray.save('tmp.jpg')
listgray = list(gray.getdata())
print listgray
