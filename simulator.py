import os,sys
import Image
from PIL import Image
import numpy as np

class simulator():
  def __init__(self):
    self.reward = 0
    #self.screen = np.random.rand(200,200)
    self.bar1 = 1
    self.bar2 = 1

  def reset_game(self):
    os.system('./reset_game.sh ')
    [bb1, bb2, self.screen] = self.img_feature()
    return

  def step(self,action):
    os.system('./dqn2control.sh ' + str(action) )
    # play lf2
#    os.system('sleep 0.3')
    [bb1, bb2, self.screen] = self.img_feature()
    self.reward = self.bar1 - bb1 - self.bar2 + bb2

    return self.reward, self.screen


  def get_observation(self):
    return self.screen


  def img_feature(self):
    os.system('./capture_window.sh')

    img = Image.open('lf2.png')
#    print "Image size :", img.size

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

    bar1 = (blood1*1.0)/maxbar*500  #enemy
    bar2 = (blood2*1.0)/maxbar*500  #me

    gray = img.crop((0, 108, 793, 549))
    gray = gray.resize( (100, 100), Image.ANTIALIAS ).convert('L')
    #gray.save('tmp.jpg')
    listgray = list(gray.getdata())  #feature vector
    listgray = np.reshape(listgray, (100, 100))
    #print listgray  

    return bar1, bar2, listgray
