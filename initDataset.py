import os
import yaml
import argparse

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of cfg.yaml')
    parser.add_argument('--nc', type=int, default=0, help='number of classification')
    args = parser.parse_args()
    return args

def generateFolder(path:str, folderName:str) -> None:
    os.chdir(path)
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    os.chdir(path+"\\"+folderName)
    if not os.path.exists("images"):
        os.mkdir("images")
    if not os.path.exists("labels"):
        os.mkdir("labels")
    os.chdir("../")

def generateYaml(args:argparse.Namespace) -> dict:
    dct = {}
    dct["names"] = []
    dct["nc"] = args.nc
    dct["val"] = "./val/images"
    dct["train"] = "./train/images"
    return dct

def main(args:argparse.Namespace):
    fp = open(args.cfgpath, "r", encoding='utf-8')
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    datasetPath = cfg.get('datasetPath', './')

    generateFolder(datasetPath, "data")
    generateFolder(datasetPath, "train")
    generateFolder(datasetPath, "val")
    generateFolder(datasetPath, "detect")

    dataYaml = generateYaml(args)
    with open(args.path+"\\"+"data.yaml", "w", encoding="utf-8") as fp:
        yaml.dump(dataYaml, fp, allow_unicode=True)

if __name__ == "__main__":
    args = getArgs()
    main(args)