# & *********************************************
# & @Date: 2023-04-19 12:32:12
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 18:44:43
# & @FilePath: /Arithmetic/Bus.py
# & @Description: 
# & *********************************************
from Entity import Templates, Factors
from Logic.IntQuestionMaker import IntQuestionMaker
from IO.SettingLoader import SettingLoader
from IO.OutPutter import OutputDocx


class Bus:
    def __init__(self) -> None:
        self.templateCollection = Templates.TemplateCollection()
        self.factorCollection = Factors.FactorCollection()

    def loadTemplates(self) -> None:
        self.templateCollection.addTemplates([
            Templates.Template(**t)
            for t in list(SettingLoader.loadTemplates())
        ])

    def loadFactors(self) -> None:
        self.factorCollection.addFactors(
            [Factors.Factor(**f) for f in list(SettingLoader.loadFactors())])

    def getIntQuestionsByLevel(self, *args, **kwargs):
        lstLevel: list[int] = kwargs['levels']
        lstTemplate = self.templateCollection.getTemplateByLevels(lstLevel)
        return self.__getIntQuestions(templates=lstTemplate, **kwargs)

    def getIntQuestionsByNames(self, *args, **kwargs):
        lstName: list[str] = kwargs['names']
        lstTemplate = self.templateCollection.getTemplateByNames(lstName)
        return self.__getIntQuestions(templates=lstTemplate, **kwargs)

    def __getIntQuestions(self, *args, **kwargs):
        resRange: list[int] = kwargs['resRange']
        quantity: int = kwargs['quantity']
        lstTemplate: list[Templates.Template] = kwargs['templates']
        lstFactor = self.factorCollection.getFactorByNames(
            [t.name for t in lstTemplate])
        paramIQM = {'resRange': resRange, 'quantity': quantity}
        paramQ = {'templates': lstTemplate, 'factors': lstFactor}
        insIQM = IntQuestionMaker(**paramIQM)
        insIQM.getQuestions(**paramQ)
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