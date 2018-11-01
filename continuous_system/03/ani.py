import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ims = []
flag_legend = True#凡例描画のフラグ
#30step分だけsin,cosを少しずつ動かしながら描画する
for i in range(30):
    x = np.arange(-5,5,0.1)
    sin = np.sin(x+i*0.1)
    cos = np.cos(x+i*0.1)
    im1 = plt.plot(x,sin,label="sin_curve",color="red")
    im2 = plt.plot(x,cos,label="cos_curve",color="blue")
    if flag_legend:#一回のみ凡例を描画
        plt.legend()
        flag_legend = False
    ims.append(im1+im2)#グラフを配列に追加

ani = animation.ArtistAnimation(fig, ims, interval=100)#100ms ごとに表示
ani.save("output.html", writer="imagemagick")
