from collections import Counter
import json

class GetResults:
    def __init__(self, allVotes):
        self.allVotes = allVotes
    
    def getScores(self):
        partyVotes = [chipcard['votedParty'] for chipcard in self.allVotes]
        partyCounts = Counter(partyVotes)
        rankedParties = sorted(partyCounts.items(), key=lambda x: x[1], reverse=True)
        ranking = []
        for (party, votes) in rankedParties:
            partyData = {
                "party": party.name,
                "votes": votes,
                "candidates": []
            }
            candidateVotes = []
            for vote in self.allVotes:
                if vote['votedParty'] == party:
                    candidateVotes.extend([candidate for candidate in vote['CandidatesPreference']])

            candidateCounts = Counter(candidateVotes)
            rankedCandidates = sorted(candidateCounts.items(), key=lambda x: (x[0].rank), reverse=True)
            for (candidate, rank) in rankedCandidates:
                candidateData = {
                    "name": candidate.name,
                    "totalRank": candidate.rank + rank,
                    "votes": rank
                }
                partyData["candidates"].append(candidateData)
            
            ranking.append(partyData)

        with open('./json/output.json', 'w') as f:
            json.dump(ranking, f)

    def getVotes(self):
        for ballotReciept in self.allVotes:
            if ballotReciept['CandidatesPreference']:
                candidates_str = f"the candidates {', '.join(candidate.name for candidate in ballotReciept['CandidatesPreference'])}"
            else:
                candidates_str = "no one"
            print(f"{ballotReciept['voter']} voted for {ballotReciept['votedParty']} and preferces {candidates_str}.")