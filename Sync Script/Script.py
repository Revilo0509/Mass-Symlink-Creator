import os
import shutil
import subprocess
from operator import length_hint

def read(file_path):
    """Read a file and clean each line by removing double quotes and newline characters from the start and end."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip().strip('"').strip('\n') for line in file]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

def createcommandfolders():
    SourcesCount = length_hint(Sources)
    for i in range(length_hint(Sources)):
        for i in range(length_hint(Folders)):
            Source_Path = ''.join(Sources[SourcesCount - 1]) + '\\' + str(Folders[i])
            Destination_Path = ''.join(Destination) + '\\' + str(Folders[i])
            if os.path.exists(Source_Path):
                try:
                    shutil.rmtree(Source_Path)
                except OSError as e:
                    print(f"An error occurred: {e}")
                pass
            try:
                subprocess.run(['mklink', '/D', Source_Path, Destination_Path], shell=True)
            except Exception as e:
                print(f"An error occurred: {e}")
        SourcesCount -= 1

def createcommandfiles():
    SourcesCount = length_hint(Sources)
    for i in range(length_hint(Sources)):
        for i in range(length_hint(Files)):
            Source_Path = ''.join(Sources[SourcesCount - 1]) + '\\' + str(Files[i])
            Destination_Path = ''.join(Destination) + '\\' + str(Files[i])
            if os.path.exists(Source_Path):
                try:
                    os.remove(Source_Path)
                except OSError as e:
                    print(f"An error occurred: {e}")
                pass
            try:
                subprocess.run(['mklink', Source_Path, Destination_Path], shell=True)
            except Exception as e:
                print(f"An error occurred: {e}")
        SourcesCount -= 1


Folders = read("Folders.txt")
Files = read("Files.txt")
Sources = read("Sources.txt")
Destination = read("Destination.txt")

createcommandfolders()
createcommandfiles()

