import os
import hashlib

'''
This code is used to find a given string in a file and count the number of times it occored
'''
file_names = []
match = {}
duplicate=[]
def list_files(path='.'):
    with os.scandir(path) as entrys:
        for files in entrys:
            if files.is_file():
                file_names.append(files.path)
            else:
                list_files(files.path) 

def check_hash():
    for file in file_names:
        with open(file, 'br') as f:
            hash_value = hashlib.md5(f.read()).hexdigest()
        if hash_value in match:
            match[hash_value].append(file)
        else:
            match[hash_value] = [file]

def main():
    list_files()
    check_hash()
    for i in match.keys():
        if (len(match[i]) > 1):
            print('These are duplicate files:')
            print(match[i])
        else:
            print('No suplicate files found')
    

        
if __name__=="__main__":
    main()

