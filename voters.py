import json
import uuid

class Voter:
    def __init__(self, person):
        self.UUID = str(uuid.uuid4())
        self.firstName = person["firstName"]
        self.lastName = person["lastName"]
        self.age = person["age"]
        self.hasVoted = False

    def __repr__(self):
        return f"{self.firstName} {self.lastName}"

class Voters:
    def __init__(self):
        self.votersList = []

    def addVoter(self, voter):
        self.votersList.append(voter)


# inisialize voter creation
def createVoters():
    peopleList = []
    with open('./json/votersList.json') as f:
        data = json.load(f)
        for item in data:
            peopleList.append(item)

    voters = Voters()
    for person in peopleList:
        voter = Voter(person)
        voters.addVoter(voter)

    return voters

createVoters()