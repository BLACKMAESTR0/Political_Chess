from Logs import ClearLogs
from Values import MainValues
from IternalView import MainVision, End
from FileManager import Upload
values = MainValues()
def RoundStart(window):
    global ecology
    global badThings
    global round
    global listOfCountries
    ClearLogs()
    ecology = int(ecology - badThings * ecology * values["ecoDowngrade"])
    for country in listOfCountries:
        country.RoundStart()
    round += 1
    badThings = 0
    Upload()
    if round != values["EndRound"]:
        MainVision(window)
    else:
        End(window)

