from voters import createVoters
from parties import createParties
from buildWebsite import buildWebsite
from voteComputer import VoteComputer
from usbStick import Usb
from ballotBox import BallotBox
from scanner import Scanner
from chipcard import Chipcard 
from votingconsole import VotingConsole
import votingProcess
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

votecomputers = [VoteComputer(), VoteComputer(), VoteComputer()]

for votecomputer in votecomputers:
    votecomputer.turnOn(usb.usbCode)


ballotBox = BallotBox()
scanner = Scanner()


votingprocess = votingProcess.VotingProcess(voters.votersList, votecomputers, parties, ballotBox, scanner)
votingprocess.startVoteProcess()

for votecomputer in votecomputers:
    votecomputer.turnOff(usb.usbCode)


console = VotingConsole(ballotBox.allVotes, 50)

#!!!!! uncomment voor de terminal info van het stemmen !!!!! 

# print(console.RawResults())
console.votingReciepts()
console.FinalResults()
votingprocess.checkCounts()


buildWebsite(console.RawResults())
