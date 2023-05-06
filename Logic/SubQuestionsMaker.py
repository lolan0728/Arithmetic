# *********************************************
# * @Date: 2023-04-26 16:06:30
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 10:19:55
# * @FilePath: /Arithmetic/Logic/SubQuestionsMaker.py
# * @Description:引き算
# *********************************************
from Enums.OperatorEnum import OpEnum as OPR
from Interface.AbsQuestionMaker import AbsQuestionMaker
from Tools.MathTools import MathTools
from Tools.StringTools import StringTools


class SubQuestionsMaker(AbsQuestionMaker):
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
    # * @param {list[int]} digits: 各計算因子の桁数
    # *********************************************
    def makeQuestions(self, *args, **kwargs) -> None:
        digits = kwargs['digits']
        while True:
            # 各計算因子の生成
            lstNum = [MathTools.getRandomInt(d) for d in digits]
            # 結果計算
            result = lstNum[0] - sum(lstNum[1:])
            # 結果は範囲内の場合、数式を作成する
            if self.resRange[0] < result < self.resRange[1]:
                # 当クラスは全部「-」
                lstOpr = [OPR.SUB.value] * (len(lstNum) - 1)
                # 数式の作成
                formula = self.getFormula(numList=lstNum, oprList=lstOpr)
                self.questions.append(formula)
                self.answers.append(formula + str(result))
                # 所定数量に達したらループから脱出
                if len(self.questions) == self.quantity:
                    return None

    # *********************************************
    # * @param {list[int]} numList: 数字リスト
    # * @param {list[str]} oprList: オペレータリスト
    # * @return {str}: 数式文字列
    # *********************************************
    def getFormula(self, *args, **kwargs) -> str:
        lstNum = kwargs['numList']
        lstOpr = kwargs['oprList']
        return StringTools.getFormulaSample(lstNum, lstOpr)


# テスト用
if __name__ == "__main__":
    params = {'resRange': [0, 1000], 'quantity': 50}
    ins = SubQuestionsMaker()
    ins.setParams(**params)
    ins.makeQuestions(digits=[3, 2])
    print(ins.answers)