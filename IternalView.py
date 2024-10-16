from tkinter import *
from Values import MainValues
from CleanRAM import CleanUp
import tkinter.messagebox as mb
from YesNo import YesNo
from Logs import ClearLogs
from FileManager import Upload
ecology, badThings = 0, 0
from Values import ecology, badThings, round
from NotBaseValues import *


bg = "#f5f5f5"
b2 = "#fffafa"
values = MainValues()


def RoundStart(window):
    global ecology, badThings, round
    ClearLogs()
    ecology = int(ecology - badThings * ecology * values["ecoDowngrade"])
    for country in listOfCountries:
        country.RoundStart()
    round += 1
    badThings = 0
    Upload(listOfCountries, ecology, values, round)
    if round != values["EndRound"]:
        MainVision(window)
    else:
        End(window)

def MainVision(window):
    CleanUp(window)
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    frameEc = Frame(window, bg=bg)
    frameEc.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=1 / 9)
    begEco = values["begEcology"]
    Ec = Label(frameEc, text=f"Экология: {int(ecology / begEco * 100)}%", font=("TimesNewRoman", 10, "bold"),
               foreground="green", bg=bg)
    Ec.pack()

    frameRound = Frame(window, bg=bg)
    frameRound.place(relx=0.35, rely=0.03, relwidth=0.3, relheight=1 / 9)

    roundInit = Label(frameRound, text=f"Раунд {round}", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
    roundInit.pack()

    frameFirst = Frame(window, bg=b2)
    frameFirst.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)

    frameSecond = Frame(window, bg=b2)
    frameSecond.place(relx=0.15, rely=0.12 + 0.12, relwidth=0.7, relheight=1 / 9)

    frameThird = Frame(window, bg=b2)
    frameThird.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.7, relheight=1 / 9)

    frameFourth = Frame(window, bg=b2)
    frameFourth.place(relx=0.15, rely=0.12 + 0.12 * 3, relwidth=0.7, relheight=1 / 9)

    frameFifth = Frame(window, bg=b2)
    frameFifth.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)

    frameSixth = Frame(window, bg=b2)
    frameSixth.place(relx=0.15, rely=0.12 + 0.12 * 5, relwidth=0.7, relheight=1 / 9)

    FrameEndRound = Frame(window, bg=b2)
    FrameEndRound.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)

    firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 20), width=20,
                             height=7, command=lambda: InCountryVision(window, 0))
    firstCountryBtn.pack()

    SecondCountryBtn = Button(frameSecond, text=listOfCountries[1].name, font=("TimesNewRoman", 20), width=20,
                              height=7, command=lambda: InCountryVision(window, 1))
    SecondCountryBtn.pack()

    ThirdCountryBtn = Button(frameThird, text=listOfCountries[2].name, font=("TimesNewRoman", 20), width=20,
                             height=7, command=lambda: InCountryVision(window, 2))
    ThirdCountryBtn.pack()

    FourthCountryBtn = Button(frameFourth, text=listOfCountries[3].name, font=("TimesNewRoman", 20), width=20,
                              height=7, command=lambda: InCountryVision(window, 3))
    FourthCountryBtn.pack()

    FifthCountryBtn = Button(frameFifth, text=listOfCountries[4].name, font=("TimesNewRoman", 20), width=20,
                             height=7, command=lambda: InCountryVision(window, 4))
    FifthCountryBtn.pack()

    SixthCountryBtn = Button(frameSixth, text=listOfCountries[5].name, font=("TimesNewRoman", 20), width=20,
                             height=7, command=lambda: InCountryVision(window, 5))
    SixthCountryBtn.pack()

    RoundEndBtn = Button(FrameEndRound, text="Завершить раунд", font=("Verdana", 20, "bold"), width=20, height=7,
                         bg="red", foreground="white", command=lambda: areYouSure(window))
    RoundEndBtn.pack()
    window.mainloop()
def InCountryVision(window, numberCountry):
    CleanUp(window)
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: MainVision(window))
    back.pack()

    frameBudget = Frame(window, bg=bg)
    frameBudget.place(relx=0.03, rely=0.15, relwidth=0.27, relheight=1 / 9)
    Budget = Label(frameBudget, text=f"Бюджет: {listOfCountries[numberCountry].budget} $",
                   font=("TimesNewRoman", 12), bg=bg)
    Budget.pack()

    frameBombs = Frame(window, bg=bg)
    frameBombs.place(relx=0.01, rely=0.19, relwidth=0.26, relheight=1 / 9)
    Bombs = Label(frameBombs, text=f"Бомбы: {listOfCountries[numberCountry].bombAmountNow} шт",
                  font=("TimesNewRoman", 12), bg=bg)
    Bombs.pack()

    frameAvgQual = Frame(window, bg=bg)
    frameAvgQual.place(relx=0.01, rely=0.23, relwidth=0.30, relheight=1 / 9)
    Bombs = Label(frameAvgQual, text=f"Общ. УЖ: {listOfCountries[numberCountry].avgLifeQual} %",
                  font=("TimesNewRoman", 12), bg=bg)
    Bombs.pack()

    frameTech = Frame(window, bg=bg)
    frameTech.place(relx=0.01, rely=0.27, relwidth=0.31, relheight=1 / 9)
    Tech = Label(frameTech, text=f"Технология: " + YesNo(listOfCountries[numberCountry].tech),
                 font=("TimesNewRoman", 12), bg=bg)
    Tech.pack()

    frameBombCom = Frame(window, bg=bg)
    frameBombCom.place(relx=0.01, rely=0.31, relwidth=0.36, relheight=1 / 9)
    Tech = Label(frameBombCom, text=f"Бомбы заказ: " + str(listOfCountries[numberCountry].bombAmountComing) + " шт",
                 font=("TimesNewRoman", 12), bg=bg)
    Tech.pack()

    frameProfit = Frame(window, bg=bg)
    frameProfit.place(relx=0.01, rely=0.35, relwidth=0.26, relheight=1 / 9)
    Profit = Label(frameProfit, text=f" Доход: " + str(listOfCountries[numberCountry].payout) + " $",
                   font=("TimesNewRoman", 12), bg=bg)
    Profit.pack()

    frameProfit = Frame(window, bg=bg)
    frameProfit.place(relx=0.01, rely=0.39, relwidth=0.35, relheight=1 / 9)
    Profit = Label(frameProfit, text=f"Разведчики: " + str(listOfCountries[numberCountry].scoutsHome) + " чел",
                   font=("TimesNewRoman", 12), bg=bg)
    Profit.pack()

    leftCityVision(numberCountry, window)

    frameOrder = Frame(window, bg=bg)
    frameOrder.place(relx=0.1, rely=0.65, relwidth=0.45, relheight=1 / 9)
    Order = Button(frameOrder, width=45, height=15, text="Отдать приказ", font=("Realest", 19, "bold"), bg="green",
                   command=lambda: OrderCountry(window, numberCountry))
    Order.pack()
