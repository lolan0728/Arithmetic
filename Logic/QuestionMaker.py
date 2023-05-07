# *********************************************
# * @Date: 2023-05-03 20:47:08
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 21:37:13
# * @FilePath: /Arithmetic/Logic/QuestionMaker.py
# * @Description: テンプレートより数式作成
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
    # level 1
    TEMP_SIM_1 = '{} + {}'
    TEMP_SIM_2 = '{} - {}'

    # level 2
    TEMP_SIM_3 = '{} + {} + {}'
    TEMP_SIM_4 = '{} - {} - {}'
    TEMP_SIM_5 = '{} + {} - {}'
    TEMP_SIM_6 = '{} - {} + {}'

    # level 3
    TEMP_ADV_1 = '{} * {}'
    TEMP_ADV_2 = '{} / {}'

    # level 4
    TEMP_ADV_3 = '{} * {} * {}'
    TEMP_ADV_4 = '{} / {} / {}'
    TEMP_ADV_5 = '{} * {} / {}'
    TEMP_ADV_6 = '{} / {} * {}'

    # level 5
    TEMP_MIX_5 = '{} + {} * {}'
    TEMP_MIX_6 = '{} + {} / {}'

    # level 6
    TEMP_MIX_1 = '({} + {}) * {}'
    TEMP_MIX_2 = '({} - {}) * {}'
    TEMP_MIX_3 = '({} + {}) / {}'
    TEMP_MIX_4 = '({} - {}) / {}'

    # level 7
    TEMP_MIX_7 = '({} + {}) * ({} + {})'
    TEMP_MIX_8 = '({} + {}) / ({} + {})'
    TEMP_MIX_9 = '({} - {}) * ({} + {})'
    TEMP_MIX_10 = '({} - {}) * ({} - {})'
    TEMP_MIX_11 = '({} + {} + {}) * {}'
    TEMP_MIX_12 = '({} + {} - {}) * {}'
    TEMP_MIX_13 = '({} - {} - {}) * {}'
    TEMP_MIX_14 = '({} - {} + {}) * {}'
    TEMP_MIX_15 = '({} + {} + {}) / {}'
    TEMP_MIX_16 = '({} - {} - {}) / {}'


class QuestionMaker(AbsQuestionMaker):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.setParams(*args, **kwargs)

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
            if self.resRange[0] < result < self.resRange[1] and result % 1 == 0:
                # 数式の作成
                formula = self.getFormula(template=template, numList=lstNum)
                self.questions.append(formula)
                self.answers.append(formula + str(int(result)))
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
    ins = QuestionMaker(**params)
    # ins.setParams(**params)
    ins.makeQuestions(template=TemplateEnum.TEMP_ADV_2, digits=[2, 1])
    print(ins.answers)
