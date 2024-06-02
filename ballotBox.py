class BallotBox:
    def __init__(self):
        self.allVotes = []

    def AddVote(self, ballotReciept):
        self.allVotes.append(ballotReciept)