def Logs(window, number):
    global finaleLogExplosions
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    frameRound = Frame(window, bg=bg)
    frameRound.place(relx=0.35, rely=0.03, relwidth=0.3, relheight=1 / 9)
    roundInit = Label(frameRound, text=f"Раунд {number+1}", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
    roundInit.pack()
    frameRound = Frame(window, bg=bg)
    frameRound.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=1 / 9)
    roundInit = Label(frameRound, text="Логи", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
    roundInit.pack()
    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=1 / 9)
    T = Button(frameT, text="Назад", font=("TimesNewRoman", 20), bg=bg,
               command=lambda: End(window))
    T.pack()
    frameToward = Frame(window, bg=bg)
    frameToward.place(relx= 0.75, rely = 0.8, relwidth=0.2, relheight=1 / 9)
    Toward = Button(frameToward, text = "--->",font=("TimesNewRoman", 20), bg=bg, command=lambda: Logs(window, (number + 1) % (values["EndRound"]-1)))
    Toward.pack()
    frameToward = Frame(window, bg=bg)
    frameToward.place(relx=0.06, rely=0.8, relwidth=0.2, relheight=1 / 9)
    Toward = Button(frameToward, text="<---", font=("TimesNewRoman", 20), bg=bg,
                    command=lambda: Logs(window, (number + (values["EndRound"]-2)) % (values["EndRound"]-1)))
    Toward.pack()

    deli = 0.09
    x = 0
    if finaleLogExplosions[number][listOfCountries[0].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 0))
        firstCountryBtn.pack()
        x += deli
    if finaleLogExplosions[number][listOfCountries[1].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 1))
        firstCountryBtn.pack()
        x += deli
    if finaleLogExplosions[number][listOfCountries[2].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 2))
        firstCountryBtn.pack()
        x += deli
    if finaleLogExplosions[number][listOfCountries[3].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 3))
        firstCountryBtn.pack()
        x += deli
    if finaleLogExplosions[number][listOfCountries[4].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 4))
        firstCountryBtn.pack()
        x += deli
    if finaleLogExplosions[number][listOfCountries[5].name]:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ViewLogRound(number, 5))
        firstCountryBtn.pack()

def areYouSure(window):

    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameRound = Frame(window, bg=bg)
    frameRound.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)

    SureFrame = Frame(window, bg=bg)
    SureFrame.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
    Sure = Label(SureFrame, text="Вы уверены?", font=("Verdana", 20, "bold"), bg=bg)
    Sure.pack()

    YesFrame = Frame(window, bg=bg)
    YesFrame.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)
    RoundEndBtn = Button(YesFrame, text="Да", font=("Verdana", 20, "bold"), width=10, height=7,
                         bg="red", foreground="white", command=lambda: RoundStart(window))
    RoundEndBtn.pack()

    NoFrame = Frame(window, bg=bg)
    NoFrame.place(relx=0.15, rely=0.12 + 0.12 * 5, relwidth=0.7, relheight=1 / 9)
    RoundNotEndBtn = Button(NoFrame, text="Отмена", font=("Verdana", 20, "bold"), width=10, height=7,
                            command=lambda: MainVision(window))
    RoundNotEndBtn.pack()

    RoundFr = Frame(window, bg=bg)
    if round != 6:
        RoundFr.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.7, relheight=1 / 9)
        RoundLbl = Label(RoundFr, text=f"Раунд {round} → {round + 1} ", font=("Verdana", 20), bg="#f5f5f5")
    else:
        RoundFr.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.8, relheight=1 / 9)
        RoundLbl = Label(RoundFr, text=f"Раунд {round} → конец игры ", font=("Verdana", 20), bg="#f5f5f5")
    RoundLbl.pack()

def End(window):
    global listOfCountries
    listOfWinners = [x for x in range(len(listOfCountries))]
    listOfWinners = sorted(listOfWinners, key=lambda x: -listOfCountries[x].avgLifeQual)
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameOver = Frame(window, bg=bg)
    frameOver.place(relx=0.15, rely=0.05, relwidth=0.7, relheight= 1 / 9)
    Over = Label(frameOver, text = "GAME OVER", font=("TimesNewRoman", 25, "bold"), bg=bg)
    Over.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.16 + 0.12 * 6, relwidth=0.7, relheight=1 / 8)
    back = Button(frameBack, text="Логи", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: Logs(window, 0))
    back.pack()

    frameTabl = Frame(window, bg=bg)
    frameTabl.place(relx=0.01, rely=0.18, relwidth=0.2, relheight=1 / 9)
    Tabl = Label(frameTabl, text="Место", font=("TimesNewRoman", 15), bg=bg)
    Tabl.pack()

    frameTabl = Frame(window, bg=bg)
    frameTabl.place(relx=0.29, rely=0.18, relwidth=0.2, relheight=1 / 9)
    Tabl = Label(frameTabl, text="Страна", font=("TimesNewRoman", 15), bg=bg)
    Tabl.pack()
    x = 0
    y = 0
    for i in range(1, 7):
        frameTabl = Frame(window, bg=bg)
        frameTabl.place(relx=0.18, rely=0.28 + y, relwidth=0.45, relheight=1 / 9)
        Tabl = Label(frameTabl, text=listOfCountries[listOfWinners[i-1]].name +" ("+ str(listOfCountries[listOfWinners[i-1]].avgLifeQual)+"%)", font=("TimesNewRoman", 15, "bold"), bg=bg)
        Tabl.pack()
        y += 0.07
        frameTabl = Frame(window, bg=bg)
        frameTabl.place(relx=0.01, rely=0.28 + x, relwidth=0.2, relheight=1 / 9)
        Tabl = Label(frameTabl, text=str(i), font=("TimesNewRoman", 15), bg=bg)
        Tabl.pack()
        x+= 0.07


