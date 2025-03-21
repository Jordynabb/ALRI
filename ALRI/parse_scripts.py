from process_scripts import process
from transcription import Transcription, Transcription_manager
import zipfile
import os
import sys

#usage: python parse_scripts.py folder path
# e.g python parse_scripts.py "C:/Users/YourName/Documents/Transcriptions"

folder_path = sys.argv[1] 
print("folder_path: ", folder_path)
pos = 1

collection = Transcription_manager()

def parse(folder_path):
    
    global pos
    if not os.path.exists(folder_path):
     return -1   

    for file_name in os.listdir(folder_path):

        file = Transcription()

        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            print(f"Skipping non-file: {file_path}")
            continue

        if os.path.getsize(file_path) == 0:
            print(f"Skipping empty file: {file_path}")
            continue

        if not file_name.endswith(".docx"):
            print(f"Skipping unsupported file type: {file_path}")
            continue


        print(f"Processing file {pos}: {file_name} \n")
        print("file ID: ",file.ID) #Degug statement
        print("---------------------------------------- \n")
        process(file_path, file, collection) #TEST THIS
        pos += 1

    print("Reached end of folder. Terminating.")

    

parse(folder_path)
collection.print_all

