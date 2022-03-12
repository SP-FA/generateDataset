import os


class CreateTXT:
    def __init__(self, path:str):
        self.path = path
        files = os.listdir(path)
        dct = {}
        self.images = []
        for file in files:
            file = os.path.splitext(file)
            dct[file[0]] = dct.get(file[0], 0) + 1

        for i in dct.keys():
            if dct[i] == 1:
                self.images.append(i)

    def generateTXT(self) -> None:
        for image in self.images:
            fp = open(self.path + "\\" + image + ".txt", 'w')
            fp.close()

    def genClasses(self, names:list) -> None:
        fp = open(self.path + "\\classes.txt", 'w')
        for i in names:
            fp.write(i + "\n")
        fp.close()


if __name__ == "__main__":
    path = ""
    a = CreateTXT(path)
    a.generateTXT()