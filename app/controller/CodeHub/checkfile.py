import sys
import os

def thePath():
    return sys.path


def openFileList():
    file_list = []
    for file_name in os.listdir(r'/var/www/html/codehub/'):
        file_list.append(file_name)
    return file_list


def saveFile(data):
    path = os.path.join('/var/www/html', data.name)
    with open(path, 'wb+') as destination:
        destination.writable(data)


def getFileContent(filename):
    with open('/var/www/html/codehub/'+filename,'r') as reader:
        return reader.read()




if __name__ == '__main__':
    print()