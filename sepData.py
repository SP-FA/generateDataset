from lib.separateData import SeparateData
import argparse

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=r'E:\Computer\code\Python\machine learning\scientific research\乳腺AI - 副本\3Ddata', help='the path of dataset')
    parser.add_argument('--isDel', type=bool, default=True, help='whether to delete original data')
    parser.add_argument('--sepr', type=list, default=[0.7, 0.3, 0], help='the proportion of train, val, dectect')
    args = parser.parse_args()
    return args

def main(args:argparse.Namespace):
    rootPath = args.path
    dataPath = rootPath + r"\data"
    trainPath = rootPath + r"\train"
    testPath = rootPath + r"\val"
    detectPath = rootPath + r"\detect"

    sd = SeparateData(args.sepr, dataPath)
    sd.randomSep(trainPath, testPath, detectPath, args.isDel)

if __name__ == '__main__':
    args = getArgs()
    main(args)
