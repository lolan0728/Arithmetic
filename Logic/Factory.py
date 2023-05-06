# *********************************************
# * @Date: 2023-05-03 21:07:48
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 16:12:17
# * @FilePath: /Arithmetic/Logic/Factory.py
# * @Description:
# *********************************************
import importlib
from Interface.AbsQuestionMaker import AbsQuestionMaker
from Logic.TemplateQuestionMaker import TemplateEnum
from IO.SettingLoader import SettingLoader


class ClassFactory:

    # 类名:类对象 字典
    __classDict = {}

    # 传入子类的类型，获得实例
    @classmethod
    def instance(cls, clsType):
        return cls.__classDict[clsType]()

    # 子类注册函数
    @classmethod
    def register(cls, clsType: str, myCls: AbsQuestionMaker):
        cls.__classDict[clsType] = myCls

    @classmethod
    def importMarkerClasses(cls):
        mkList = SettingLoader.loadMakerClasses()
        for maker in mkList:
            mkModule = importlib.import_module('.', maker['module'])
            mkClass = getattr(mkModule, maker['class'])
            ClassFactory.register(maker['name'], mkClass)


# テスト用
if __name__ == "__main__":
    ClassFactory.importMarkerClasses()
    ins = ClassFactory.instance('MIXED')
    params = {'ansRange': [0, 1000], 'quantity': 50}
    ins.setParams(params)
    ins.makeQuestions(template=TemplateEnum.TEMP2, digits=[2, 1, 1])
    print(ins.answers)