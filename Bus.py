# *********************************************
# * @Date: 2023-04-19 12:32:12
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-10 13:55:52
# * @FilePath: /Arithmetic/Bus.py
# * @Description:
# *********************************************
import random
from IO.SettingLoader import SettingLoader
from IO.OutPutter import OutputDocx
from Entity import Templates, Factors
from Logic.IntQuestionMaker import IntQuestionMaker


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
        resRange: list[int] = kwargs['resRange']
        quantity: int = kwargs['quantity']
        paramIQM = {'resRange': resRange, 'quantity': quantity}
        insIQM = IntQuestionMaker(**paramIQM)
        lstTemplate = self.templateCollection.getTemplateByLevels(lstLevel)
        lstFactor = self.factorCollection.getFactorByNames(
            [t.name for t in lstTemplate])
        paramQ = {'templates': lstTemplate, 'factors': lstFactor}
        insIQM.getQuestions(**paramQ)
        for a in insIQM.answers:
            print(a)


# テスト用
if __name__ == "__main__":
    bus = Bus()
    bus.loadTemplates()
    bus.loadFactors()
    bus.getIntQuestionsByLevel(**{
        'levels': [1, 1],
        'resRange': [0, 100],
        'quantity': 50
    })
    # print(bus)