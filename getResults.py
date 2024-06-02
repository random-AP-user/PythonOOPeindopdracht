from collections import Counter


class GetResults:
    def __init__(self, allVotes):
        self.allVotes = allVotes

    def getScores(self, totalSeats):
        partyVotes = [chipcard["votedParty"] for chipcard in self.allVotes]
        partyCounts = Counter(partyVotes)
        rankedParties = sorted(partyCounts.items(), key=lambda x: x[1], reverse=True)

        totalVotes = sum(partyCounts.values())

        results = []
        for party, votes in rankedParties:
            seats = round((votes / totalVotes) * totalSeats)

            preferenceVotes = []
            for vote in self.allVotes:
                if vote["votedParty"] == party:
                    preferenceVotes.extend(vote["CandidatesPreference"])

            preferenceCounts = Counter(preferenceVotes).items()

            rankedCandidates = sorted(preferenceCounts, key=lambda x: (x[0].rank, x[1]), reverse=True)

            candidates = []
            amountCandidates = len(rankedCandidates)
            for seat in range(seats):
                if seat < amountCandidates:
                    candidateData = {
                        "candidate": rankedCandidates[seat % amountCandidates][0].name,
                        "votes": rankedCandidates[seat % amountCandidates][1],
                        "totalRank": rankedCandidates[seat % amountCandidates][0].rank
                        + rankedCandidates[seat % 10][1],
                        "seats": 1,
                    }
                    candidates.append(candidateData)
                else:
                    candidates[seat % amountCandidates]["seats"] += 1

            results.append(
                {"name": party, "seats": seats, "chosencandidates": candidates}
            )

        return results