def TechOrder(window, numbercountry):
    global badThings, listOfCountries
    bg = "#f5f5f5"
    frameTechRes = Frame(window, bg=bg)
    frameTechRes.place(relx=0.15, rely=0.12 + 0.14 * 1, relwidth=0.7, relheight=1 / 9)
    if listOfCountries[numbercountry].tech or listOfCountries[numbercountry].preTech:
        TechRes = Label(frameTechRes, text="Технология уже разработана/разрабатывается", foreground="red", bg=bg)
        TechRes.pack()
    elif listOfCountries[numbercountry].preTech == False and listOfCountries[numbercountry].budget >= values[
        "techCost"]:
        listOfCountries[numbercountry].CreateTech()
        badThings += 1
        TechRes = Label(frameTechRes, text="Технология успешно приобретена", foreground="green", bg=bg)
        TechRes.pack()
    elif listOfCountries[numbercountry].preTech == False and listOfCountries[numbercountry].budget < values["techCost"]:
        TechRes = Label(frameTechRes, text="Недостаточно бюджетных средств", foreground="red", bg=bg)
        TechRes.pack()


def OneToNine(window, numberCountry):
    x = 0.26
    y = 0.12 * 4
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="1", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(1, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="2", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(2, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="3", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(3, window, numberCountry))
    Bomb1.pack()

    x = 0.26
    y += 0.12

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="4", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(4, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="5", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(5, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="6", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(6, window, numberCountry))
    Bomb1.pack()

    x = 0.26
    y += 0.12

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="7", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(7, window, numberCountry))
    Bomb1.pack()
    x += 0.2
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="8", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(8, window, numberCountry))
    Bomb1.pack()
    x += 0.2
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="9", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyBombs(9, window, numberCountry))
    Bomb1.pack()


def BuyBombs(amount, window, numberCountry):
    global badThings
    bg = "#f5f5f5"
    s = (listOfCountries[numberCountry].budget - amount * values["bombCost"])
    if s >= 0:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.25, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Успешно", font=("TimesNewRoman", 10, "bold"), bg=bg, height=10, foreground="green")
        T.pack()
        badThings += int(0.8 * amount)
        listOfCountries[numberCountry].BuyBombs(amount)
    else:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.25, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Недостаточно бюджетных средств", font=("TimesNewRoman", 10, "bold"), bg=bg, height=10,
                  foreground="red")
        T.pack()


def BombsOrder(window, numberCountry):
    bg = "#f5f5f5"
    if listOfCountries[numberCountry].tech:
        someframe = Frame(window, bg=bg)
        someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Технологии", font=("TimesNewRoman", 19, "bold"), bg=bg)
        T.pack()

        frameBomb = Frame(window, bg=bg)
        frameBomb.place(relx=0.01, rely=0.12 + 0.19, relwidth=1, relheight=2 / 9)
        Bomb = Label(frameBomb, text="Выберите количество бомб", font=("TimesNewRoman", 15), bg=bg)
        Bomb.pack()

        frameBack = Frame(window, bg=bg)
        frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
        back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                      command=lambda: OrderCountry(window, numberCountry))
        back.pack()

        frameCountry = Frame(window, bg=bg)
        frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
        Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                        bg=bg)
        Country.pack()

        OneToNine(window, numberCountry)
    else:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.14 * 1, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Отсутствует ядерная технология", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="red")
        T.pack()
def BuyScouts(amount, window, numberCountry):
    bg = "#f5f5f5"
    s = (listOfCountries[numberCountry].budget - amount * values["scoutsCost"])
    if s >= 0:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.25, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Успешно", font=("TimesNewRoman", 10, "bold"), bg=bg, height=10, foreground="green")
        T.pack()
        listOfCountries[numberCountry].BuyScouts(amount)
    else:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.25, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Недостаточно бюджетных средств", font=("TimesNewRoman", 10, "bold"), bg=bg, height=10,
                  foreground="red")
        T.pack()
def ScoutsOrder(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    T = Label(frameT, text="Технологии", font=("TimesNewRoman", 19, "bold"), bg=bg)
    T.pack()

    frameBomb = Frame(window, bg=bg)
    frameBomb.place(relx=0.15, rely=0.12 + 0.19, relwidth=0.7, relheight=1 / 9)
    Bomb = Label(frameBomb, text="Выберите колво разведчиков", font=("TimesNewRoman", 15), bg=bg)
    Bomb.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: TechCh(window, numberCountry))
    back.pack()

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()
    x = 0.26
    y = 0.12 * 4
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="1", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(1, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="2", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(2, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="3", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(3, window, numberCountry))
    Bomb1.pack()

    x = 0.26
    y += 0.12

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="4", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(4, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="5", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(5, window, numberCountry))
    Bomb1.pack()
    x += 0.2

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="6", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(6, window, numberCountry))
    Bomb1.pack()

    x = 0.26
    y += 0.12

    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="7", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(7, window, numberCountry))
    Bomb1.pack()
    x += 0.2
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="8", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(8, window, numberCountry))
    Bomb1.pack()
    x += 0.2
    frameBomb1 = Frame(window, bg="#f5f5f5")
    frameBomb1.place(relx=x, rely=y, relwidth=0.078, relheight=1 / 9)
    Bomb1 = Button(frameBomb1, text="9", font=("TimesNewRoman", 19), bg="#f5f5f5",
                   command=lambda: BuyScouts(9, window, numberCountry))
    Bomb1.pack()

