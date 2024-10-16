import Values
from Values import ecology, badThings, round
import random
from YesNo import YesNo
values = Values.MainValues()
listOfCountries = [0 for _ in range(values["amountOfCountries"])]

class City:
    def __init__(self, name):
        self.name = name
        self.existance = values["begExistance"]
        self.lifeQual = values["begLifeQual"]
        self.development = values["begDevelopment"]
        self.profit = values["begProfit"]
        self.shield = values["begShield"]
        self.bombComing = values["begBombComing"]
        self.improved = values["begImproved"]
        self.PVO = values["begPVO"]

    def improve(self):
        if self.improved:
            self.lifeQual += values["cityUpdateQual"]
            self.profit += values["cityUpdateProfit"]
            self.development += values["cityUpdateDevelopment"]
            self.improved = False

    def SetImprove(self):
        self.improved = True

    def BombsDown(self):
        global badThings
        currbadThings = 0
        for i in range(self.bombComing):
            if self.PVO:
                ran = random.randint(0, 99)
                if ran > values["PVOChance"]:
                    if self.shield:
                        currbadThings += 2
                        self.shield = False
                    else:
                        currbadThings += 4
                        self.existance = False
                else:
                    currbadThings += 2
                    self.PVO = False
            else:
                if self.shield:
                    currbadThings += 2
                    self.shield = False
                else:
                    currbadThings += 4
                    self.existance = False
        self.bombComing = 0
        badThings += currbadThings

