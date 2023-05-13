# & *********************************************
# & @Date: 2023-05-03 20:47:08
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-12 21:54:38
# & @FilePath: /Arithmetic/Logic/IntQuestionMaker.py
# & @Description:
# & *********************************************
import copy
import random
from Entity.Factors import Factor
from Entity.Templates import Template
from Interface.AbsQuestionMaker import AbsQuestionMaker
from Tools.MathTools import MathTools
from Tools.StringTools import StringTools


# *********************************************
# * @description: 整数数式作成クラス
# *********************************************
class IntQuestionMaker(AbsQuestionMaker):

    # 数式
    _questions = []
    # 結果つき数式
    _answers = []

    # *********************************************
    # * @description: 初期化
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 数式の数量
    # *********************************************
    def __init__(self,
                 resRange: list[int] = None,
                 quantity: int = None) -> None:
        super().__init__()
        # パラメーター設定
        self.setParams(resRange, quantity)

    # *********************************************
    # * @description: パラメーター設定
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 数式の数量
    # *********************************************
    def setParams(self, resRange: list[int], quantity: int) -> None:
        self.resRange = resRange
        self.quantity = quantity

    # *********************************************
    # * @description: 複数数式作成
    # * @param {list[Template]} templates: テンプレートリスト
    # * @param {list[Factor]} factors: Factorリスト
    # *********************************************
    def getQuestions(self, templates: list[Template],
                     factors: list[Factor]) -> None:
        for _ in range(self.quantity):
            # ランダムにテンプレート1つ取得
            template = random.choice(templates)
            # ランダムにテンプレートに適用Factor1つ取得
            factor = random.choice(
                [f for f in factors if f.name == template.name])
            formula, answer = self.__createQuestion(template, factor)
            self._questions.append(formula)
            self._answers.append(answer)

    # *********************************************
    # * @description: 数式作成
    # * @param {Template} template: テンプレート
    # * @param {Factor} factor: Factor
    # * @return {tuple[str, str]}: 数式、結果つき数式
    # *********************************************
    def __createQuestion(self, template: Template,
                         factor: Factor) -> tuple[str, str]:
        while True:
            # 各数字作成
            lstNum = [MathTools.getElement(f) for f in factor.elementList]
            try:
                # 計算
                result = eval(template.format.format(*lstNum))
            # ゼロ除算エラーキャッチ
            except ZeroDivisionError:
                continue
            # 結果は範囲内＋整数の場合、数式を作成する
            if self.resRange[0] < result < self.resRange[1] and result % 1 == 0:
                # 数式
                formula = self.getFormula(template.format, lstNum)
                # 結果つき数式
                answer = formula + str(int(result))
                return formula, answer

    # *********************************************
    # * @param {str} format: フォーマット
    # * @param {list[int]} nums: 数字リスト
    # * @return {str}: 数式の文字列
    # *********************************************
    def getFormula(self, format: str, nums: list[int]) -> str:
        return StringTools.getFormulaFromTEMP(format, nums)

    # *********************************************
    # * @description: 数式リスト取得
    # * @return {list[str]}: 数式リスト(DeepCopy)
    # * @comments: プロパティメソード
    # *********************************************
    @property
    def questions(self):
        return copy.deepcopy(self._questions)

    # *********************************************
    # * @description: 結果つき数式リスト取得
    # * @return {list[str]}: 結果つき数式リスト(DeepCopy)
    # * @comments: プロパティメソード
    # *********************************************
    @property
    def answers(self):
        return copy.deepcopy(self._answers)


# テスト用
if __name__ == "__main__":
    ins = IntQuestionMaker()
    lst = ins.questions
    lst.append('aaa')
    print(ins._questions)
