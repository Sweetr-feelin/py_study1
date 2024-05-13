import os.path

def cat_n_files_task2(main_root):
    for root, dirs, files in os.walk(main_root):
        if dirs == []:
            for f in files:
                file_root = str(main_root + '/' + f)
                os.remove(file_root)
            os.rmdir(main_root)
            return print('Success')
        else:
            return print('Fail')

cat_n_files_task2('example2')
