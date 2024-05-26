import hashlib

class Scanner:
    def __init__(self):
        self.key = "ec8c148e6a99f7989fae09d571c53cfc99d63266fb41a19d2e39c51ddfa06492"

    def validateID(self, ballotReciept):
        UUID = ballotReciept["chipCard"]
        hashedID = ballotReciept["BallodID"]
        HashedUUID =  hashlib.sha256(UUID.encode() + self.key.encode()).hexdigest()
        if HashedUUID == hashedID:
            return True
        else:
            print("UUID doens't match")
            return False