def TechCh(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    T = Label(frameT, text="Технологии", font=("TimesNewRoman", 19, "bold"), bg=bg)
    T.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: OrderCountry(window, numberCountry))
    back.pack()

    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.01, rely=0.12 + 0.12 * 2, relwidth=0.5, relheight=2 / 9)
    TechBuy = Button(frameTechBuy, text="Ядерные исследования", font=("TimesNewRoman", 12), height=2, width=22, bg=bg,
                     command=lambda: TechOrder(window, numberCountry))
    TechBuy.pack()

    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.48, rely=0.12 + 0.12 * 2, relwidth=0.5, relheight=2 / 9)
    TechBuy = Button(frameTechBuy, text="Заказать боеголовки", font=("TimesNewRoman", 12), height=2, width=22,
                     bg=bg,
                     command=lambda: BombsOrder(window, numberCountry))
    TechBuy.pack()

    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.01, rely=0.12 + 0.12 * 3, relwidth=0.5, relheight=2 / 9)
    Scout = Button(frameTechBuy, text="Заказать разведчиков", font=("TimesNewRoman", 12), height=2, width=22,
                     bg=bg,
                     command=lambda: ScoutsOrder(window, numberCountry))
    Scout.pack()

    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.48, rely=0.12 + 0.12 * 3, relwidth=0.5, relheight=2 / 9)
    Saboteur = Button(frameTechBuy, text="ЧИСТКА", font=("TimesNewRoman", 12), height=2, width=22,
                      bg=bg,
                      command=lambda: ClearEnemy(window, numberCountry))
    Saboteur.pack()


def Transfer(window, numberCountry):
    bg = "#f5f5f5"
    DefaultAfterCountryVision(window, numberCountry)

    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    T = Label(frameT, text="Перевод средств", font=("TimesNewRoman", 19, "bold"), bg=bg)
    T.pack()

    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.09, relwidth=0.7, relheight=1 / 13)
    T = Label(frameT, text="Кому:", font=("TimesNewRoman", 19), bg=bg)
    T.pack()
    deli = 0.09
    x = 0
    if numberCountry != 0:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 0))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 1:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 1))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 2:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 2))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 3:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 3))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 4:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 4))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 5:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: TransferIn(window, numberCountry, 5))
        firstCountryBtn.pack()


def btn_click(window, numberCountry, countryToTransfer, Amount):
    try:
        amount = int(Amount)
        if amount <= 0:
            frameNo = Frame(window, bg="#f5f5f5")
            frameNo.place(relx=0.17, rely=0.12 + 0.38, relwidth=0.7, relheight=1 / 18)
            No = Label(frameNo, text="Введено некорректное число", font=("TimesNewRoman", 13), bg="#f5f5f5",
                       foreground="red", width=30, height=1)
            No.pack()
        elif listOfCountries[numberCountry].budget < amount:
            frameNo = Frame(window, bg="#f5f5f5")
            frameNo.place(relx=0.17, rely=0.12 + 0.38, relwidth=0.7, relheight=1 / 18)
            No = Label(frameNo, text="Недостаточно средств", font=("TimesNewRoman", 13), bg="#f5f5f5",
                       foreground="red", width=30, height=1)
            No.pack()
        else:
            frameNo = Frame(window, bg="#f5f5f5")
            frameNo.place(relx=0.15, rely=0.12 + 0.38, relwidth=0.7, relheight=1 / 18)
            No = Label(frameNo, text="Успешно", font=("TimesNewRoman", 13), bg="#f5f5f5",
                       foreground="green", width=30, height=1)
            No.pack()
            listOfCountries[numberCountry].budget -= amount
            listOfCountries[countryToTransfer].budget += amount

    except:
        frameNo = Frame(window, bg="#f5f5f5")
        frameNo.place(relx=0.15, rely=0.12 + 0.38, relwidth=0.7, relheight=1 / 18)
        No = Label(frameNo, text="Не число", font=("TimesNewRoman", 13), bg="#f5f5f5",
                   foreground="red", width=30, height=1)
        No.pack()


def TransferIn(window, numberCountry, countryToTransfer):
    bg = "#f5f5f5"

    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameTrans = Frame(window, bg=bg)
    frameTrans.place(relx=0.15, rely=0.06, relwidth=0.7, relheight=1 / 9)
    Trans = Label(frameTrans, text="Перевод", font=("TimesNewRoman", 25, "bold"), bg=bg)
    Trans.pack()

    frameToWhat = Frame(window, bg=bg)
    frameToWhat.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    ToWhat = Label(frameToWhat,
                   text=str(listOfCountries[numberCountry].name) + " → " + str(listOfCountries[countryToTransfer].name),
                   font=("TimesNewRoman", 19, "bold"), bg=bg)
    ToWhat.pack()

    frameToWhat = Frame(window, bg=bg)
    frameToWhat.place(relx=0.15, rely=0.12 + 0.23, relwidth=0.7, relheight=1 / 9)
    ToWhat = Label(frameToWhat,
                   text="Введите сумму для перевода:",
                   font=("TimesNewRoman", 15), bg=bg)
    ToWhat.pack()

    frameSend = Frame(window, bg=bg)
    frameSend.place(relx=0.15, rely=0.12 + 0.43, relwidth=0.7, relheight=1 / 9)

    frameAmountInput = Frame(window, bg=bg)
    frameAmountInput.place(relx=0.15, rely=0.12 + 0.33, relwidth=0.7, relheight=1 / 9)
    AmountInput = Entry(frameAmountInput, bg=bg, width=15)
    AmountInput.pack()

    Send = Button(frameSend, text="Перевести", font=("TimesNewRoman", 24, "bold"), width=15, bg="green",
                  height=10, command=lambda: btn_click(window, numberCountry, countryToTransfer, AmountInput.get()))
    Send.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: Transfer(window, numberCountry))
    back.pack()


def DefaultAfterCountryVision(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.13, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: OrderCountry(window, numberCountry))
    back.pack()


def CityUpgrade(window, numberCountry, cityNumber):
    bg = "#f5f5f5"
    frameCityVar = Frame(window, bg=bg)
    frameCityVar.place(relx=0.15, rely=0.12 + 0.08, relwidth=0.7, relheight=1 / 20)

    if listOfCountries[numberCountry].listOfTowns[cityNumber].existance == False:
        CityVar = Label(frameCityVar, text="Город был уничтожен", foreground="red", bg=bg)
        CityVar.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].development == 100:
        CityVar = Label(frameCityVar, text="Город уже был улучшен до максимума", foreground="red", bg=bg)
        CityVar.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].improved == False and listOfCountries[
        numberCountry].budget >= 150:
        listOfCountries[numberCountry].ImproveTown(cityNumber)
        CityVar = Label(frameCityVar, text="Успешное улучшение города", foreground="green", bg=bg)
        CityVar.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].improved:
        CityVar = Label(frameCityVar, text="Город уже был улучшен", foreground="red", bg=bg)
        CityVar.pack()
    else:
        CityVar = Label(frameCityVar, text="Недостаточно бюджетных средств", foreground="red", bg=bg)
        CityVar.pack()


