from lib.separateData import SeparateData
import argparse
import yaml


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of dataset')
    parser.add_argument('--isDel', type=int, default=1, help='whether to delete original data')
    parser.add_argument('--sepr', default=[0.7, 0.3, 0], nargs='+', type=float, help='the proportion of train, val, dectect')
    parser.add_argument('--haveLabel', type=int, default=1, help='set 1 if the dataset have label as a .txt file')
    args = parser.parse_args()
    return args


def main(args:argparse.Namespace):
    fp = open(args.cfgpath, "r", encoding="utf-8")
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    rootPath = cfg.get('datasetPath', './')

    dataPath = rootPath + r"\data"
    trainPath = rootPath + r"\train"
    testPath = rootPath + r"\val"
    detectPath = rootPath + r"\detect"

    haveLabel = True if args.haveLabel==1 else False
    isDel = True if args.isDel==1 else False

    sd = SeparateData(args.sepr, dataPath, haveLabel)
    sd.randomSep(trainPath, testPath, detectPath, isDel)


if __name__ == '__main__':
    args = getArgs()
    main(args)
