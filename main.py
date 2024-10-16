from FileManager import CreateFolders, Upload
from tkinter import Tk
from IternalView import MainVision
from Values import MainValues
from Values import ecology, badThings, round
from NotBaseValues import *
values = MainValues()


if __name__ == "__main__":

    CreateFolders()

    for cou in listOfCountries:
        for i in range(len(listOfCountries)):
            for ci in listOfCountries[i].listOfTowns:
                blowLog[cou.name + ci.name] = 0

    window = Tk()
    window['bg'] = "#f5f5f5"
    window.title("Political Chess")
    window.geometry("450x550")
    window.resizable(width=False, height=False)

    Upload(listOfCountries, ecology, values, round)
    MainVision(window)