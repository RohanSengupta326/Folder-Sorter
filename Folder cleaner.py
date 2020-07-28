import  os
import shutil


files = os.listdir('C:\\Users\\ranapc\\Downloads\\Folder cleaner Python') # in python 3 dont need to mention path

files.remove('main.py')
#print files
 
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def move(foldername, files):
    for file in files:
        shutil.move(file, '{foldername}\{file}'.format(foldername=foldername, file=file))


createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Videos')
createIfNotExist('Others')

imgext = ['.png', '.jpg', '.jpeg']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgext ]
move("Images", images)

#print images

docext = ['.pdf', '.docx', '.doc', '.txt']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docext ]
#print docs
move("Docs", docs)

medext = ['.mp4', '.mp3', '.flv']
media = [file for file in files if os.path.splitext(file)[1].lower() in medext]
#print media
move("Videos", media)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgext) and (ext not in docext) and (ext not in medext) and os.path.isfile(file):
        others.append(file)
move("Others", others)