def CityShieldPlace(window, numberCountry, cityNumber):
    bg = "#f5f5f5"
    frameCityShield = Frame(window, bg=bg)
    frameCityShield.place(relx=0.15, rely=0.12 + 0.08, relwidth=0.7, relheight=1 / 20)
    if not listOfCountries[numberCountry].listOfTowns[cityNumber].existance:
        CityShield = Label(frameCityShield, text="Город уничтожен", foreground="red", bg=bg)
        CityShield.pack()
    elif listOfCountries[numberCountry].tech == False:
        CityShield = Label(frameCityShield, text="Отсутствует ядерная технология", foreground="red", bg=bg)
        CityShield.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].shield == False and listOfCountries[
        numberCountry].budget >= values["shieldCost"]:
        listOfCountries[numberCountry].BuyShield(cityNumber)
        CityShield = Label(frameCityShield, text="Успешное установление щита", foreground="green", bg=bg)
        CityShield.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].shield == True:
        CityShield = Label(frameCityShield, text="Город уже под щитом", foreground="red", bg=bg)
        CityShield.pack()
    else:
        CityShield = Label(frameCityShield, text="Недостаточно бюджетных средств", foreground="red", bg=bg)
        CityShield.pack()


def CityPVOPlace(window, numberCountry, cityNumber):
    bg = "#f5f5f5"
    frameCityPVO = Frame(window, bg=bg)
    frameCityPVO.place(relx=0.15, rely=0.12 + 0.08, relwidth=0.7, relheight=1 / 20)
    if listOfCountries[numberCountry].listOfTowns[cityNumber].PVO == False and listOfCountries[
        numberCountry].budget >= 175:
        listOfCountries[numberCountry].BuyPVO(cityNumber)
        CityPVO = Label(frameCityPVO, text="Успешное установление ПВО", foreground="green", bg=bg)
        CityPVO.pack()
    elif listOfCountries[numberCountry].listOfTowns[cityNumber].PVO == True:
        CityPVO = Label(frameCityPVO, text="Город уже имеет ПВО", foreground="red", bg=bg)
        CityPVO.pack()
    else:
        CityPVO = Label(frameCityPVO, text="Недостаточно бюджетных средств", foreground="red", bg=bg)
        CityPVO.pack()


def CityEdit(window, numberCountry, cityNumber):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: CityPeak(window, numberCountry))
    back.pack()

    frameCityUp = Frame(window, bg=bg)
    frameCityUp.place(relx=0.15, rely=0.12 + 0.14, relwidth=0.7, relheight=1 / 9)
    CityUp = Button(frameCityUp, text="Улучшить город", font=("TimesNewRoman", 20), width=20,
                    height=7, command=lambda: CityUpgrade(window, numberCountry, cityNumber))
    CityUp.pack()

    frameCityShield = Frame(window, bg=bg)
    frameCityShield.place(relx=0.15, rely=0.12 + 0.14 * 2, relwidth=0.7, relheight=1 / 9)
    CityShield = Button(frameCityShield, text="Установить щит", font=("TimesNewRoman", 20), width=20,
                        height=7, command=lambda: CityShieldPlace(window, numberCountry, cityNumber))
    CityShield.pack()

    frameCityPVO = Frame(window, bg=bg)
    frameCityPVO.place(relx=0.15, rely=0.12 + 0.14 * 3, relwidth=0.7, relheight=1 / 9)
    CityPVO = Button(frameCityPVO, text="Установить ПВО", font=("TimesNewRoman", 20), width=20,
                     height=7, command=lambda: CityPVOPlace(window, numberCountry, cityNumber))
    CityPVO.pack()


