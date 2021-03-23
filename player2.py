from game import *

image_player = image("chicken.png")

def player(p):
  #移動速度を設定
  v = 0.01

  if key(LEFT):
    p.x -= v
  
  if key(RIGHT):
    p.x += v

  if key(UP):
    p.y += v

  if key(DOWN):
    p.y -= v
    