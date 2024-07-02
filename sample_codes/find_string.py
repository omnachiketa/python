import os
'''
this will search the string in a given directory and return the file names
'''
file_names = []
match = []
def list_files(path='.'):
    with os.scandir(path) as entrys:
        for files in entrys:
            if files.is_file():
                file_names.append(files.path)
            else:
                list_files(files.path) 


def find_str(string):
    for file in file_names:
        with open(file, 'r') as f:
            if string in f:
                print("found a match")
                match.append(file)
            else:
                pass


def main():
    print('enter the string you want to sarch in the dir:')
    serch_string = input()
    list_files()
    find_str(serch_string)
    print('we found the match in:'+str(match))

if __name__ =='__main__':
    main()