def CityPeak(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    DefaultAfterCountryVision(window, numberCountry)

    frameInterview = Frame(window, bg=bg)
    frameInterview.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
    Interview = Label(frameInterview, text="Выберите город:", font=("TimesNewRoman", 20, "bold"),
                      bg=bg)
    Interview.pack()

    frameFirstCity = Frame(window, bg=bg)
    frameFirstCity.place(relx=0.15, rely=0.12 + 0.13, relwidth=0.7, relheight=1 / 9)
    FirstCity = Button(frameFirstCity, text=listOfCountries[numberCountry].firstCity.name, font=("TimesNewRoman", 20),
                       width=20,
                       height=7, command=lambda: CityEdit(window, numberCountry, 0))
    FirstCity.pack()

    frameSecondCity = Frame(window, bg=bg)
    frameSecondCity.place(relx=0.15, rely=0.12 + 0.13 * 2, relwidth=0.7, relheight=1 / 9)
    SecondCity = Button(frameSecondCity, text=listOfCountries[numberCountry].secondCity.name,
                        font=("TimesNewRoman", 20),
                        width=20,
                        height=7, command=lambda: CityEdit(window, numberCountry, 1))
    SecondCity.pack()

    frameThirdCity = Frame(window, bg=bg)
    frameThirdCity.place(relx=0.15, rely=0.12 + 0.13 * 3, relwidth=0.7, relheight=1 / 9)
    ThirdCity = Button(frameThirdCity, text=listOfCountries[numberCountry].thirdCity.name, font=("TimesNewRoman", 20),
                       width=20,
                       height=7, command=lambda: CityEdit(window, numberCountry, 2))
    ThirdCity.pack()

    frameFourthCity = Frame(window, bg=bg)
    frameFourthCity.place(relx=0.15, rely=0.12 + 0.13 * 4, relwidth=0.7, relheight=1 / 9)
    FourthCity = Button(frameFourthCity, text=listOfCountries[numberCountry].fourthCity.name,
                        font=("TimesNewRoman", 20),
                        width=20,
                        height=7, command=lambda: CityEdit(window, numberCountry, 3))
    FourthCity.pack()


def EcUp(window, numberCountry):
    global ecology
    bg = "#f5f5f5"
    frameEc = Frame(window, bg=bg)
    frameEc.place(relx=0.15, rely=0.12 + 0.35, relwidth=0.7, relheight=1 / 20)
    if listOfCountries[numberCountry].ecologyUp == False and listOfCountries[numberCountry].budget >= values[
        "ecologyCost"]:
        listOfCountries[numberCountry].ecologyUp = True
        listOfCountries[numberCountry].budget -= values["ecologyCost"]
        Ec = Label(frameEc, text="Успешное вложение в экологию", foreground="green", bg=bg, font=("TimesNewRoman", 9))
        Ec.pack()
    elif listOfCountries[numberCountry].ecologyUp:
        Ec = Label(frameEc, text="Страна уже вкладывалась в экологию в этом раунде", foreground="red", bg=bg,
                   font=("TimesNewRoman", 9))
        Ec.pack()
    else:
        Ec = Label(frameEc, text="Недостаточно бюджетных средств", foreground="red", bg=bg, font=("TimesNewRoman", 9))
        Ec.pack()


def SureEcUp(window, numberCountry):
    bg = "#f5f5f5"
    DefaultAfterCountryVision(window, numberCountry)
    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    T = Label(frameT, text="Улучшение экологии", font=("TimesNewRoman", 19, "bold"), bg=bg)
    T.pack()

    frameSure = Frame(window, bg=bg)
    frameSure.place(relx=0.06, rely=0.12 + 0.25, relwidth=0.9, relheight=1 / 9)
    Sure = Label(frameSure, text="Вы уверены, что хотите улучшить экологию?", font=("TimesNewRoman", 13, "bold"), bg=bg)
    Sure.pack()

    frameButSure = Frame(window, bg=bg)
    frameButSure.place(relx=0.15, rely=0.12 + 0.4, relwidth=0.7, relheight=1 / 9)
    ButSure = Button(frameButSure, text="Улучшить", font=("TimesNewRoman", 20, "bold"), width=20,
                     height=7, bg="green", command=lambda: EcUp(window, numberCountry))
    ButSure.pack()


def BlowUpCountryCity(window, numberCountry, numberCountryToAttack, numberCityToAttack):
    global blowLog
    global finaleLogExposions
    bg = "#f5f5f5"
    frameBlowing = Frame(window, bg=bg)
    frameBlowing.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=1 / 20)
    if listOfCountries[numberCountry].bombAmountNow == 0:
        Blowing = Label(frameBlowing, text="Запас бомб закончился", foreground="red", bg=bg, font=("TimesNewRoman", 9))
        Blowing.pack()
    elif blowLog[listOfCountries[numberCountry].name + listOfCountries[numberCountryToAttack].listOfTowns[
        numberCityToAttack].name] != 0:
        Blowing = Label(frameBlowing, text="Страна уже отправляла туда бомбу в этом раунде", foreground="red", bg=bg,
                        font=("TimesNewRoman", 9))
        Blowing.pack()
    elif not listOfCountries[numberCountryToAttack].listOfTowns[numberCityToAttack].existance:
        Blowing = Label(frameBlowing, text="Данный город уже уничтожен", foreground="red", bg=bg,
                        font=("TimesNewRoman", 9))
        Blowing.pack()
    else:
        blowLog[listOfCountries[numberCountry].name + listOfCountries[numberCountryToAttack].listOfTowns[
            numberCityToAttack].name] = 1
        finaleLogExposions[round][listOfCountries[numberCountry].name].append(listOfCountries[numberCountryToAttack].listOfTowns[numberCityToAttack].name)
        listOfCountries[numberCountry].BlowUpAnother(numberCountryToAttack, numberCityToAttack)
        Blowing = Label(frameBlowing, text="Бомба успешно отправлена", foreground="green", bg=bg,
                        font=("TimesNewRoman", 9))
        Blowing.pack()


def BlowUpCity(window, numberCountry, numberCountryToAttack):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.13, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: BlowUpCountry(window, numberCountry))
    back.pack()

    frameCountryToAttack = Frame(window, bg=bg)
    frameCountryToAttack.place(relx=0, rely=0.12 + 0.03, relwidth=1, relheight=1 / 9)
    CountryToAttack = Label(frameCountryToAttack,
                            text=f"Выберите город страны {listOfCountries[numberCountryToAttack].name} для атаки:",
                            font=("TimesNewRoman", 15, "bold"),
                            bg=bg)
    CountryToAttack.pack()

    deli = 0.09
    x = 0
    frameFirstCity = Frame(window, bg=bg)
    frameFirstCity.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=1 / 9)
    firstCityBtn = Button(frameFirstCity, text=listOfCountries[numberCountryToAttack].firstCity.name,
                          font=("TimesNewRoman", 15), width=20,
                          height=1, command=lambda: BlowUpCountryCity(window, numberCountry, numberCountryToAttack, 0))
    firstCityBtn.pack()
    x += deli
    frameFirst = Frame(window, bg=bg)
    frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
    firstCountryBtn = Button(frameFirst, text=listOfCountries[numberCountryToAttack].secondCity.name,
                             font=("TimesNewRoman", 15), width=20,
                             height=1,
                             command=lambda: BlowUpCountryCity(window, numberCountry, numberCountryToAttack, 1))
    firstCountryBtn.pack()
    x += deli
    frameFirst = Frame(window, bg=bg)
    frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
    firstCountryBtn = Button(frameFirst, text=listOfCountries[numberCountryToAttack].thirdCity.name,
                             font=("TimesNewRoman", 15), width=20,
                             height=1,
                             command=lambda: BlowUpCountryCity(window, numberCountry, numberCountryToAttack, 2))
    firstCountryBtn.pack()
    x += deli
    frameFirst = Frame(window, bg=bg)
    frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
    firstCountryBtn = Button(frameFirst, text=listOfCountries[numberCountryToAttack].fourthCity.name,
                             font=("TimesNewRoman", 15), width=20,
                             height=1,
                             command=lambda: BlowUpCountryCity(window, numberCountry, numberCountryToAttack, 3))
    firstCountryBtn.pack()

def ClearEnemy(window, numberCountry):
    bg = "#f5f5f5"
    if not listOfCountries[numberCountry].clearInRound and listOfCountries[numberCountry].budget>=200:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.14 * 1, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Успешная чистка", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="green")
        T.pack()
        listOfCountries[numberCountry].MakeClear()
    elif not listOfCountries[numberCountry].clearInRound:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.14 * 1, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Недостаточно бюджетных средств", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="red")
        T.pack()
    else:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.14 * 1, relwidth=0.7, relheight=1 / 9)
        T = Label(frameT, text="Чистка уже была завершена", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="red")
        T.pack()
