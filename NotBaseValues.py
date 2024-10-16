from MainObjects import Country
from Values import MainValues
Japan = Country("Япония", "Токио", "Осака", "Нагасаки", "Кавасаки")
Latvia = Country("Латвия", "Рига", "Юрмала", "Лиепая", "Елгава")
Russia = Country("Россия", "Москва", "Омск", "Ярославль", "Владивосток")
Germany = Country("Германия", "Берлин", "Мюнхен", "Кёльн", "Гамбург")
Estonia = Country("Эстония", "Таллин", "Кохтла-Ярве", "Нарва", "Тарту")
France = Country("Франция", "Париж", "Марсель", "Лион", "Тулуза")

listOfCountries = [Japan, Latvia, Russia, Germany, Estonia, France]
values = MainValues()
finaleLogExplosions = [{country.name : [] for country in listOfCountries} for _ in range(values["EndRound"])]

blowLog = dict() # Динамические логи для раундов