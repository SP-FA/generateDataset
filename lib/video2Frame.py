import os
import cv2
from .createTXT import CreateTXT

class Video2Frame:
    def __init__(self, videoPath:str, savePath:str='./', timeInterval:int=1):
        '''
        初始化，获取 videoPath 下的所有视频

        PARAMETERS:
         @ videoPath: 视频的存放路径
         @ framesSavePath: 视频切分成帧之后图片的保存路径
         @ timeInterval: 保存间隔
        '''
        self.videoPath = videoPath
        self.savePath = savePath
        self.timeInterval = timeInterval
        self.videos = os.listdir(videoPath)
        self.length = len(self.videos)

    def getVideoList(self) -> list:
        return self.videos

    def getFrames(self, args:list=[0, None], genTXT:bool=False) -> None:
        '''
        对每个视频创建文件夹，保存 frame
        PARAMETER:
         @ args: 从第几个视频开始，到第几个结束 (不包括)，负数表示倒数第几
         @ genTXT: 是否生成对应的 txt 文件
        '''
        begin = args[0]
        end   = args[1]
        
        if end == None:
            end = self.length - 1
        begin = begin % self.length
        end = end % self.length + 1
        for i in range(begin, end):
            self.getFrameFromVideo(i, genTXT)

    def getFrameFromVideo(self, i:int=0, genTXT:bool=False, lmt:int=None) -> None:
        '''
        对某个视频创建文件夹，保存 frame
        PARAMETER:
         @ i: 第i个视频，负数表示倒数第几
         @ genTXT: 是否生成对应的 txt 文件
         @ lmt: 设置上限，在第几帧结束
        '''
        i = i % self.length
        video = self.videos[i]
        folderName = os.path.splitext(video)[0]
        os.chdir(self.savePath)
        if not os.path.exists(folderName):
            os.mkdir(folderName)

        vidCap = cv2.VideoCapture(self.videoPath + "\\" + video)
        success, image = vidCap.read()
        cnt = 0
        while success:
            success, image = vidCap.read()
            cnt += 1
            if cnt % self.timeInterval == 0:
                cv2.imencode('.jpg', image)[1].tofile(self.savePath + "\\" + folderName + r"\frame%d.jpg" % cnt)
            if lmt != None:
                if cnt == lmt:
                    break
        print(folderName + ": ", cnt // self.timeInterval, "images")

        if genTXT == True:
            crtTXT = CreateTXT(self.savePath + "\\" + folderName)
            crtTXT.generateTXT()



if __name__ == "__main__":
    videos_path = ""
    frames_save_path = ""
    time_interval = 10
    v2f = Video2Frame(videos_path, frames_save_path, time_interval)
    v2f.getFrameFromVideos()