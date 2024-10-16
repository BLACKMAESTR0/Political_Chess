from NotBaseValues import *
def ClearLogs():
    global blowLog, listOfCountries, finaleLogExposions
    blowLog = dict()
    for cou in listOfCountries:
        for i in range(len(listOfCountries)):
            for ci in listOfCountries[i].listOfTowns:
                blowLog[cou.name + ci.name] = 0