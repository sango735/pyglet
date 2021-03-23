#ゲーム機能の読み込み
from game import *

#画像の読み込み
image_player = image('chicken.png')

#キャラクターの関数定義と引数の受け渡し
def player(p):
    #横軸・縦軸の移動の向きを設定
    p.x += p.vx
    p.y += p.vy


def start():
    #add関数でキャラクターと画像の呼び出し、サイズ、座標指定、移動速度の設定
    add(player, image_player, 0.1, 1.1, 0, -0.01, 0)

#上記の呼び出しと、キャンバスの解像度を設定
run(start, 1280, 720)
