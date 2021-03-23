#ゲーム機能の読み込み
from game import *

#画像の読み込み
image_player = image('chicken.png')

def player(p):
    p.x += p.vx
    p.y += p.vy

def start():
    add(player, image_player, 0.1, 1.1, 0, -0.01, 0)

run(start, 1280, 720)