def BlowUpCountry(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    DefaultAfterCountryVision(window, numberCountry)
    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: Arsenal(window, numberCountry))
    back.pack()
    frameCountryToAttack = Frame(window, bg=bg)
    frameCountryToAttack.place(relx=0, rely=0.12 + 0.03, relwidth=1, relheight=1 / 9)
    CountryToAttack = Label(frameCountryToAttack, text="Выберите страну для атаки:", font=("TimesNewRoman", 15, "bold"),
                            bg=bg)
    CountryToAttack.pack()

    deli = 0.09
    x = 0
    if numberCountry != 0:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 0))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 1:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 1))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 2:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 2))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 3:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 3))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 4:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 4))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 5:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: BlowUpCity(window, numberCountry, 5))
        firstCountryBtn.pack()


def MakeSanctions(window, numberCountry, numberToSanc):
    CleanUp(window)
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    if numberToSanc != -1:
        result = listOfCountries[numberToSanc].WillBeOnSanctions(numberCountry)
        frameS = Frame(window, bg=bg)
        frameS.place(relx=0.25, rely=0.05 + 0.12 * 6, relwidth=0.5, relheight=1 / 9)
        if result:
            listOfCountries[numberToSanc].message += f"- [САНКЦИИ]: Страна {listOfCountries[numberCountry].name} наложила на Вас санкции.\n"
            S = Label(frameS, text="Санкции наложены", foreground="red", bg=bg)
            S.pack()
        else:
            listOfCountries[
                numberToSanc].message += f"- [САНКЦИИ]: Страна {listOfCountries[numberCountry].name} сняла с Вас санкции.\n"
            S = Label(frameS, text="Санкции успешно сняты", foreground="green", bg=bg)
            S.pack()

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.13, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: OrderCountry(window, numberCountry))
    back.pack()
    deli = 0.09
    x = 0
    if numberCountry != 0:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[0].sanctions[numberCountry]) + "red"*(listOfCountries[0].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 0))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 1:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[1].sanctions[numberCountry]) + "red"*(listOfCountries[1].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 1))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 2:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[2].sanctions[numberCountry]) + "red"*(listOfCountries[2].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 2))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 3:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[3].sanctions[numberCountry]) + "red"*(listOfCountries[3].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 3))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 4:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[4].sanctions[numberCountry]) + "red"*(listOfCountries[4].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 4))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 5:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), bg = "green"*(not listOfCountries[5].sanctions[numberCountry]) + "red"*(listOfCountries[5].sanctions[numberCountry]), width=20,
                                 height=1, command=lambda: MakeSanctions(window, numberCountry, 5))
        firstCountryBtn.pack()

    frameSanc = Frame(window, bg=bg)
    frameSanc.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
    Sanc = Label(frameSanc, text="Наложение санкций", font=("TimesNewRoman", 19, "bold"), bg=bg)
    Sanc.pack()

    frameSanc = Frame(window, bg=bg)
    frameSanc.place(relx=0.15, rely=0.12 + 0.11, relwidth=0.7, relheight=1 / 35)
    Sanc = Label(frameSanc, text="Выберите страну для наложения санкций:", font=("TimesNewRoman", 12), bg=bg)
    Sanc.pack()
def ScoutSend(window, numberCountry, numberCountryTo):
    bg = "#f5f5f5"
    if listOfCountries[numberCountry].scoutsHome == 0:
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.09, relwidth=0.7, relheight=1 / 30)
        T = Label(frameT, text="Отсутствуют отряды", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="red")
        T.pack()
    else:
        listOfCountries[numberCountry].SendScout(numberCountry, numberCountryTo)
        frameT = Frame(window, bg=bg)
        frameT.place(relx=0.15, rely=0.12 + 0.09, relwidth=0.7, relheight=1 / 30)
        T = Label(frameT, text=f"Отряд был отправлен", font=("TimesNewRoman", 10), bg=bg, height=6,
                  foreground="green")
        T.pack()
def ScoutDefine(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.13, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    frameCountryToAttack = Frame(window, bg=bg)
    frameCountryToAttack.place(relx=0, rely=0.12 + 0.03, relwidth=1, relheight=1 / 9)
    CountryToAttack = Label(frameCountryToAttack, text="Выберите страну для отправки разведки:", font=("TimesNewRoman", 15, "bold"),
                            bg=bg)
    CountryToAttack.pack()
    deli = 0.09
    x = 0
    if numberCountry != 0:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 0))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 1:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 1))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 2:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 2))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 3:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 3))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 4:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 4))
        firstCountryBtn.pack()
        x += deli
    if numberCountry != 5:
        frameFirst = Frame(window, bg=bg)
        frameFirst.place(relx=0.15, rely=0.3 + x, relwidth=0.7, relheight=1 / 9)
        firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), width=20,
                                 height=1, command=lambda: ScoutSend(window, numberCountry, 5))
        firstCountryBtn.pack()
    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: Arsenal(window, numberCountry))
    back.pack()
def Arsenal(window, numberCountry):
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameT = Frame(window, bg=bg)
    frameT.place(relx=0.15, rely=0.12 + 0.03, relwidth=0.7, relheight=1 / 9)
    T = Label(frameT, text="Арсенал", font=("TimesNewRoman", 19, "bold"), bg=bg)
    T.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: OrderCountry(window, numberCountry))
    back.pack()


    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.48, rely=0.12 + 0.12 * 2, relwidth=0.5, relheight=2 / 9)
    TechBuy = Button(frameTechBuy, text="Направить разведку", font=("TimesNewRoman", 12), height=2, width=22,
                     bg=bg,
                     command=lambda: ScoutDefine(window, numberCountry))
    TechBuy.pack()


    frameTechBuy = Frame(window, bg=bg)
    frameTechBuy.place(relx=0.01, rely=0.12 + 0.12 * 2, relwidth=0.5, relheight=2 / 9)
    TechBuy = Button(frameTechBuy, text="Использовать бомбы", font=("TimesNewRoman", 12), height=2, width=22,
                     bg=bg,
                     command=lambda: BlowUpCountry(window, numberCountry))
    TechBuy.pack()
