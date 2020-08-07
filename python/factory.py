# Creational
# Factory
# Uncertainties in the types of objects
# Decisions to be made at the runtime
# ex:Pet shop used to sell dogs originally, now the want to sell cats too.

from abc import ABCMeta, abstractclassmethod
class IChair():
    @abstractclassmethod
    def get_dimensions():
        "The chiar interface"
        


class BigChair(IChair):

    def __init__(self):
        self.h=30
        self.w=30
        self.d=30
    
    def get_dimensions(self):
        return {"height":self.h, "width":self.w, "depth": self.d}

class smallchair(IChair):

    def __init__(self):
        self.h=10
        self.w=10
        self.d=10
    
    def get_dimensions(self):
        return {"height":self.h, "width":self.w, "depth": self.d}

class ChairFactory():
    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype=="bigchair":
                return BigChair()
            elif chairtype=="smallchair":
                return smallchair()
            else:
                raise AssertionError("chair not found")
        except AssertionError as e:
            print(e)

if __name__=="__main__":
    chair=ChairFactory.get_chair("bigchair")
    print(chair.get_dimensions())
    chair=ChairFactory.get_chair("smallchair")
    print(chair.get_dimensions())

    




