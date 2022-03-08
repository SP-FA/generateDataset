# generate dataset

---

## 01. 说明

`getImages.py` 用于将视频批量转换成图片，并且可以生成对应的 txt 文件以方便制作数据集。

`initDataset.py` 用于初始化数据集所需要的文件夹和配置文件，目前仅支持 Yolov5

`sepData.py` 用于数据分割，将数据随机按比例分到各文件夹，同样目前仅支持 Yolov5

## 02. 参数

1. `--data`: 配置文件的路径，str
2. `--interval`: 每隔几帧取一次图片，int
3. `--video`: 从第几个视频到第几个视频进行转换，list
4. `--genTXT`: 是否生成对应的 txt 文件，bool

## 03. 配置文件

配置文件是一个 `.yaml` 文件，可以写入一下两个参数：

1. `videoPath`: 视频文件夹的路径
2. `savePath`: 视频保存路径

## 04. 可使用的方法

`Video2Frame` 类里包含了三个方法：

1. `getVideoList()->list`: 获取 videoPath 下的视频列表
2. `getFrames(args:list, genTXT:bool)->None`: 将 args 区间内的视频转换成图片（从 0 开始）
3. `getFrameFromVideo(i:int, genTXT:bool, lmt:int)->None`: 将第 i 个视频转换成图片（从 0 开始）

`CreateTXT` 类：

`generateTXT()->None`: 对于给定路径下没有对应 txt 文件的图片，生成对应的 txt 文件