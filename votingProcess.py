
import random
from chipcard import Chipcard

class VotingProcess:
    def __init__(self, voters, votecomputers, parties, ballotBox, scanner):
        self.votecomputers = votecomputers
        self.voters = voters
        self.parties = parties
        self.ballotBox = ballotBox
        self.scanner = scanner

    def startVoteProcess(self):   
        for voter in self.voters:
                chipcard = Chipcard()
                chipcard.initialize('chipcardCode')
                selectedComputer = random.choice(self.votecomputers)
                chipcard.ballotReciept = selectedComputer.startVote(self.parties, chipcard)

                if self.scanner.validateID(chipcard.ballotReciept):        
                    self.ballotBox.AddVote(chipcard.ballotReciept)
                chipcard.makeFresh()

        if len(self.voters) == len(self.ballotBox.allVotes):
            print()
            print("Everyone voted","\n")
        else: 
            print("Inconsistent Votes")

    def checkCounts(self):
        print()
        print(f"Pc1 has {self.votecomputers[0].Votecount} votes")
        print(f"Pc2 has {self.votecomputers[1].Votecount} votes")
        print(f"Pc3 has {self.votecomputers[2].Votecount} votes")
        totalVotes = sum(computer.Votecount for computer in self.votecomputers)
        print(f"Total votes: {totalVotes}")
