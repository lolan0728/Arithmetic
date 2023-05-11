# & *********************************************
# & @Date: 2023-05-06 17:13:45
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 15:32:09
# & @FilePath: /Arithmetic/Entity/Templates.py
# & @Description:
# & *********************************************


# *********************************************
# * @description: 数式のテンプレート
# *********************************************
class Template:

    # *********************************************
    # * @description: 初期化
    # * @param {str} name: ネーム
    # * @param {str} format: 数式テンプレート
    # * @param {str} numOfFactors: 数字の個数
    # * @param {str} level: 難易度
    # *********************************************
    def __init__(self, name: str, format: str, numOfFactors: str, level: str,
                 description: str) -> None:
        self.name = name
        self.format = format
        self.numOfFactors = int(numOfFactors)
        self.level = int(level)
        self.description = description


# *********************************************
# * @description: 全て数式のテンプレート部分のセット
# *********************************************
class TemplateCollection:
    def __init__(self) -> None:
        self.__templateList = []

    # *********************************************
    # * @description: テンプレート個別追加
    # * @param {Template} template: テンプレート
    # *********************************************
    def addTemplate(self, template: Template) -> None:
        self.__templateList.append(template)

    # *********************************************
    # * @description: テンプレート個別追加
    # * @param {list[Template]} templates: テンプレートリスト
    # *********************************************
    def addTemplates(self, templates: list[Template]) -> None:
        self.__templateList.extend(templates)

    # *********************************************
    # * @description: ネームリストよりテンプレートリスト取得
    # * @param {list[str]} names: ネームリスト
    # * @return {list[Template]}: テンプレートリスト
    # *********************************************
    def getTemplateByNames(self, names: list[str]) -> list[Template]:
        return [t for t in self.__templateList if t.name in names]

    # *********************************************
    # * @description: Levelリストよりテンプレートリスト取得
    # * @param {list[int]} levels: ネームリスト
    # * @return {list[Template]}: テンプレートリスト
    # *********************************************
    def getTemplateByLevels(self, levels: list[int]) -> list[Template]:
        return [t for t in self.__templateList if t.level in levels]