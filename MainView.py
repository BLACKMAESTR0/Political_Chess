# from Start import RoundStart
# from IternalView import *
# values = MainValues()
# bg = "#f5f5f5"
# b2 = "#fffafa"
# def MainVision(window):
#     global ecology
#     CleanUp(window)
#     someframe = Frame(window, bg=bg)
#     someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
#     frameEc = Frame(window, bg=bg)
#     frameEc.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=1 / 9)
#     begEco = values["begEcology"]
#     Ec = Label(frameEc, text=f"Экология: {int(ecology / begEco * 100)}%", font=("TimesNewRoman", 10, "bold"),
#                foreground="green", bg=bg)
#     Ec.pack()
#
#     frameRound = Frame(window, bg=bg)
#     frameRound.place(relx=0.35, rely=0.03, relwidth=0.3, relheight=1 / 9)
#
#     roundInit = Label(frameRound, text=f"Раунд {round}", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
#     roundInit.pack()
#
#     frameFirst = Frame(window, bg=b2)
#     frameFirst.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
#
#     frameSecond = Frame(window, bg=b2)
#     frameSecond.place(relx=0.15, rely=0.12 + 0.12, relwidth=0.7, relheight=1 / 9)
#
#     frameThird = Frame(window, bg=b2)
#     frameThird.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.7, relheight=1 / 9)
#
#     frameFourth = Frame(window, bg=b2)
#     frameFourth.place(relx=0.15, rely=0.12 + 0.12 * 3, relwidth=0.7, relheight=1 / 9)
#
#     frameFifth = Frame(window, bg=b2)
#     frameFifth.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)
#
#     frameSixth = Frame(window, bg=b2)
#     frameSixth.place(relx=0.15, rely=0.12 + 0.12 * 5, relwidth=0.7, relheight=1 / 9)
#
#     FrameEndRound = Frame(window, bg=b2)
#     FrameEndRound.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
#
#     firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 20), width=20,
#                              height=7, command=lambda: InCountryVision(window, 0))
#     firstCountryBtn.pack()
#
#     SecondCountryBtn = Button(frameSecond, text=listOfCountries[1].name, font=("TimesNewRoman", 20), width=20,
#                               height=7, command=lambda: InCountryVision(window, 1))
#     SecondCountryBtn.pack()
#
#     ThirdCountryBtn = Button(frameThird, text=listOfCountries[2].name, font=("TimesNewRoman", 20), width=20,
#                              height=7, command=lambda: InCountryVision(window, 2))
#     ThirdCountryBtn.pack()
#
#     FourthCountryBtn = Button(frameFourth, text=listOfCountries[3].name, font=("TimesNewRoman", 20), width=20,
#                               height=7, command=lambda: InCountryVision(window, 3))
#     FourthCountryBtn.pack()
#
#     FifthCountryBtn = Button(frameFifth, text=listOfCountries[4].name, font=("TimesNewRoman", 20), width=20,
#                              height=7, command=lambda: InCountryVision(window, 4))
#     FifthCountryBtn.pack()
#
#     SixthCountryBtn = Button(frameSixth, text=listOfCountries[5].name, font=("TimesNewRoman", 20), width=20,
#                              height=7, command=lambda: InCountryVision(window, 5))
#     SixthCountryBtn.pack()
#
#     RoundEndBtn = Button(FrameEndRound, text="Завершить раунд", font=("Verdana", 20, "bold"), width=20, height=7,
#                          bg="red", foreground="white", command=lambda: areYouSure(window))
#     RoundEndBtn.pack()
#     window.mainloop()
# def InCountryVision(window, numberCountry):
#     CleanUp(window)
#     someframe = Frame(window, bg=bg)
#     someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
#     frameCountry = Frame(window, bg=bg)
#     frameCountry.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
#     Country = Label(frameCountry, text=f" {listOfCountries[numberCountry].name}", font=("TimesNewRoman", 25),
#                     bg=bg)
#     Country.pack()
#
#     frameBack = Frame(window, bg=bg)
#     frameBack.place(relx=0.15, rely=0.12 + 0.12 * 6, relwidth=0.7, relheight=1 / 9)
#     back = Button(frameBack, text="Назад", font=("TimesNewRoman", 19), bg=bg,
#                   command=lambda: MainVision(window))
#     back.pack()
#
#     frameBudget = Frame(window, bg=bg)
#     frameBudget.place(relx=0.03, rely=0.15, relwidth=0.27, relheight=1 / 9)
#     Budget = Label(frameBudget, text=f"Бюджет: {listOfCountries[numberCountry].budget} $",
#                    font=("TimesNewRoman", 12), bg=bg)
#     Budget.pack()
#
#     frameBombs = Frame(window, bg=bg)
#     frameBombs.place(relx=0.01, rely=0.19, relwidth=0.26, relheight=1 / 9)
#     Bombs = Label(frameBombs, text=f"Бомбы: {listOfCountries[numberCountry].bombAmountNow} шт",
#                   font=("TimesNewRoman", 12), bg=bg)
#     Bombs.pack()
#
#     frameAvgQual = Frame(window, bg=bg)
#     frameAvgQual.place(relx=0.01, rely=0.23, relwidth=0.30, relheight=1 / 9)
#     Bombs = Label(frameAvgQual, text=f"Общ. УЖ: {listOfCountries[numberCountry].avgLifeQual} %",
#                   font=("TimesNewRoman", 12), bg=bg)
#     Bombs.pack()
#
#     frameTech = Frame(window, bg=bg)
#     frameTech.place(relx=0.01, rely=0.27, relwidth=0.31, relheight=1 / 9)
#     Tech = Label(frameTech, text=f"Технология: " + YesNo(listOfCountries[numberCountry].tech),
#                  font=("TimesNewRoman", 12), bg=bg)
#     Tech.pack()
#
#     frameBombCom = Frame(window, bg=bg)
#     frameBombCom.place(relx=0.01, rely=0.31, relwidth=0.36, relheight=1 / 9)
#     Tech = Label(frameBombCom, text=f"Бомбы заказ: " + str(listOfCountries[numberCountry].bombAmountComing) + " шт",
#                  font=("TimesNewRoman", 12), bg=bg)
#     Tech.pack()
#
#     frameProfit = Frame(window, bg=bg)
#     frameProfit.place(relx=0.01, rely=0.35, relwidth=0.26, relheight=1 / 9)
#     Profit = Label(frameProfit, text=f" Доход: " + str(listOfCountries[numberCountry].payout) + " $",
#                    font=("TimesNewRoman", 12), bg=bg)
#     Profit.pack()
#
#     frameProfit = Frame(window, bg=bg)
#     frameProfit.place(relx=0.01, rely=0.39, relwidth=0.35, relheight=1 / 9)
#     Profit = Label(frameProfit, text=f"Разведчики: " + str(listOfCountries[numberCountry].scoutsHome) + " чел",
#                    font=("TimesNewRoman", 12), bg=bg)
#     Profit.pack()
#
#     leftCityVision(numberCountry)
#
#     frameOrder = Frame(window, bg=bg)
#     frameOrder.place(relx=0.1, rely=0.65, relwidth=0.45, relheight=1 / 9)
#     Order = Button(frameOrder, width=45, height=15, text="Отдать приказ", font=("Realest", 19, "bold"), bg="green",
#                    command=lambda: OrderCountry(window, numberCountry))
#     Order.pack()
# def Logs(window, number):
#     global finaleLogExplosions
#     someframe = Frame(window, bg=bg)
#     someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
#     frameRound = Frame(window, bg=bg)
#     frameRound.place(relx=0.35, rely=0.03, relwidth=0.3, relheight=1 / 9)
#     roundInit = Label(frameRound, text=f"Раунд {number+1}", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
#     roundInit.pack()
#     frameRound = Frame(window, bg=bg)
#     frameRound.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=1 / 9)
#     roundInit = Label(frameRound, text="Логи", font=("TimesNewRoman", 19, "bold"), bg="#f5f5f5")
#     roundInit.pack()
#     frameT = Frame(window, bg=bg)
#     frameT.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=1 / 9)
#     T = Button(frameT, text="Назад", font=("TimesNewRoman", 20), bg=bg,
#                command=lambda: End(window))
#     T.pack()
#     frameToward = Frame(window, bg=bg)
#     frameToward.place(relx= 0.75, rely = 0.8, relwidth=0.2, relheight=1 / 9)
#     Toward = Button(frameToward, text = "--->",font=("TimesNewRoman", 20), bg=bg, command=lambda: Logs(window, (number + 1) % (values["EndRound"]-1)))
#     Toward.pack()
#     frameToward = Frame(window, bg=bg)
#     frameToward.place(relx=0.06, rely=0.8, relwidth=0.2, relheight=1 / 9)
#     Toward = Button(frameToward, text="<---", font=("TimesNewRoman", 20), bg=bg,
#                     command=lambda: Logs(window, (number + (values["EndRound"]-2)) % (values["EndRound"]-1)))
#     Toward.pack()
#
#     deli = 0.09
#     x = 0
#     if finaleLogExplosions[number][listOfCountries[0].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[0].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 0))
#         firstCountryBtn.pack()
#         x += deli
#     if finaleLogExplosions[number][listOfCountries[1].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[1].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 1))
#         firstCountryBtn.pack()
#         x += deli
#     if finaleLogExplosions[number][listOfCountries[2].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[2].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 2))
#         firstCountryBtn.pack()
#         x += deli
#     if finaleLogExplosions[number][listOfCountries[3].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[3].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 3))
#         firstCountryBtn.pack()
#         x += deli
#     if finaleLogExplosions[number][listOfCountries[4].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[4].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 4))
#         firstCountryBtn.pack()
#         x += deli
#     if finaleLogExplosions[number][listOfCountries[5].name]:
#         frameFirst = Frame(window, bg=bg)
#         frameFirst.place(relx=0.15, rely=0.2 + x, relwidth=0.7, relheight=1 / 9)
#         firstCountryBtn = Button(frameFirst, text=listOfCountries[5].name, font=("TimesNewRoman", 15), width=20,
#                                  height=1, command=lambda: ViewLogRound(number, 5))
#         firstCountryBtn.pack()
#
# def areYouSure(window):
#     global round
#
#     someframe = Frame(window, bg=bg)
#     someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
#
#     frameRound = Frame(window, bg=bg)
#     frameRound.place(relx=0.15, rely=0.03, relwidth=0.7, relheight=1 / 9)
#
#     SureFrame = Frame(window, bg=bg)
#     SureFrame.place(relx=0.15, rely=0.12, relwidth=0.7, relheight=1 / 9)
#     Sure = Label(SureFrame, text="Вы уверены?", font=("Verdana", 20, "bold"), bg=bg)
#     Sure.pack()
#
#     YesFrame = Frame(window, bg=bg)
#     YesFrame.place(relx=0.15, rely=0.12 + 0.12 * 4, relwidth=0.7, relheight=1 / 9)
#     RoundEndBtn = Button(YesFrame, text="Да", font=("Verdana", 20, "bold"), width=10, height=7,
#                          bg="red", foreground="white", command=lambda: RoundStart(window))
#     RoundEndBtn.pack()
#
#     NoFrame = Frame(window, bg=bg)
#     NoFrame.place(relx=0.15, rely=0.12 + 0.12 * 5, relwidth=0.7, relheight=1 / 9)
#     RoundNotEndBtn = Button(NoFrame, text="Отмена", font=("Verdana", 20, "bold"), width=10, height=7,
#                             command=lambda: MainVision(window))
#     RoundNotEndBtn.pack()
#
#     RoundFr = Frame(window, bg=bg)
#     if round != 6:
#         RoundFr.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.7, relheight=1 / 9)
#         RoundLbl = Label(RoundFr, text=f"Раунд {round} → {round + 1} ", font=("Verdana", 20), bg="#f5f5f5")
#     else:
#         RoundFr.place(relx=0.15, rely=0.12 + 0.12 * 2, relwidth=0.8, relheight=1 / 9)
#         RoundLbl = Label(RoundFr, text=f"Раунд {round} → конец игры ", font=("Verdana", 20), bg="#f5f5f5")
#     RoundLbl.pack()
#
# def End(window):
#     global listOfCountries
#     listOfWinners = [x for x in range(len(listOfCountries))]
#     listOfWinners = sorted(listOfWinners, key=lambda x: -listOfCountries[x].avgLifeQual)
#     someframe = Frame(window, bg=bg)
#     someframe.place(relx=0, rely=0, relwidth=1, relheight=1)
#
#     frameOver = Frame(window, bg=bg)
#     frameOver.place(relx=0.15, rely=0.05, relwidth=0.7, relheight= 1 / 9)
#     Over = Label(frameOver, text = "GAME OVER", font=("TimesNewRoman", 25, "bold"), bg=bg)
#     Over.pack()
#
#     frameBack = Frame(window, bg=bg)
#     frameBack.place(relx=0.15, rely=0.16 + 0.12 * 6, relwidth=0.7, relheight=1 / 8)
#     back = Button(frameBack, text="Логи", font=("TimesNewRoman", 19), bg=bg,
#                   command=lambda: Logs(window, 0))
#     back.pack()
#
#     frameTabl = Frame(window, bg=bg)
#     frameTabl.place(relx=0.01, rely=0.18, relwidth=0.2, relheight=1 / 9)
#     Tabl = Label(frameTabl, text="Место", font=("TimesNewRoman", 15), bg=bg)
#     Tabl.pack()
#
#     frameTabl = Frame(window, bg=bg)
#     frameTabl.place(relx=0.29, rely=0.18, relwidth=0.2, relheight=1 / 9)
#     Tabl = Label(frameTabl, text="Страна", font=("TimesNewRoman", 15), bg=bg)
#     Tabl.pack()
#     x = 0
#     y = 0
#     for i in range(1, 7):
#         frameTabl = Frame(window, bg=bg)
#         frameTabl.place(relx=0.18, rely=0.28 + y, relwidth=0.45, relheight=1 / 9)
#         Tabl = Label(frameTabl, text=listOfCountries[listOfWinners[i-1]].name +" ("+ str(listOfCountries[listOfWinners[i-1]].avgLifeQual)+"%)", font=("TimesNewRoman", 15, "bold"), bg=bg)
#         Tabl.pack()
#         y += 0.07
#         frameTabl = Frame(window, bg=bg)
#         frameTabl.place(relx=0.01, rely=0.28 + x, relwidth=0.2, relheight=1 / 9)
#         Tabl = Label(frameTabl, text=str(i), font=("TimesNewRoman", 15), bg=bg)
#         Tabl.pack()
#         x+= 0.07
#
