import os
import yaml
import argparse

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./', help='where to build the dataset')
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
    generateFolder(args.path, "data")
    generateFolder(args.path, "train")
    generateFolder(args.path, "val")
    generateFolder(args.path, "detect")

    dataYaml = generateYaml(args)
    with open(args.path+"\\"+"data.yaml", "w", encoding="utf-8") as fp:
        yaml.dump(dataYaml, fp, allow_unicode=True)

if __name__ == "__main__":
    args = getArgs()
    main(args)