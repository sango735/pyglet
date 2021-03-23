from game import *

image_player = image("chicken.png")

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
def start():
  #初期位置にする場合はxとy座標の指定は不要
  add(player, image_player, 0.1)

run(start, 1280, 720)