class Country:
    global listOfCountries, blowLog, finaleLogExposions
    def __init__(self, nameCountry, nameFirstCity, nameSecondCity, nameThirdCity, nameFourthCity):
        self.name = nameCountry
        self.avgLifeQual = values["begAvgLifeQual"]
        self.bombAmountNow = values["begBombAmountNow"]
        self.bombAmountComing = values["begBombAmountComing"]
        self.budget = values["begBudget"]
        self.tech = values["begTech"]
        self.payout = values["begPayout"]
        self.firstCity = City(nameFirstCity)
        self.secondCity = City(nameSecondCity)
        self.thirdCity = City(nameThirdCity)
        self.fourthCity = City(nameFourthCity)
        self.listOfTowns = [self.firstCity, self.secondCity, self.thirdCity, self.fourthCity]
        self.preTech = values["begPreTech"]
        self.ecologyUp = values["begEcologyUp"]
        self.sanctions = [0,0,0,0,0,0]
        self.scoutsHome = 0
        self.scoutsHomeComing = 0
        self.scoutsInCountry = {i: [] for i in range(len(listOfCountries))}
        self.clearInRound = False
        self.message =  f"[РАУНД {round}]\n"
    def Clear(self):
        scoutDestroy = 0
        for i in range(len(self.scoutsInCountry)):
            z=0
            while z!=(len(self.scoutsInCountry[i])):
                ran = random.randint(1,100)
                if ran <= values["ClearanceSucc"]:
                    reveal = random.randint(1, 100)
                    if reveal <= values["revealChance"]:
                        self.message += f"- [ЧИСТКА]: Один из раскрытых отрядов был послан страной - {listOfCountries[i].name}\n"
                    self.scoutsInCountry[i].pop(z)
                    scoutDestroy += 1
                    listOfCountries[i].message += f"- [РАЗВЕДКА]: В стране {self.name} был уничтожен ваш разведовательный отряд\n"
                else:
                    z+=1
        self.message += f"- [ЧИСТКА]: На вашей территории было уничтожено {scoutDestroy} развед. отрядов\n"  #  В случае диверсантов, добавить информацию о колве уничтоженных

    def WillBeOnSanctions(self, byCountryNumber):
        self.sanctions[byCountryNumber] = not self.sanctions[byCountryNumber]
        return self.sanctions[byCountryNumber]
    def BlowUpAnother(self, countryNumber, cityNumber):
        listOfCountries[countryNumber].listOfTowns[cityNumber].bombComing += 1
        self.bombAmountNow -= 1
        blowLog[self.name + listOfCountries[countryNumber].listOfTowns[cityNumber].name] = 1
    def BuyScouts(self, amount):
        self.budget -= values["scoutsCost"]*amount
        self.scoutsHomeComing += amount
    def ImproveTown(self, cityNumber):
        self.budget -= values["improveCost"]
        self.listOfTowns[cityNumber].SetImprove()

    def BuyPVO(self, cityNumber):
        self.budget -= values["PVOCost"]
        self.listOfTowns[cityNumber].PVO = True

    def LifeQualRecalculation(self):
        avg = 0
        for city in self.listOfTowns:
            if city.existance:
                avg += city.lifeQual
        self.avgLifeQual = int(avg / len(self.listOfTowns))
    def SanctionsCoefficient(self):
        count = 0
        for i in self.sanctions:
            if i:
                count+=1
        return count
    def UpSoldiers(self):
        # for i in range(len(self.saboteursInCountry)):
        #     for z in range(len(self.saboteursInCountry[i])):
        #         if self.saboteursInCountry[i][z] != 2:
        #             self.saboteursInCountry[i][z] += 1
        for i in range(len(self.scoutsInCountry)):
            for z in range(len(self.scoutsInCountry[i])):
                if self.scoutsInCountry[i][z] != 2:
                    self.scoutsInCountry[i][z] += 1
    def MakeSoldiersActive(self):
        for i in range(len(self.scoutsInCountry)):
            msg = []
            aliveTowns = len([0 for k in range(len(self.listOfTowns)) if self.listOfTowns[k].existance])
            checkCityShield = [False for _ in range(len(self.listOfTowns))]
            checkCityPVO = [False for _ in range(len(self.listOfTowns))]
            for z in range(len(self.scoutsInCountry[i])):
                ran = random.randint(1,100)
                if ran <= values["LvlOfScouts"][self.scoutsInCountry[i][z]]:
                    variants = -1
                    while len(msg)!=5:
                        if 0 in msg and 1 in msg and 2 in msg and (len([0 for k in range(len(checkCityShield)) if not checkCityShield[k]]) == 0) and (len([0 for k in range(len(checkCityPVO)) if not checkCityPVO[k]]) == 0) :
                            break
                        variants = random.randint(1,100)
                        if variants <= 24:
                            currVar = 0
                        elif variants >= 25 and variants <= 49:
                            currVar = 1
                        elif variants >= 50 and variants <= 67:
                            currVar = 2
                        elif variants >= 68 and variants <= 85:
                            currVar = 3
                        elif variants >= 86:
                            currVar = 4
                        if currVar in msg and currVar <= 2:
                            continue
                        msg.append(currVar)
                        if currVar == 0:
                            listOfCountries[i].message += f"- [РАЗВЕДКА]: В стране {self.name} {self.bombAmountNow} бомб в данном раунде ({round+1})\n"
                            break
                        if currVar == 1:
                            listOfCountries[i].message += f"- [РАЗВЕДКА]: В стране {self.name} бюджет составляет {self.budget}$ в данном раунде ({round+1})\n"
                            break
                        if currVar == 2:
                            namesOfCities = []
                            for cityThis in range(len(finaleLogExposions[round][self.name])):
                                namesOfCities.append(finaleLogExposions[round][self.name][cityThis])
                            if len(namesOfCities) == 0:
                                listOfCountries[i].message += f"- [РАЗВЕДКА]: Страна {self.name} не атаковала в данном раунде ({round})\n"
                                break
                            else:
                                peakToExec = random.randint(0, len(namesOfCities)-1)
                                listOfCountries[i].message += f"- [РАЗВЕДКА]: Страна {self.name} атаковала {namesOfCities[peakToExec]} в данном раунде ({round})\n"
                                break
                        if currVar == 3:
                            if msg.count(currVar) > aliveTowns:
                                continue
                            cityForShield = random.randint(0,3)
                            while checkCityShield[cityForShield]:
                                cityForShield = random.randint(0,3)
                            listOfCountries[i].message += f"- [РАЗВЕДКА]: В стране {self.name} у города {self.listOfTowns[cityForShield].name} есть щит? - {YesNo(self.listOfTowns[cityForShield].shield)}\n"
                            checkCityShield[cityForShield] = True
                            break
                        if currVar == 4:
                            if msg.count(currVar) > aliveTowns:
                                continue
                            cityForPVO = random.randint(0, 3)
                            while checkCityPVO[cityForPVO]:
                                cityForPVO = random.randint(0, 3)
                            listOfCountries[
                                i].message += f"- [РАЗВЕДКА]: В стране {self.name} у города {self.listOfTowns[cityForPVO].name} есть ПВО? - {YesNo(self.listOfTowns[cityForPVO].PVO)}\n"
                            checkCityShield[cityForPVO] = True
                            break

    def RoundStart(self):
        global ecology
        self.message += f"\n[РАУНД {round+1}]\n"
        self.budget += self.payout # Выплата в бюджет выплат
        currPayout = 0
        if self.ecologyUp: # Расчет выплат
            ecology = int(ecology + ecology * values["ecologyUpg"])
        for city in self.listOfTowns:
            city.improve()
            city.BombsDown()
            if city.existance:
                currPayout += city.profit
        self.payout = currPayout + ecology # Выплаты + экология
        self.ecologyUp = False
        if self.preTech:        # Выдача технологии
            self.tech = True
        self.payout = int(self.payout * (1 - self.SanctionsCoefficient()*values["oneSanctionEffect"]))   # Перерасчет выплат, учитывая Санкции
        self.bombAmountNow += self.bombAmountComing          # Присоединение бомб, которые готовились
        self.bombAmountComing = 0            # Отчистка бомб, которые готовились
        self.LifeQualRecalculation()         # Перерасчет общего ур жизни
        self.scoutsHome += self.scoutsHomeComing  # Присоединение отрядов, которые готовились
        # self.saboteursHome += self.saboteursHomeComing
        self.scoutsHomeComing = 0      # Отчистка отрядов, которые готовились
        # self.saboteursHomeComing = 0
        if self.clearInRound:         # Убрать ограничение на чистку и отчистить
            self.Clear()
            self.clearInRound = False
        self.MakeSoldiersActive() # Активация отрядов
        self.UpSoldiers()
        # Тут добыча информации и работа диверс
    def SendScout(self,thisCountryVal, numberCountryTo):
        self.scoutsHome -= 1
        listOfCountries[numberCountryTo].scoutsInCountry[thisCountryVal].append(0)
    def MakeClear(self):
        self.clearInRound = True
        self.budget -= values["ClearanceCost"]
    def CreateTech(self):
        self.budget -= values["techCost"]
        self.preTech = True

    def BuyBombs(self, amount):
        self.budget -= amount * values["bombCost"]
        self.bombAmountComing += amount

    def BuyShield(self, cityNumber):
        self.budget -= values["shieldCost"]
        self.listOfTowns[cityNumber].shield = True

    def EcologyUp(self):
        self.budget -= values["ecologyCost"]