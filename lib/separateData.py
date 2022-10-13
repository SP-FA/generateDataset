import os
import shutil
import random


class SeparateData:
    def __init__(self, lst: list, model: str, datasetPath: str):
        '''
        Initialise the class and print the size of train, test, detect set

        PARAMETERS:
          @ lst: Represents the proportion of train, test, detect set
          @ dataPath: The path of the data set
          @ haveLabel: The label.txt file for each pic
        '''
        self.model = model
        if model == 'other':
            labelPath = datasetPath+"\\data\\label.txt"
            fp = open(labelPath, 'r')
            labelList = fp.readlines()
            self.labelDict = []
            for i in labelList:
                j = i.strip().split(" ")
                seq = ""
                for k in j[1:]:
                    seq = seq + k + " "
                self.labelDict.append(seq)
            fp.close()

        # Get the total size of the data set
        fileList = os.listdir(datasetPath + "//data//images")
        self.tot = len(fileList)
        fileDetail = os.path.splitext(fileList[0])
        self.fileName = fileDetail[0][:-3]
        self.fileExte = fileDetail[1]

        self.datasetPath = datasetPath
        # Get train size, test size and print them
        self.valSize = int(self.tot * lst[1])
        self.detectSize = 0
        # If you need to separate data into detect set
        if len(lst) == 3:
            self.detectSize = int(self.tot * lst[2])

        print("train size: ", self.tot - self.valSize - self.detectSize)
        print("val size: ", self.valSize)
        print("detect size: ", self.detectSize)


    def getRandomList(self, num: int, selected=None) -> list:
        '''
        This function is used to choose some data randomly.

        PARAMETERS:
         @ num: The number of the elements of list.
         @ selected: A list represents previously selected data. Default value selected=[]

        RETURN:
         Return a list represents the serial number of the data, randomly.
        '''
        if selected is None:
            lst = random.sample(range(0, self.tot-1),num)
            return lst
        lst = []
        for i in range(0, num):
            # Loops until r is not in lst and selected. That means r
            # was never chosen in this for loop or previous program.
            while True:
                r = random.randint(0, self.tot - 1)
                if not((r in lst) or (r in selected)):
                    lst.append(r)
                    break
        return lst


    def copyData(self, lst, path: list, isDataDelete: bool):
        '''
        There must be two folders under the given path, 'images' and 'labels'
        and this function will copy the images and labels into given folders respectively.

        PARAMETERS:
         @ lst: The serial number of the data.
         @ path: Where the data will be copied to.
         @ isDataDelete: Whether to delete original data. Default value isDataDelete=False.
        '''
        if self.model == 'yolov5' or self.model == 'yolov7':
            for i in lst:
                name = self.fileName + "(" + str(i) + ")"
                IMG = self.datasetPath + "\\data\\images\\" + name + self.fileExte
                TXT = self.datasetPath + "\\data\\labels\\" + name + ".txt"
                shutil.copy(IMG, path[0])
                shutil.copy(TXT, path[1])
        else:
            fp = open(path[1] + "\\label.txt", 'w' if isDataDelete == True else 'a')
            seqList = []
            for i in lst:
                name = "(" + str(i) + ")" + self.fileExte
                seq = name + " " + self.labelDict[i] + "\n"
                seqList.append(seq)
                IMG = self.datasetPath + "\\data\\images\\" + self.fileName + name
                shutil.copy(IMG, path[0])
            fp.writelines(seqList)
            fp.close()


    def deleteData(self, path: list):
        '''
        Delete the data under the given path.
        There must be two folders under the given path, 'images' and 'labels'.
        '''
        os.chdir(path[0])
        for data in os.listdir(path[0]):
            os.remove(data)
        os.chdir(path[1])
        for data in os.listdir(path[1]):
            os.remove(data)


    def randomSep(self, isDataDelete: bool):
        '''
        Separate data set into train, test, detect set, or just train and test set.

        PARAMETERS:
         @ isDataDelete: Whether to delete original data. Default value isDataDelete=False.
        '''
        trainPath = []
        valPath = []
        detectPath = []
        if self.model == 'yolov5' or self.model == 'other':
            trainPath = [self.datasetPath+"\\train\\images", self.datasetPath+"\\train\\labels"]
            valPath = [self.datasetPath+"\\val\\images", self.datasetPath+"\\val\\labels"]
            detectPath = [self.datasetPath+"\\detect\\images", self.datasetPath+"\\detect\\labels"]
        elif self.model == 'yolov7':
            trainPath = [self.datasetPath+"\\images\\train", self.datasetPath+"\\labels\\train"]
            valPath = [self.datasetPath+"\\images\\val", self.datasetPath+"\\labels\\val"]
            detectPath = [self.datasetPath+"\\images\\detect", self.datasetPath+"\\labels\\detect"]

        if isDataDelete:
            self.deleteData(trainPath)
            self.deleteData(valPath)
            if self.detectSize != 0:
                self.deleteData(detectPath)

        valList = self.getRandomList(self.valSize)
        detectList = self.getRandomList(self.detectSize, valList)
        trainList = []
        for i in range(0, self.tot):
            if not((i in valList) or (i in detectList)):
                trainList.append(i)

        self.copyData(valList, valPath, isDataDelete)
        if self.detectSize != 0:
            self.copyData(detectList, detectPath, isDataDelete)
        self.copyData(trainList, trainPath, isDataDelete)


if __name__ == "__main__":
    rootPath = r"H:\ABM\data"

    sd = SeparateData([0.7, 0.3, 0], 'yolov5', rootPath)
    sd.randomSep(isDataDelete=True)
    print("finished")
