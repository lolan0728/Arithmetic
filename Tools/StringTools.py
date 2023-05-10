# *********************************************
# * @Date: 2023-05-03 20:13:27
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-09 10:45:29
# * @FilePath: /Arithmetic/Tools/StringTools.py
# * @Description: 文字列に関するツールクラス
# *********************************************
from Enums.OperatorEnum import OpEnum as OPR


class StringTools:

    OPR_MAPPING_DIC = {
        '+': OPR.ADD.value,
        '-': OPR.SUB.value,
        '*': OPR.MULTI.value,
        '/': OPR.DIV.value,
        '(': OPR.LEFT_BRACKET.value,
        ')': OPR.RIGHT_BRACKET.value,
        '=': OPR.EQUALS.value
    }

    # *********************************************
    # * @description: 数字とオペレータを結合して数式にする
    # * @param {list[int]} numList: 数字リスト
    # * @param {list[str]} oprList: オペレータリスト
    # * @return {str}: 数式文字列
    # * @Date: 2023-05-03 20:28:51
    # *********************************************
    @classmethod
    def getFormulaSample(cls, numList: list, oprList: list) -> str:
        formula = str(numList[0])
        for i in range(1, len(numList)):
            formula += OPR.BLANK.value + str(oprList[i - 1]) + \
                                        OPR.BLANK.value + str(numList[i])
        formula += OPR.BLANK.value + OPR.EQUALS.value + OPR.BLANK.value
        return cls.__formatFormula(formula)

    # *********************************************
    # * @description: 数字とオペレータを結合して数式にする
    # * @param {list[int]} numList: 数字リスト
    # * @param {list[str]} oprList: オペレータリスト
    # * @return {str}: 数式文字列
    # * @Date: 2023-05-03 20:28:51
    # *********************************************
    @classmethod
    def getFormulaMixed(cls, template: str, numList: list) -> str:
        formula = template.format(*numList) + OPR.BLANK.value + \
                                        OPR.EQUALS.value + OPR.BLANK.value
        return cls.__formatFormula(formula)

    @classmethod
    def __formatFormula(cls, formula: str) -> str:
        transTable = formula.maketrans(cls.OPR_MAPPING_DIC)
        formula = formula.translate(transTable)
        return formula


# テスト用
if __name__ == "__main__":
    f = '(a + b) * c = d'
    print(StringTools.__formatFormula(f))
