# *********************************************
# * @Date: 2023-05-08 20:03:35
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-10 13:57:02
# * @FilePath: /Arithmetic/Entity/Factors.py
# * @Description:
# *********************************************
class FactorUnit:
    def __init__(self, *args, **kwargs) -> None:
        self.intDigits: int = int(kwargs['intDigits'])
        self.decimalPlaces: int = int(kwargs['decimalPlaces'])
        self.allowZero: bool = eval(kwargs['allowZero'])
        self.allowOne: bool = eval(kwargs['allowOne'])


class Factor:
    def __init__(self, *args, **kwargs) -> None:
        self.__elementList: list[FactorUnit] = []
        self.name: str = kwargs['name']
        self.description: str = kwargs['description']
        self.addElements(kwargs['elementList'])

    def addElements(self, eList: list):
        self.__elementList.extend([FactorUnit(**e) for e in eList])

    @property
    def numOfElements(self):
        return len(self.__elementList)
    
    @property
    def elementList(self):
        return self.__elementList


class FactorCollection:
    def __init__(self, *args, **kwargs) -> None:
        self.__factorList = []

    def addFactor(self, factor: Factor) -> None:
        self.__factorList.append(factor)

    def addFactors(self, factors: list[Factor]) -> None:
        self.__factorList.extend(factors)

    def getFactorByNames(self, names: list[str]) -> list[Factor]:
        return [f for f in self.__factorList if f.name in names]