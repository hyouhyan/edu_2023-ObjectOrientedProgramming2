import numpy as np
import cv2

img = cv2.imread('google.png')

# opencvの画像データはnumpy.ndarray型として扱われる
print(type(img))
# <class 'numpy.ndarray'>

# 画像サイズを知るにはnumpy.ndarrayのshapeを呼び出す
# rows には640が，colsには1280が代入される
# channelsにはカラーチャンネル数(b,g,r)の3<class 'int'>が代入される
rows,cols,channels = img.shape
print(f"画像の縦{rows}px, 画像の横{cols}px, 画像のカラーチャンネル数{channels}")
# 画像の縦640px, 画像の横1280px, 画像のカラーチャンネル数3


# 例として画像のx,y=640, 140の画素(ピクセル)を指定するとGoogleの３文字目黄色[5, 188, 251]が得られる
# 色の並びは一般的なRGBではなくBGRの順番であることに注意
print(img[140, 640])
# array([  5, 188, 251], dtype=uint8)

# channnelの型はnumpy.ndarray
print(type(img[140,640]))
# <class 'numpy.ndarray'>

# (Step1)色の操作
# 画素から青色を消したい場合は次のように処理する
for y in range(rows):
    for x in range(cols):
        # 横x縦yの画素のカラーを取得(ここでは8bitRGB)
        b, g, r = img[y, x]
        # もし画素が白色だったな何もしない
        if (b, g, r) == (255, 255, 255):
            continue
        img[y, x] = 0, g, r

# 編集した画像を保存する
cv2.imwrite('google_change_color.png', img)


# (Step2)図形の描画
# 矩形（水色の長方形）を描画する
# 矩形の左上(begin_point)と右下(end_point)を(x,y)のタプルで定義
begin_point = (350, 50)
end_point = (begin_point[0]+250, begin_point[1]+200)
# 水色(255,255,0)
cyan = (255,255,0)
# cv2.rectangle以外にもline, circle, ellipse, putTextなどがある
img = cv2.rectangle(img, begin_point, end_point, cyan, thickness=3)

# 編集した画像を保存する
cv2.imwrite('google_with_rectangle.png', img)

# (Step3)画像の一部を切り取る
# 画像の一部を切り出す(begin_pointから250x200)
part_img = img[begin_point[1]:begin_point[1]+200,begin_point[0]:begin_point[0]+250]

# 編集した画像を保存する
cv2.imwrite('google_250x200.png',part_img)


# (Step4)画像を並べる
# 新しい画像領域を生成するには(rows, cols, channel)を指定する
# データの型はnumpy.ndarrayなので結果としては３次元配列が生成される
part_img_rows, part_img_cols, part_img_channels = part_img.shape
new_img = np.zeros((part_img_rows*2, part_img_cols*3, part_img_channels), dtype=np.uint8)
print(new_img.shape)
# (400, 750, 3)

# 領域を指定して画像を上書き
for y in range(2):
    for x in range(3):
        new_img[part_img_rows*y:part_img_rows*(y+1), part_img_cols*x:part_img_cols*(x+1)] = part_img[:,:]

# 編集した画像を保存する
cv2.imwrite('new_img_750x400.png',new_img)

# (Step5)値のコピーではなくアドレスのコピー
# Step3で切り抜いた画像を黒色に塗る
for y in range(part_img_rows):
    for x in range(part_img_cols):
        # 光の３原色なので混ぜると白，色が無いと黒になる
        part_img[y, x] = 0, 0, 0

# part_imgの変更はimgにも反映されている(一部が黒に変わっている)
cv2.imwrite('img_modified.png', img)