from game import *

from crash import *

import math
import random

image_player = image("chicken.png")
image_enemy = image("car.png")

sw,sh =1,9/16

def player(p):
  #移動速度を設定
  v = 0.05

  if key(LEFT):
    p.x -= v
  
  if key(RIGHT):
    p.x += v

  if key(UP):
    p.y += v

  if key(DOWN):
    p.y -= v

  #画面外にはみ出さないように設定
  #横幅とキャラクターの差分を計算し、移動範囲を制限する
  #今いる位置と画面端までの距離を計算して反映させている
  #キャラクターのp.sx,syを引かなかったら半分だけ隠れる
  p.x =max(-sw+p.sx,min(sw-p.sx,p.x))
  p.y =max(-sh+p.sy,min(sh-p.sy,p.y))

  for e in group(enemy):
    if math.dist((p.x, p.y),(e.x, e.y)) < (p.sx + e.sx)*0.5:
      new_crash(p.x,p.y,0.01,20,0.98)

      p.life=0

def enemy(e):
  e.x += e.vx
  e.r= math.sin(e.time*0.2)*0.01
  e.time +=1
  if abs(e.x) > sw+e.sx:
    e.life=0

def stage(s):
  if random.random() < 0.05:
    size=0.1
    side = random.choice([-1,1])
    y=random.uniform(-sh+size,sh-size)

    add(enemy,image_enemy,size,(sw+size)*side,y,-0.01*side)

def start():
  #初期位置にする場合はxとy座標の指定は不要
  add(stage)
  add(player, image_player, 0.1)

run(start, 1280, 720)