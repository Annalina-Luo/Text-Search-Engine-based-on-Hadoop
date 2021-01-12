import os


def rename():
    path = "D:/ebook/"
    file_list = os.listdir(path)
    # print(file_list)
    a = 0
    for i in file_list:
        dir1 = os.path.join(path, i)
        print(i)
        dir2 = os.path.join(path, i.replace(' ', '_'))
        os.rename(dir1, dir2)


rename()
