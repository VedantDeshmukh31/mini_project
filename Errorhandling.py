from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import colors
import cv2

def rgb_to_hex(rgb_color):
  hex_color="#"
  for i in rgb_color:
    i=int(i)
    hex_color+= ("{:02x}".format(i))

  return hex_color

#rgb_to_hex((255,0,0))

img_name='images\Y181.jpg'
raw_img=cv2.imread(img_name)
raw_img=cv2.cvtColor(raw_img,cv2.COLOR_BGR2RGB)





img=cv2.resize(raw_img,(900,600),interpolation=cv2.INTER_AREA)
#img.shape

img=img.reshape(img.shape[0]*img.shape[1],3)
#img.shape

#img

clf=KMeans(n_clusters=15)
color_labels=clf.fit_predict(img)
center_colors=clf.cluster_centers_

#color_labels

#center_colors

counts=Counter(color_labels)
#counts

ordered_colors=[center_colors[i] for i in counts.keys()]
hex_colors=[rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
#hex_colors


# plt.pie(counts.values(),labels=hex_colors,colors=hex_colors)



def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)

def x(hex):
  hex1=""
  for i in hex:
    if i!='#':
      hex1+=i

  return hex1
colors=[]
for i in range(len(hex_colors)):
  colors.append(x(hex_colors[i]))


injury=[]
status1=True
for i in colors:
  t=hex_to_rgb(i)
  if ((t[0]==t[1] or t[0]==t[1]+1 or t[0]==t[1]+2 or t[0]==t[1]+3 or t[0]==t[1] or t[0]==t[1]-1 or t[0]==t[1]-2 or t[0]==t[1]-3) and (t[0]==t[2] or t[0]==t[2]+1 or t[0]==t[2]+2 or t[0]==t[2]+3 or t[0]==t[2] or t[0]==t[2]-1 or t[0]==t[2]-2 or t[0]==t[2]-3)):
    status1=status1 and True
  else :
    status1=status1 and False
  injury.append(t)


if status1==True:
  print('Giving result')
else:
  print('Invalid Image!!')

print(injury)