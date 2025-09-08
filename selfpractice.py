import os
def process(folder):
        try:
            files = os.listdir(folder)
            return files, None
        except FileNotFoundError:
            return None, "Directory does not exist"
        except PermissionError:
            return None, "Permission denied for Directory"



def main():
    
    folders = input("Enter the folder names seperated by space: ").split()
    if len(folders) < 1:
        print(f"Need atleast one input")
        exit(1)
    for folder in folders:
        files, errormessage = process(folder)
        if files:
            print(f"Contents of {folder}:")
            for file in files:
                print(f"{file}")
        else:
            print(f"{folder} : {errormessage}")
main()
## some changes here
## Branch changes here