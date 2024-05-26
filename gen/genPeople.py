import random

class GenPeople:
    firstNames = [
        "Jan",
        "Anna",
        "Pieter",
        "Sophie",
        "Hendrik",
        "Emma",
        "Willem",
        "Lotte",
        "Johannes",
        "Eva",
        "Maarten",
        "Femke",
        "Dirk",
        "Julia",
        "Cornelis",
        "Amber",
        "Gerard",
        "Lisa",
        "Petra",
        "Thijs",
        "Noah",
        "Patrik",
        "Bob",
        "Erik",
        "Miro",
        "Joey",
        "Mats",
        "Johan",
        "Bjorn",
        "Joost",
        "Maximus",
        "Sooi",
        "Kristof",
    ]

    lastNames = [
        "de Vries",
        "van der Meer",
        "Jansen",
        "van Dijk",
        "Bakker",
        "Visser",
        "van den Berg",
        "Mulder",
        "Smit",
        "Meijer",
        "de Jong",
        "van Leeuwen",
        "van der Linden",
        "Kramer",
        "Vermeer",
        "Bos",
        "Vos",
        "de wit",
        "de Graaf",
        "van der Wal",
    ]

    def __init__(self, amount):
        self.peopleList = []
        for i in range(amount):
            randomNum1 = round(random.random() * len(self.firstNames) - 1)
            randomNum2 = round(random.random() * len(self.lastNames) - 1)

            randomAge = random.randint(18, 90)

            objPerson = {
                "firstName": self.firstNames[randomNum1],
                "lastName": self.lastNames[randomNum2],
                "age": randomAge,
            }
            self.peopleList.append(objPerson)
