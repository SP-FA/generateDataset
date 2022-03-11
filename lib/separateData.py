import os
import shutil
import random

class SeparateData:
    def __init__(self, lst: list, dataPath: str):
        '''
        Initialise the class and print the size of train, test, detect set

        PARAMETERS:
          @ lst: Represents the proportion of train, test, detect set
          @ dataPath: The path of the data set
        '''

        # Get the total size of the data set
        fileList = os.listdir(dataPath + r"\images")
        self.tot = len(fileList)
        for f in fileList:
            fileDetail = os.path.splitext(f)
            self.fileName = fileDetail[0][:-3]
            self.fileExte = fileDetail[1]
            break
        self.dataPath = dataPath
        # Get train size, test size and print them
        self.testSize = int(self.tot * lst[1])
        self.detectSize = 0
        # If you need to separate data into detect set
        if len(lst) == 3:
            self.detectSize = int(self.tot * lst[2])

        print("train size: ", self.tot - self.testSize - self.detectSize)
        print("val size: ", self.testSize)
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
            selected = []
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

    def copyData(self, i: int, path: str):
        '''
        There must be two folders under the given path, 'images' and 'labels'
        and this function will copy the images and labels into given folders respectively.

        PARAMETERS:
         @ i: The serial number of the data.
         @ path: Where the data will be copied to.
        '''
        EXT = self.dataPath + "\\images\\" + self.fileName + "(" + str(i) + ")" + self.fileExte
        TXT = self.dataPath + "\\labels\\" + self.fileName + "(" + str(i) + ").txt"
        shutil.copy(EXT, path + r"\images")
        shutil.copy(TXT, path + r"\labels")

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
        txtPath = path + r"\labels"
        os.chdir(jpgPath)
        for data in os.listdir(jpgPath):
            os.remove(data)
        os.chdir(txtPath)
        for data in os.listdir(txtPath):
            os.remove(data)

    def randomSep(self, trainPath: str,
                        testPath: str,
                        detectPath: str="",
                        isDataDelete: bool=False):
        '''
        Separate data set into train, test, detect set, or just train and test set.

        PARAMETERS:
         @ trainPath: The path of train set.
         @ testPath: The path of test set.
         @ detectPath: The path of detect set. Default value detectPath="".
         @ isDataDelete: Whether to delete original data. Default value isDataDelete=False.
        '''
        if isDataDelete:
            self.deleteData(trainPath)
            self.deleteData(testPath)
            self.deleteData(detectPath)

        testList = self.getRandomList(self.testSize)
        detectList = self.getRandomList(self.detectSize, testList)

        for i in testList:
            self.copyData(i, testPath)
        for i in detectList:
            self.copyData(i, detectPath)
        for i in range(0, self.tot):
            if not((i in testList) or (i in detectList)):
                self.copyData(i, trainPath)


if __name__ == "__main__":
    rootPath = r"E:\Computer\code\Python\machine learning\scientific research\ApexCheater"
    dataPath = rootPath + r"\data"
    trainPath = rootPath + r"\train"
    testPath = rootPath + r"\val"
    detectPath = rootPath + r"\detect"

    sd = SeparateData([0.7, 0.3, 0], dataPath)
    sd.randomSep(trainPath, testPath, isDataDelete=True)
    print("finished")