# generate dataset

![head](pic\head.png)

<br>

## 01. 文件说明

`getImages.py` 用于将视频批量转换成图片，并且可以生成对应的 txt 文件以方便制作数据集。

`initDataset.py` 用于初始化数据集所需要的文件夹和配置文件，目前仅支持 yolov5，yolov7

`sepData.py` 用于数据分割，将数据随机按比例分到各文件夹，同样目前仅支持 yolov5，yolov7

### 如何使用

首先我们需要填写一个配置文件，然后在运行上面的 python 文件时将配置文件路径作为参数传入，并添加其它需要的参数即可。

<br>

## 02. 配置文件

配置文件是一个 `.yaml` 文件，可以写入以下参数：

1. `videoPath`: 视频文件夹的路径
2. `savePath`: 视频保存路径
3. `datasetPath`: 数据集的路径，用于创建数据集和数据分割
4. `yoloPath`: yolo 的路径，现阶段仅支持 yolo
5. `nc`: 分为几类 (yolo)
6. `names`: 每一类的名字，list (yolo)
7. `model`: 模型名，可选 yolov5, yolov7, other

<br>

## 03. 参数

### getImages.py

1. `--cfgpath`: 配置文件的路径，str
2. `--interval`: 每隔几帧取一次图片，int
3. `--video`: 从第几个视频到第几个视频进行转换，list
4. `--genTXT`: 是否生成对应的 txt 文件，bool
5. `--limit`: 每个视频生成的图片数量，int

### sepData.py

1. `--cfgpath`
2. `--isDel`: 是否删除文件夹内已有的文件，bool
3. `--sepr`: 数据分割的比例，list 内有三个元素，分别表示 `train`, `test`, `detect` 的比例，小于 1，可以为 0，list


### initDataset.py

1. `--cfgpath`
