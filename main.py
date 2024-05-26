from getResults import GetResults
from voters import createVoters
from parties import createParties
from voteComputer import VoteComputer
from usbStick import Usb
from ballotBox import BallotBox
from scanner import Scanner
from chipcard import Chipcard
import random

voters = createVoters()
parties = createParties(
    voters.votersList,
    [
        "Brotherhood of Steel",
        "Enclave",
        "Commonwealth Minutemen",
        "The railroad",
        "The Institute",
        "Yes Man"
    ]
)

usb = Usb()
votecomputer1 = VoteComputer()
votecomputer2 = VoteComputer()
votecomputer3 = VoteComputer()

votecomputer1.turnOn(usb.usbCode)
votecomputer2.turnOn(usb.usbCode)
votecomputer3.turnOn(usb.usbCode)

ballotBox = BallotBox()
scanner = Scanner()

for voter in voters.votersList:
    chipcard = Chipcard()
    chipcard.initialize('chipcardCode')
    match random.randint(0,2):
        case 0:
            chipcard.ballotReciept = votecomputer1.startVote(parties, chipcard)
        case 1:
            chipcard.ballotReciept = votecomputer2.startVote(parties, chipcard)
        case 2:
            chipcard.ballotReciept = votecomputer3.startVote(parties, chipcard)

    if scanner.validateID(chipcard.ballotReciept):        
        ballotBox.AddVote(chipcard.ballotReciept)
    chipcard.makeFresh()

if len(voters.votersList) == len(ballotBox.allVotes):
    print()
    print("Everyone voted","\n")
else: print("Inconsistent Votes")

votecomputer1.turnOff(usb.usbCode)
votecomputer2.turnOff(usb.usbCode)
votecomputer3.turnOff(usb.usbCode)


getResults = GetResults(ballotBox.allVotes)
getResults.getScores()

print()
print(f"Pc1 has {votecomputer1.Votecount} votes")
print(f"Pc2 has {votecomputer2.Votecount} votes")
print(f"Pc3 has {votecomputer3.Votecount} votes")
totalvotes = votecomputer1.Votecount + votecomputer2.Votecount + votecomputer3.Votecount
print(f"Total votes: {totalvotes}")