def OrderCountry(window, numberCountry):
    CleanUp(window)
    bg = "#f5f5f5"
    someframe = Frame(window, bg=bg)
    someframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameCountry = Frame(window, bg=bg)
    frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
    Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
                    bg=bg)
    Country.pack()

    frameBack = Frame(window, bg=bg)
    frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
    back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
                  command=lambda: InCountryVision(window, numberCountry))
    back.pack()

    frameTechChange = Frame(window, bg=bg)
    frameTechChange.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
    TechChange = Button(frameTechChange, text="Технологии", font=("TimesNewRoman", 20), width=20,
                        height=7, command=lambda: TechCh(window, numberCountry))
    TechChange.pack()

    frameTechChange = Frame(window, bg=bg)
    frameTechChange.place(relx=0.15, rely=0.12 + 0.12, relwidth=0.7, relheight=1 / 9)
    TechChange = Button(frameTechChange, text="Переводы", font=("TimesNewRoman", 20), width=20,
                        height=7, command=lambda: Transfer(window, numberCountry))
    TechChange.pack()

    frameTechChange = Frame(window, bg=bg)
    frameTechChange.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.7, relheight=1 / 9)
    TechChange = Button(frameTechChange, text="Управление городами", font=("TimesNewRoman", 20), width=20,
                        height=7, command=lambda: CityPeak(window, numberCountry))
    TechChange.pack()

    if listOfCountries[numberCountry].ecologyUp:
        frameTechChange = Frame(window, bg=bg)
        frameTechChange.place(relx=0.15, rely=0.12 + 0.12 * 3, relwidth=0.7, relheight=1 / 9)
        TechChange = Button(frameTechChange, text="Вложиться в экологию", font=("TimesNewRoman", 20), width=20,
                            height=7, bg="red")
        TechChange.pack()
    else:
        frameTechChange = Frame(window, bg=bg)
        frameTechChange.place(relx=0.15, rely=0.12 + 0.12 * 3, relwidth=0.7, relheight=1 / 9)
        TechChange = Button(frameTechChange, text="Вложиться в экологию", font=("TimesNewRoman", 20), width=20,
                            height=7, command=lambda: SureEcUp(window, numberCountry))
        TechChange.pack()

    if listOfCountries[numberCountry].bombAmountNow  or listOfCountries[numberCountry].scoutsHome: # В случае разведчиков, добавить условие
        frameBlowBombs = Frame(window, bg=bg)
        frameBlowBombs.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)
        BlowBombs = Button(frameBlowBombs, text="Использовать арсенал", font=("TimesNewRoman", 20), width=20,
                           height=7, command=lambda: Arsenal(window, numberCountry))
        BlowBombs.pack()
    else:
        frameBlowBombs = Frame(window, bg=bg)
        frameBlowBombs.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)
        BlowBombs = Button(frameBlowBombs, text="Использовать арсенал", font=("TimesNewRoman", 20), bg="red",
                           width=20,
                           height=7)
        BlowBombs.pack()

    frameSanctions = Frame(window, bg=bg)
    frameSanctions.place(relx=0.15, rely=0.12 + 0.12 * 5, relwidth=0.7, relheight=1 / 9)
    Sanctions = Button(frameSanctions, text="Наложить санкции", font=("TimesNewRoman", 20), width=20,
                        height=7, command=lambda: MakeSanctions(window, numberCountry, -1))
    Sanctions.pack()

def ViewLogRound(number, country):
    global finaleLogExplosions
    message = ''
    for name in finaleLogExplosions[number][listOfCountries[country].name]:
        message +=name + "\n"
    mb.showinfo(listOfCountries[country].name, message = message)
def leftCityVision(numberCountry, window):
    counter = 0
    length = 0.1
    for city in listOfCountries[numberCountry].listOfTowns:
        if city.existance:
            bg = "#f5f5f5"
        else:
            bg = "red"
        frameSecondCity = Frame(window, bg=bg)
        frameSecondCity.place(relx=0.67, rely=length, relwidth=0.25, relheight=1 / 9)
        F = Label(frameSecondCity, text=city.name,
                  font=("TimesNewRoman", 13, "bold"), bg=bg)
        F.pack()
        counter += 1
        length += 0.05

        frameDevelopment = Frame(window, bg=bg)
        frameDevelopment.place(relx=0.68, rely=length, relwidth=0.23, relheight=1 / 40)
        First = Label(frameDevelopment,
                      text=" " * (3 * int(len(city.name) / 3) - 10) + "Развитие: " + str(
                          city.development) + " %",
                      font=("TimesNewRoman", 8), bg=bg)
        First.pack()
        counter += 1
        length += 0.03

        frameLifeQual = Frame(window, bg=bg)
        frameLifeQual.place(relx=0.675, rely=length, relwidth=0.25, relheight=1 / 40)
        First = Label(frameLifeQual,
                      text=" " * (3 * int(
                          len(city.name) / 3) - 10) + "УР. Жизни: " + str(
                          city.lifeQual) + " %",
                      font=("TimesNewRoman", 8), bg=bg)
        First.pack()
        counter += 1
        length += 0.03

        frameProfit = Frame(window, bg=bg)
        frameProfit.place(relx=0.7, rely=length, relwidth=0.2, relheight=1 / 40)
        First = Label(frameProfit,
                      text=" " * (3 * int(
                          len(city.name) / 3) - 10) + "Доход: " + str(
                          city.profit) + " $",
                      font=("TimesNewRoman", 8), bg=bg)
        First.pack()
        counter += 1
        length += 0.03

        frameShield = Frame(window, bg=bg)
        frameShield.place(relx=0.7, rely=length, relwidth=0.2, relheight=1 / 40)
        First = Label(frameShield,
                      text=" " * (3 * int(
                          len(city.name) / 3) - 10) + "Щит: " +
                           YesNo(city.shield),
                      font=("TimesNewRoman", 8), bg=bg)
        First.pack()
        counter += 1
        length += 0.03

        framePVO = Frame(window, bg=bg)
        framePVO.place(relx=0.7, rely=length, relwidth=0.2, relheight=1 / 40)
        First = Label(framePVO,
                      text=" " * (3 * int(
                          len(city.name) / 3) - 10) + "ПВО: " +
                           YesNo(city.PVO),
                      font=("TimesNewRoman", 8), bg=bg)
        First.pack()
        length += 0.05
        counter += 1