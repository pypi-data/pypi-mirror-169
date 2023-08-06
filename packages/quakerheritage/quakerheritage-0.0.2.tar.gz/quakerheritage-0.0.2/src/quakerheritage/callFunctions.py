import getWebData as gwd
import cleanseData as cd
import tkinter as tk
import csv
from tkinter import filedialog

url = "https://heritage.quaker.org.uk/"
#filepath = 'D:\Documents\Coding\quakerHeritage\quakerHeritageDB.csv'

#query webpage for pdfs, collate data, and hygiene

def getOnlineData(url): 
    pdfList = gwd.getUrls(url)
    dictList = []
    for pdf in pdfList[1:3]: ####remove slice for full Go Live####
        dictList.append(gwd.pdfDataExtract(pdf))
    df = cd.createDataframe(dictList)
    df = cd.hygieneDataframe(df)
    return df
    

if __name__ == '__main__':
    #load data from csv for testing purposes
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory() + '\quakerHeritageDB.csv'
    db = getOnlineData(url)
    cd.saveToCSV(db, file_path)