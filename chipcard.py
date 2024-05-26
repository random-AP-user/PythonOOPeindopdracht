import uuid

class Chipcard:
    def __init__(self):
        self.code  = None
        self.chipID = str(uuid.uuid4())
        self.ballotReciept = None
        self.hasVoted = False
    def initialize(self,code):
        self.code = code
    def makeFresh(self):
        self.code = None
    def __repr__(self) -> str:
        return self.chipID