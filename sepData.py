from lib.separateData import SeparateData
import argparse

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of cfg.yaml')
    parser.add_argument('--isDel', type=bool, default=True, help='whether to delete original data')
    parser.add_argument('--sepr', type=list, default=[0.7, 0.3, 0], help='the proportion of train, val, dectect')
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

    sd = SeparateData(args.sepr, dataPath)
    sd.randomSep(trainPath, testPath, detectPath, args.isDel)

if __name__ == '__main__':
    args = getArgs()
    main(args)
