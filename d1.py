import os   
import shutil

def MoveAndSort(source,dest):
    if os.path.isdir(dest) == False:
        os.makedirs(dest)
    shutil.move(source,dest)

def getEntries(res,target_path):
    for r in res:
        full_path = os.path.join(target_path,r)
        if '.doc' in r:
            MoveAndSort(full_path,os.path.join(target_path,'Documents'))
        if '.exe' in r or '.msi' in r:
            MoveAndSort(full_path,os.path.join(target_path,'Installers'))
        if '.zip' in r:
            MoveAndSort(full_path,os.path.join(target_path,'Zip_Files'))
        if '.txt' in r:
            MoveAndSort(full_path,os.path.join(target_path,'Text_Files'))
        if '.pdf' in r:
            MoveAndSort(full_path,os.path.join(target_path,'PDFs'))
        if '.jpg' in r or '.png' in r:
            MoveAndSort(full_path,os.path.join(target_path,'Pictures'))

if __name__ == '__main__':

    target_path = input()
    res = os.listdir(target_path)

    getEntries(res,target_path)
