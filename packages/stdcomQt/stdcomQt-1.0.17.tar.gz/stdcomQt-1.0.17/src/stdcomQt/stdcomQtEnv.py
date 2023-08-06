import os, sys


def stdcomQtInsertPath(file : str = None) :
    """
    sets the current enviroment of a file or self to path
    :param file:
    :return:
    """

    if file is None :
        file = __file__

    dirPath = os.path.dirname(os.path.abspath(file))

    print('Absolute path of file:     ',
        os.path.abspath(file))
    print('Absolute directoryname: ',
        dirPath)

    if dirPath not in sys.path :
        sys.path.append(dirPath)
        print("Inserted: ", dirPath, "Now Is: ",sys.path)



if __name__ == '__main__':
    stdcomQtInsertPath()
