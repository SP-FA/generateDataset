from lib.separateData import SeparateData
import argparse

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./', help='the path of data')
    parser.add_argument('--name', type=str, help='the name of data file')
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

    sd = SeparateData([0.7, 0.3, 0], dataPath)
    sd.randomSep(trainPath, testPath, detectPath, args.name, args.isDel)

if __name__ == '__main__':
    args = getArgs()
    main(args)
