# & *********************************************
# & @Date: 2023-05-08 20:03:35
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 15:33:05
# & @FilePath: /Arithmetic/Entity/Factors.py
# & @Description: 数式の数値部分に関連クラス
# & ********************************************


# *********************************************
# * @description: 単一の数字
# *********************************************
class Element:

    # *********************************************
    # * @description: 初期化
    # * @param {str} intDigits: 整数部分の桁数
    # * @param {str} decimalPlaces: 小数部分の桁数
    # * @param {str} allowZero: 0可能?　True/False
    # * @param {str} allowOne: 1可能?　True/False
    # *********************************************
    def __init__(self, intDigits: str, decimalPlaces: str, allowZero: str,
                 allowOne: str) -> None:
        self.intDigits = int(intDigits)
        self.decimalPlaces = int(decimalPlaces)
        self.allowZero = eval(allowZero)
        self.allowOne = eval(allowOne)


# *********************************************
# * @description: 数式の数値部分
# *********************************************
class Factor:

    # *********************************************
    # * @description: 初期化
    # * @param {str} name: ネーム
    # * @param {str} description: 説明
    # * @param {list[Element]} elements: 数字リスト
    # *********************************************
    def __init__(self, name: str, description: str,
                 elements: list[Element]) -> None:
        self.name = name
        self.description = description
        self.__elementList: list[Element] = []
        self.__addElements(elements)

    # *********************************************
    # * @description: 数字リストに内容追加
    # * @param {list} eList
    # *********************************************
    def __addElements(self, eList: list) -> None:
        self.__elementList.extend([Element(**e) for e in eList])

    # *********************************************
    # * @description: 数字個数取得
    # * @return {int}: 数字個数
    # * @comments: プロパティメソード
    # *********************************************
    @property
    def numOfElements(self) -> int:
        return len(self.__elementList)

    # *********************************************
    # * @description: 数字リスト取得
    # * @return {list[Element]}: 数字リスト
    # * @comments: プロパティメソード
    # *********************************************
    @property
    def elementList(self) -> list[Element]:
        return self.__elementList


# *********************************************
# * @description: 全て数式の数値部分のセット
# *********************************************
class FactorCollection:
    def __init__(self) -> None:
        self.__factorList = []

    # *********************************************
    # * @description: Factor個別追加
    # * @param {Factor} factor: Factor
    # *********************************************
    def addFactor(self, factor: Factor) -> None:
        self.__factorList.append(factor)

    # *********************************************
    # * @description: Factor一括追加
    # * @param {list[Factor]} factors: Factorリスト
    # *********************************************
    def addFactors(self, factors: list[Factor]) -> None:
        self.__factorList.extend(factors)

    # *********************************************
    # * @description: ネームリストよりFactorリスト取得
    # * @param {list[str]} names: ネームリスト
    # * @return {list[Factor]}: Factorリスト
    # *********************************************
    def getFactorByNames(self, names: list[str]) -> list[Factor]:
        return [f for f in self.__factorList if f.name in names]