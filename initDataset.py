import os
import yaml
import argparse


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of cfg.yaml')
    args = parser.parse_args()
    return args


def generateFolder(model, path:str, folderName:str) -> None:
    if folderName == 'data' or model == 'yolov5' or model == 'other':
        os.chdir(path)
        if not os.path.exists(folderName):
            os.mkdir(folderName)
        os.chdir(path+"\\"+folderName)
        if not os.path.exists("images"):
            os.mkdir("images")
        if not os.path.exists("labels"):
            os.mkdir("labels")

    elif model == 'yolov7' and folderName != 'data':
        os.chdir(path)
        if not os.path.exists("images"):
            os.mkdir("images")
        if not os.path.exists("labels"):
            os.mkdir("labels")
        os.chdir(path+"\\images")
        if not os.path.exists(folderName):
            os.mkdir(folderName)
        os.chdir(path+"\\labels")
        if not os.path.exists(folderName):
            os.mkdir(folderName)


def generateYaml(yoloPath:str, datasetPath:str, nc:int, names:list) -> dict:
    dct = {}
    dct["names"] = names
    dct["nc"] = nc
    dct["val"] = os.path.relpath(datasetPath, yoloPath)+r"\images\val"
    dct["train"] = os.path.relpath(datasetPath, yoloPath)+r"\images\train"
    return dct


if __name__ == "__main__":
    model = ['yolov5', 'yolov7', 'other']
    args = getArgs()

    fp = open(args.cfgpath, "r", encoding='utf-8')
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    datasetPath = cfg.get('datasetPath', './')
    yoloPath = cfg.get('yoloPath', './')
    nc = cfg.get('nc', 0)
    names = cfg.get('names', [])
    thisModel = cfg.get('model', 'other')
    if thisModel not in model:
        thisModel = 'other'

    generateFolder(thisModel, datasetPath, "data")
    generateFolder(thisModel, datasetPath, "train")
    generateFolder(thisModel, datasetPath, "val")
    generateFolder(thisModel, datasetPath, "detect")

    dataYaml = generateYaml(yoloPath, datasetPath, nc, names)
    with open(datasetPath+"\\"+"data.yaml", "w", encoding="utf-8") as fp:
        yaml.dump(dataYaml, fp, allow_unicode=True)
