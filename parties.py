import random
# import json

class Candidate:
    def __init__(self, canditade, rank):
        self.name = f"{canditade.firstName} {canditade.lastName}"
        self.rank = rank

    def __repr__(self):
        return f"{self.name}"

    def rankAdd(self, rank=1):
        self.rank = self.rank + rank


class Party:
    def __init__(self, name):
        self.candidatesList = []
        self.name = name

    def addCandidate(self, candidate):
        self.candidatesList.append(candidate)

    def __repr__(self):
        return self.name

    def sort_rank(self):
        self.candidatesList.sort(key=lambda x: x.rank, reverse=True)


class Parties:
    def __init__(self):
        self.partiesList = []

    def addParty(self, party):
        self.partiesList.append(party)


# inisialize party creation
def createParties(voters, partyNames):
    randCandidates = random.sample(voters, len(partyNames)*10)
    parties = Parties()
    for partyname in partyNames:
        party = Party(partyname)
        for objcandidate in randCandidates[0:10]:
            rank = round(random.randint(0,100) / 10) * 10
            candidate = Candidate(objcandidate, rank)
            party.addCandidate(candidate)
        parties.addParty(party)
    return parties
