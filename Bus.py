# & *********************************************
# & @Date: 2023-04-19 12:32:12
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 19:29:05
# & @FilePath: /Arithmetic/Bus.py
# & @Description:
# & *********************************************
from Entity import Templates, Factors
from Logic.IntQuestionMaker import IntQuestionMaker
from IO.SettingLoader import SettingLoader
from IO.OutPutter import OutputDocx


class Bus:
    def __init__(self) -> None:
        # テンプレートセット
        self.templateCollection = Templates.TemplateCollection()
        # Factorセット
        self.factorCollection = Factors.FactorCollection()

    # *********************************************
    # * @description: 定義ファイルからテンプレート情報読込
    # *********************************************
    def loadTemplates(self) -> None:
        self.templateCollection.addTemplates([
            Templates.Template(**t)
            for t in list(SettingLoader.loadTemplates())
        ])

    # *********************************************
    # * @description: 定義ファイルからactor情報読込
    # *********************************************
    def loadFactors(self) -> None:
        self.factorCollection.addFactors(
            [Factors.Factor(**f) for f in list(SettingLoader.loadFactors())])

    # *********************************************
    # * @description: レベルリストより数式作成
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 数式の数量
    # * @param {list[int]} levels: レベルリスト
    # * @return {tuple[list[str], list[str]]}: 数式リスト、結果つき数式リスト
    # *********************************************
    def getIntQuestionsByLevel(
            self, resRange: list[int], quantity: int,
            levels: list[int]) -> tuple[list[str], list[str]]:
        # Levelリストよりテンプレートリスト取得
        lstTemplate = self.templateCollection.getTemplateByLevels(levels)
        return self.__getIntQuestions(resRange, quantity, lstTemplate)

    # *********************************************
    # * @description: ネームリストより数式作成
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 数式の数量
    # * @param {list[int]} levels: レベルリスト
    # * @return {tuple[list[str], list[str]]}: 数式、結果つき数式のリスト
    # *********************************************
    def getIntQuestionsByNames(
            self, resRange: list[int], quantity: int,
            names: list[str]) -> tuple[list[str], list[str]]:
        # ネームリストよりテンプレートリスト取得
        lstTemplate = self.templateCollection.getTemplateByNames(names)
        return self.__getIntQuestions(resRange, quantity, lstTemplate)

    # *********************************************
    # * @description: テンプレートリストより数式作成
    # * @param {list[int]} resRange: 結果の範囲
    # * @param {int} quantity: 数式の数量
    # * @param {list[Templates.Template]} templates: テンプレートリスト
    # * @return {tuple[list[str], list[str]]}: 数式、結果つき数式のリスト
    # *********************************************
    def __getIntQuestions(
            self, resRange: list[int], quantity: int,
            templates: list[Templates.Template]
    ) -> tuple[list[str], list[str]]:
        # ネームリストよりFactorリスト取得
        lstFactor = self.factorCollection.getFactorByNames(
            [t.name for t in templates])
        insIQM = IntQuestionMaker(resRange, quantity)
        # 複数数式作成
        insIQM.getQuestions(templates, lstFactor)
        return insIQM.questions, insIQM.answers


# テスト用
if __name__ == "__main__":
    bus = Bus()
    bus.loadTemplates()
    bus.loadFactors()
    lsrQ, lstA = bus.getIntQuestionsByNames(**{
        'names': ['simple1', 'simple1'],
        'resRange': [0, 100],
        'quantity': 50
    })
    print(lstA)
    # print(bus)