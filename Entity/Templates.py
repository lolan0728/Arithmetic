# *********************************************
# * @Date: 2023-05-06 17:13:45
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-10 13:41:53
# * @FilePath: /Arithmetic/Entity/Templates.py
# * @Description:
# *********************************************
class Template:
    def __init__(self, *args, **kwargs) -> None:
        self.name: str = kwargs['name']
        self.format: str = kwargs['format']
        self.numOfFactors: int = int(kwargs['numOfFactors'])
        self.level: int = int(kwargs['level'])
        self.description: str = kwargs['description']


class TemplateCollection:
    def __init__(self, *args, **kwargs) -> None:
        self.__templateList = []

    def addTemplate(self, template: Template) -> None:
        self.__templateList.append(template)

    def addTemplates(self, templates: list[Template]) -> None:
        self.__templateList.extend(templates)

    def getTemplateByNames(self, names: list[str]) -> Template:
        return [t for t in self.__templateList if t.name in names]

    def getTemplateByLevels(self, levelList: list[int]) -> list[Template]:
        return [t for t in self.__templateList if t.level in levelList]