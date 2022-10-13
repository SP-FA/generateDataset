from lib.separateData import SeparateData
import argparse
import yaml


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of dataset')
    parser.add_argument('--isDel', type=int, default=1, help='whether to delete original data')
    parser.add_argument('--sepr', default=[0.7, 0.3, 0], nargs='+', type=float, help='the proportion of train, val, dectect')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = getArgs()
    fp = open(args.cfgpath, "r", encoding="utf-8")
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    rootPath = cfg.get('datasetPath', './')
    model = cfg.get('model', 'other')
    isDel = True if args.isDel==1 else False

    sd = SeparateData(args.sepr, model, rootPath)
    sd.randomSep(isDel)
