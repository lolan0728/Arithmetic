# *********************************************
# * @Date: 2023-05-03 20:47:08
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-10 11:09:25
# * @FilePath: /Arithmetic/Logic/IntQuestionMaker.py
# * @Description: テンプレートより数式作成
# *********************************************
import random
from enum import Enum
from Entity.Factors import Factor
from Entity.Templates import Template
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


class IntQuestionMaker(AbsQuestionMaker):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.setParams(*args, **kwargs)

    # *********************************************
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 作成する数式の数量
    # *********************************************
    def setParams(self, *args, **kwargs) -> None:
        self.resRange: list[int] = kwargs['resRange']
        self.quantity: int = kwargs['quantity']

    # *********************************************
    # * @param {TemplateEnum} template: 数式のテンプレート
    # * @param {list[int]} digits: 各計算因子の桁数
    # *********************************************
    def makeQuestion(self, *args, **kwargs) -> None:
        template: Template = kwargs['template']
        factor: Factor = kwargs['factor']
        while True:
            # 各計算因子の生成
            lstNum = [MathTools.getFactor(f) for f in factor.elementList]
            # 結果計算
            try:
                result = eval(template.format.format(*lstNum))
            except ZeroDivisionError:
                continue
            # 結果は範囲内の場合、数式を作成する
            if self.resRange[0] < result < self.resRange[1] and result % 1 == 0:
                # 数式の作成
                formula = self.getFormula(format=template.format,
                                          numList=lstNum)
                answer = formula + str(int(result))
                return formula, answer
                # self.questions.append(formula)
                # self.answers.append(formula + str(int(result)))
                # # 所定数量に達したらループから脱出
                # if len(self.questions) == self.quantity:
                #     return None
    
    def getQuestions(self, *args, **kwargs):
        lstTemplate: list[Template] = kwargs['templates']
        lstFactor: list[Factor] = kwargs['factors']
        for _ in range(self.quantity):
            template = random.choice(lstTemplate)
            factor = random.choice([f for f in lstFactor if f.name == template.name])
            param = {'template': template, 'factor': factor}
            formula, answer = self.makeQuestion(**param)
            self.questions.append(formula)
            self.answers.append(answer)

    # *********************************************
    # * @param {TemplateEnum} template: 数式のテンプレート
    # * @param {list[int]} numList: 数字リスト
    # * @return {str}: 数式文字列
    # *********************************************
    def getFormula(self, *args, **kwargs) -> str:
        format: str = kwargs['format']
        lstNum: list[int] = kwargs['numList']
        return StringTools.getFormulaMixed(format, lstNum)


# テスト用
if __name__ == "__main__":
    pass
    # qParams = {'resRange': [0, 100], 'quantity': 500}
    # ins = IntQuestionMaker(**qParams)
    # tParams = {
    #     'name': '',
    #     'format': '({} + {}) / {}',
    #     'numOfFactors': '3',
    #     'level': '7',
    #     'description': '(a+b)/c'
    # }
    # t = Template(**tParams)
    # fParams = {
    #   "name": "simple1",
    #   "description": "a+b",
    #   "factorList": [
    #     {
    #       "intDigits": "2",
    #       "decimalPlaces": "0",
    #       "allowZero": "False",
    #       "allowOne": "True"
    #     },
    #     {
    #       "intDigits": "2",
    #       "decimalPlaces": "0",
    #       "allowZero": "False",
    #       "allowOne": "True"
    #     },
    #     {
    #       "intDigits": "2",
    #       "decimalPlaces": "0",
    #       "allowZero": "False",
    #       "allowOne": "True"
    #     }
    #   ]
    # }
    # lstFactor = []
    # lstFactor.append(Factors(**fParams))
    # ins.makeQuestions(template=t, factors=lstFactor)
    # print(ins.answers)
