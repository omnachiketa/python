from genericpath import samefile
import os
'''this will show all the basic file operation'''
def create_file(file_name):
    with open(file_name, 'w') as f:
        res = f.write("demo file")
        print("new file got created")

def read_file(file_name):
    with open(file_name, "r") as f:
        res = f.read()
    return res

def write_file(file_name, string):
    with open(file_name, 'a') as f:
        f.write(string)

def delete_file(file_name):
    os.remove(file_name)

def  main():
    print("createing a file")
    create_file('samplefile')
    output = read_file('samplefile')
    print('this is the file content:\n' + output)
    write_file('samplefile', "\nI have writen this in the file")
    print('Thist is the content of the file after change:\n' + read_file('samplefile'))
    delete_file('samplefile')

if __name__=="__main__": 
    main() 
