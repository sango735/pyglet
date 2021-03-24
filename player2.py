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

  #出現する車の繰り返し処理を行う
  #同様に１体１体に衝突判定をつける
  for e in group(enemy):
    #距離を使った判定を行う為,math(数学).dist(距離、distance)関数を使う
    #座標pと座標eの距離を求めて返し、右記の合計サイズよりも小さければ当たり判定を行う
    if math.dist((p.x, p.y),(e.x, e.y)) < (p.sx + e.sx)*0.5:
      #衝突した時のエフェクトを発生させる
      new_crash(p.x,p.y,0.01,20,0.98)
      p.life=0

def enemy(e):
  e.x += e.vx
  #sin関数を使って振動の周波数と振り幅を設定する
  e.r= math.sin(e.time*0.2)*0.01
  #時間を加算していく（車が動く）事で上記の振動を発生させる
  e.time +=1
  #車が画面端に行った時に、その車を消去する条件式を設ける
  if abs(e.x) > sw+e.sx:
    e.life=0

def stage(s):
  #ランダム関数（0以上1未満の乱数を返す）を使って5%の確率で処理する条件式
  if random.random() < 0.05:
    size=0.1
    #車が出現するX座標を設定したどちらかランダムの値で設定する
    side = random.choice([-1,1])
    #車が出現するY座標の制限を決める。
    #ランダムユニフォームは指定値の間の乱数を返す
    y=random.uniform(-sh+size,sh-size)
    
    add(enemy,image_enemy,size,(sw+size)*side,y,-0.01*side)

def start():
  #初期位置にする場合はxとy座標の指定は不要
  add(stage)
  add(player, image_player, 0.1)

run(start, 1280, 720)