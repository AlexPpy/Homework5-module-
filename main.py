from functions import*
import platform

if __name__=='__main__':

    i=int(input('''
    Выберите нужное действи:
    0 - создать папку;
    1 - удалить (файл/папку);
    2 - копировать (файл/папку);
    3 - просмотр содержимого рабочей директории;
    4 - посмотреть только папки;
    5 - посмотреть только файлы;
    6 - просмотр информации об операционной системе;
    7 - создатель программы;
    8 - играть в викторину;
    9 - мой банковский счет;
    10 - смена рабочей директории;
    11 - выход.
        '''))
    if i==0:
        create_new()
    elif i==1:
        delete_f()
    elif i ==2:
        copy_f()
    elif i==3:
        print(os.listdir(os.getcwd()))
    elif i==4:
        look_folder()
    elif i==5:
        look_file()
    elif i==6:
        print(platform.platform())
    elif i==7:
        print('Alex')
    elif i==8:
        import Victory
    elif i==9:
        import Wallet
    elif i==10:
        os.chdir(input('Enter path'))
    elif i==11:
        exit()




