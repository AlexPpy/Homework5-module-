import os
import shutil


def create_new():  #создаем папку
    Q='y'
    while Q=='y':
        i=input('Input name for new')
        if not os.path.exists(i):
            os.mkdir(i)
        else:
            Q=input('File with this name exists - wuold you like to input other name?(y/n)')

    return 0

def copy_f():     #функция копирования дирикторий и файлов
    q = 'y'
    while q == 'y':    #открываем цикл чтобы при необходимости копирования нескольких дирикторий или файлов
        i = input('Input name of folder or file to copy') #принимаем имя файла
        if os.path.exists(i): #Проверяем наличие файла/папки
            if os.path.isfile(i): #определяем что будем копировать файл
                n=i.split('.')   #определяем гденачинается разширение файла
                c=n[0]+'_copy.'+n[1] #пишем имя для копии
                shutil.copy(i, c) # создаем копию
                break
            else:
                new_name=i+'_copy' #создаем имя для новой папки
                shutil.copytree(i, new_name) # создаем копию
                break
        else:
            q = input(f'File {i} not found, would you like to enter new name?(y/n)')
        if q!='y':
            break
    return 0



def delete_f(): #удаление файлов/папок
    q='y'
    while q=='y':  #открываем цикл чтобы при необходимости удаоения нескольких дирикторий или файлов
        i=input('Input name of folder or file to delete') #принимаем имя файла
        if os.path.exists(i):  # Проверяем наличие файла
            if os.path.isfile(i):#определяем что будем удалять файл
                os.remove(i) #удаляем фаил
                q=input('would you like to delete another file or folder?(y/n)')
            else:
                os.rmdir(i) #удаляем дирикторию
                q = input('would you like to delete another file or folder?(y/n)')
        else:
            q = input(f'File {i} not found, would you like to enter new name?(y/n)')
            #если не нашелся фаил или папка предлагаем снова ввести имя
        if q!='y':
            break
    return 0

print(os.getcwd())

def look_file():
    file_list=[]
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(),file)):
            file_list.append(file)
    print(file_list)
    return

def look_folder():
    folder_list=[]
    for folder in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), folder)):
            folder_list.append(folder)
    print(folder_list)
    return