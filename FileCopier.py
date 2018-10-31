import pandas as pd
import os
#import io
from csv import writer
import shutil
from datetime import datetime



data=pd.read_table('C:\\99XTBoligMappa\\PythonFileReader\\FileRepo.tsv',header=None)

TotalFileSize=0
run= True
sourcePath ="C:\\99XTBoligMappa\\PythonFileReader\\"
destinationPath = 'C:\\99XTBoligMappa\\PythonFileReader\\CopyDIr\\'
while run:
    for index, row in data.iterrows():
        file = row.get_values()[0]
        currentFile="C:\\99XTBoligMappa\\PythonFileReader\\"+file
        a= datetime.now()
        shutil.copy(currentFile, destinationPath)
        b= datetime.now()
        print(file)
        c=b-a
        duration=c.total_seconds() * 1000 #in miliseconds
        stat = os.stat(currentFile)
        TotalFileSize = TotalFileSize + stat.st_size #total File size
        #finaldata=("file = " + file + " | "+ str(stat.st_size) )
        #print ("file = " + file + " | "+ str(stat.st_size) )
        with open('C:\\99XTBoligMappa\\PythonFileReader\\CopyDIr\\FileRepoNew.csv',"a") as newfile:
            csv_writer = writer(newfile,delimiter=',')
            csv_writer.writerow([file,stat.st_size,duration])# add ,duration
            os.unlink(destinationPath+file) #deleting the copied file. concatination needed
    
        if TotalFileSize >= 20000: #10^12 bytes for a TB
            run = False
            print("1TB copying Complete")
            break


