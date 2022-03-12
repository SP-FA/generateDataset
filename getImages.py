import argparse
import yaml
from lib.video2Frame import Video2Frame


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfgpath', type=str, default='./cfg.yaml', help='the path of cfg.yaml')
    parser.add_argument('--interval', type=int, default=10, help='frame interval')
    parser.add_argument('--video', type=list, default=None, help='the begin and end number of the videos')
    parser.add_argument('--genTXT', type=bool, default=False, help='whether to generate the corresponding txt file')
    parser.add_argument('--limit', type=int, default=None, help='the limit of each video')
    args = parser.parse_args()
    return args


def main(args):
    fp = open(args.cfgpath, "r", encoding='utf-8')
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    videoPath = cfg.get('videoPath', './')
    savePath = cfg.get('savePath', './')

    names = cfg.get('names', [])

    v2f = Video2Frame(videoPath, savePath, args.interval)
    v2f.getFrames(args.video, args.genTXT, args.limit, names)
    fp.close()


if __name__ == "__main__":
    args = getArgs()
    main(args)
