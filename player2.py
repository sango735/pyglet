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

def start():
  #初期位置にする場合はxとy座標の指定は不要
  add(player, image_player, 0.1)

run(start, 1280, 720)