import random
import hashlib

class VoteComputer:
    Votecount = 0

    def __init__(self):
        self.state = False

    def turnOn(self, code):
        if validateUSB(code) == True:
            self.state = True
            print("PC turned on")

    def turnOff(self, code):
        if validateUSB(code) == True:
            self.state = False
            print("PC turned off")
    
    def startVote(self, parties, chipcard):
            if chipcard.hasVoted == False:
                self.vote(chipcard, parties)
                ballotPrinter = BallotPrinter()
                return ballotPrinter.ProcesData(self.chipcard, self.party, self.candidates)
            else:
                print("Voter has already made changes, so print the old reciept back")
                return chipcard.ballotReciept

    def vote(self, chipcard, parties):
        self.Votecount += 1
        
        self.candidates = []
        
        # normally random.choice(parties.partiesList) is fine but i wanted chaos
        chosenParty = parties.partiesList[1] if random.randint(0,4) == 0 else random.choice(parties.partiesList)
        for candidate in chosenParty.candidatesList:
            if random.randint(0, 10) == 0:
                self.candidates.append(candidate)
        
        self.chipcard = chipcard
        self.party = chosenParty
        chipcard.hasVoted = True

class BallotPrinter:
    def __init__(self):
        self.chipcard = None
        self.votedParty = None
        self.CandidatesPreference = None

    def ProcesData(self, chipcard, party, candidates):
        self.chipcard = chipcard
        self.votedParty = party
        self.CandidatesPreference = candidates
        return {
            "BallodID" : generateID(chipcard.chipID),
            "chipCard": self.chipcard.chipID,
            "votedParty": self.votedParty,
            "CandidatesPreference": self.CandidatesPreference,
        }

def validateUSB(code):
    secretcode = "testcode"
    if secretcode == code:
        return True
    else:
        False


def generateID(UUID):
    key = "ec8c148e6a99f7989fae09d571c53cfc99d63266fb41a19d2e39c51ddfa06492"
    return hashlib.sha256(UUID.encode() + key.encode()).hexdigest()
