import os
import shutil
import random


class SeparateData:
    def __init__(self, lst: list, dataPath: str, haveLabel: bool=False):
        '''
        Initialise the class and print the size of train, test, detect set

        PARAMETERS:
          @ lst: Represents the proportion of train, test, detect set
          @ dataPath: The path of the data set
          @ haveLabel: The label.txt file for each pic
        '''
        self.haveLabel = haveLabel

        if haveLabel == False:
            labelPath = r"H:\ABM\data\label.txt"
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
        fileList = os.listdir(dataPath + r"\images")
        self.tot = len(fileList)
        fileDetail = os.path.splitext(fileList[0])
        self.fileName = fileDetail[0][:-3]
        self.fileExte = fileDetail[1]

        self.dataPath = dataPath
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


    # def copyData(self, i: int, path: str):
    def copyData(self, lst, path:str, isDataDelete: bool):
        '''
        There must be two folders under the given path, 'images' and 'labels'
        and this function will copy the images and labels into given folders respectively.

        PARAMETERS:
         @ i: The serial number of the data.
         @ path: Where the data will be copied to.
        '''

        if self.haveLabel == True:
            for i in lst:
                EXT = self.dataPath + "\\images\\" + self.fileName + "(" + str(i) + ")" + self.fileExte
                TXT = self.dataPath + "\\labels\\" + self.fileName + "(" + str(i) + ").txt"
                shutil.copy(EXT, path + r"\images")
                shutil.copy(TXT, path + r"\labels")
        else:
            fp = None
            if isDataDelete == True:
                fp = open(path + "\\labels\\label.txt", 'w')
            else:
                fp = open(path + "\\labels\\label.txt", 'a')
            seqList = []
            for i in lst:
                name = "(" + str(i) + ")" + self.fileExte
                seq = name + " " + self.labelDict[i] + "\n"
                seqList.append(seq)
                EXT = self.dataPath + "\\images\\" + self.fileName + name
                shutil.copy(EXT, path + r"\images")
            fp.writelines(seqList)
            fp.close()


    def deleteData(self, path: str):
        '''
        Delete the data under the given path.
        There must be two folders under the given path, 'images' and 'labels'.

        PARAMETER:
         @ path: The path you want to delete data under it.
        '''
        if path == "":
            return

        jpgPath = path + r"\images"
        os.chdir(jpgPath)
        for data in os.listdir(jpgPath):
            os.remove(data)

        if self.haveLabel == True:
            txtPath = path + r"\labels"
            os.chdir(txtPath)
            for data in os.listdir(txtPath):
                os.remove(data)


    def randomSep(self, trainPath:str,
                        valPath:str,
                        detectPath:str,
                        isDataDelete:bool):
        '''
        Separate data set into train, test, detect set, or just train and test set.

        PARAMETERS:
         @ trainPath: The path of train set.
         @ valPath: The path of test set.
         @ detectPath: The path of detect set. Default value detectPath="".
         @ isDataDelete: Whether to delete original data. Default value isDataDelete=False.
        '''
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
    dataPath = rootPath + r"\data"
    trainPath = rootPath + r"\train"
    valPath = rootPath + r"\val"
    detectPath = rootPath + r"\detect"

    sd = SeparateData([0.7, 0.3, 0], dataPath)
    sd.randomSep(trainPath, valPath, detectPath, isDataDelete=True)
    print("finished")
