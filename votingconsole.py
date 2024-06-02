from getResults import GetResults

class VotingConsole:
    def __init__(self, allVotes, seats):
        self.allVotes = allVotes
        self.getResults = GetResults(self.allVotes)
        self.seats = seats


    def RawResults(self):
        return self.getResults.getScores(self.seats)

    def FinalResults(self):
        for party in self.getResults.getScores(self.seats):
            print(f"{party['name']} - total seat(s): {party['seats']}:")
            for candidate in party['chosencandidates']:
                print(f"  - {candidate['candidate']}: ")
                print(f"    - {candidate['seats']} seat")
                print(f"    - {candidate['votes']} votes")
            print()

    def votingReciepts(self):
        for ballotReciept in self.allVotes:
            if ballotReciept['CandidatesPreference']:
                candidates_str = f"the candidates {', '.join(candidate.name for candidate in ballotReciept['CandidatesPreference'])}"
            else:
                candidates_str = "no one"
            print(f"{ballotReciept['chipCard']} voted for {ballotReciept['votedParty']} and preferces {candidates_str}.")
