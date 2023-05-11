# & *********************************************
# & @Date: 2023-05-03 20:13:27
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 15:48:36
# & @FilePath: /Arithmetic/Tools/StringTools.py
# & @Description: 文字列に関するツールクラス
# & *********************************************
from Enums.OperatorEnum import OpEnum as OPR


class StringTools:

    # オペレーター符号取替用
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
    # * @description: 数字とオペレータで数式作成
    # * @param {list[int]} nums: 数字リスト
    # * @param {list[str]} oprs: オペレータリスト
    # * @return {str}: 数式文字列
    # *********************************************
    @classmethod
    def getFormulaSample(cls, nums: list[int], oprs: list[str]) -> str:
        formula = str(nums[0])
        for i in range(1, len(nums)):
            formula += OPR.BLANK.value + str(oprs[i - 1]) + \
                                        OPR.BLANK.value + str(nums[i])
        formula += OPR.BLANK.value + OPR.EQUALS.value + OPR.BLANK.value
        return cls.__replaceOperator(formula)

    # *********************************************
    # * @description: フォーマットで数式作成
    # * @param {str} format: フォーマット
    # * @param {list[int]} nums: 数字リスト
    # * @return {str}: 数式文字列
    # *********************************************
    @classmethod
    def getFormulaFromTEMP(cls, format: str, nums: list) -> str:
        formula = format.format(*nums) + OPR.BLANK.value + \
                                        OPR.EQUALS.value + OPR.BLANK.value
        return cls.__replaceOperator(formula)

    # *********************************************
    # * @description: オペレーター符号取替
    # * @param {str} formula: 数式文字列
    # * @return {str}: 数式文字列
    # *********************************************
    @classmethod
    def __replaceOperator(cls, formula: str) -> str:
        transTable = formula.maketrans(cls.OPR_MAPPING_DIC)
        formula = formula.translate(transTable)
        return formula


# テスト用
if __name__ == "__main__":
    f = '(a + b) * c = d'
    print(StringTools.__replaceOperator(f))
