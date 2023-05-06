# *********************************************
# * @Date: 2023-05-03 20:47:08
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 13:44:27
# * @FilePath: /Arithmetic/Logic/MixedOPQuestionMaker.py
# * @Description:
# *********************************************
from enum import Enum
from Interface.AbsQuestionMaker import AbsQuestionMaker
from Tools.MathTools import MathTools
from Tools.StringTools import StringTools


# *********************************************
# * @description: 数式のテンプレートEnum
# * @Date: 2023-05-05 20:17:27
# *********************************************
class TemplateEnum(Enum):
    TEMP1 = '({} + {}) * {}'
    TEMP2 = '({} - {}) * {}'
    TEMP3 = '{} + {} - {}'


class MixedOPQuestionMaker(AbsQuestionMaker):
    def __init__(self) -> None:
        super().__init__()

    # *********************************************
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 作成する数式の数量
    # *********************************************
    def setParams(self, *args, **kwargs) -> None:
        self.resRange = kwargs['resRange']
        self.quantity = kwargs['quantity']

    # *********************************************
    # * @param {TemplateEnum} template: 数式のテンプレート
    # * @param {list[int]} digits: 各計算因子の桁数
    # *********************************************
    def makeQuestions(self, *args, **kwargs) -> None:
        template = kwargs['template']
        digits = kwargs['digits']
        while True:
            # 各計算因子の生成
            lstNum = [MathTools.getRandomInt(d) for d in digits]
            # 結果計算
            result = eval(template.value.format(*lstNum))
            # 結果は範囲内の場合、数式を作成する
            if self.resRange[0] < result < self.resRange[1]:
                # 数式の作成
                formula = self.getFormula(template=template, numList=lstNum)
                self.questions.append(formula)
                self.answers.append(formula + str(result))
                # 所定数量に達したらループから脱出
                if len(self.questions) == self.quantity:
                    return None

    # *********************************************
    # * @param {TemplateEnum} template: 数式のテンプレート
    # * @param {list[int]} numList: 数字リスト
    # * @return {str}: 数式文字列
    # *********************************************
    def getFormula(self, *args, **kwargs) -> str:
        template = kwargs['template']
        lstNum = kwargs['numList']
        return StringTools.getFormulaMixed(template, lstNum)


# テスト用
if __name__ == "__main__":
    params = {'resRange': [0, 100], 'quantity': 50}
    ins = MixedOPQuestionMaker()
    ins.setParams(**params)
    ins.makeQuestions(template=TemplateEnum.TEMP3, digits=[2, 1, 1])
    print(ins.answers)
