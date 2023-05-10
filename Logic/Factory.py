# *********************************************
# * @Date: 2023-05-03 21:07:48
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-09 13:17:27
# * @FilePath: /Arithmetic/Logic/Factory.py
# * @Description:
# *********************************************
import importlib
from Interface.AbsQuestionMaker import AbsQuestionMaker
from Logic.IntQuestionMaker import TemplateEnum
from IO.SettingLoader import SettingLoader


class ClassFactory:

    # 类名:类对象 字典
    __classDict = {}

    # 传入子类的类型，获得实例
    @classmethod
    def instance(cls, clsType, *args, **kwargs):
        return cls.__classDict[clsType](*args, **kwargs)

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
    params = {'resRange': [0, 100], 'quantity': 50}
    ins = ClassFactory.instance('TEMPLATE', **params)
    ins.makeQuestions(template=TemplateEnum.TEMP_SIM_1, digits=[2, 1, 1])
    print(ins.answers)