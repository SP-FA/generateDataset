import argparse
import yaml
from lib.video2Frame import Video2Frame

def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='./cfg.yaml', help='cfg.yaml path')
    parser.add_argument('--interval', type=int, default=10, help='frame interval')
    parser.add_argument('--video', type=list, default=[0, None], help='the begin and end number of the videos')
    parser.add_argument('--genTXT', type=bool, default=False, help='whether to generate the corresponding txt file')
    args = parser.parse_args()
    return args

def main(args):
    fp = open(args.data, "r", encoding='utf-8')
    cfg = fp.read()
    cfg = yaml.safe_load(cfg)
    videoPath = cfg.get('videoPath', './')
    savePath = cfg.get('savePath', './')

    v2f = Video2Frame(videoPath, savePath, args.interval)
    v2f.getFrames(args.video, args.genTXT)

if __name__ == "__main__":
    args = getArgs()
    main(args)