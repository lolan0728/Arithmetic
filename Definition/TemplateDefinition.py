# *********************************************
# * @Date: 2023-05-06 17:13:45
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-07 10:46:14
# * @FilePath: /Arithmetic/Definition/TemplateDefinition.py
# * @Description:
# *********************************************
class Factor:
    def __init__(self, *args, **kwargs) -> None:
        self.allowOne = kwargs['allowOne']
        self.allowZero = kwargs['allowZero']


class TemplateDefinition:
    def __init__(self, *args, **kwargs) -> None:
        self.level = kwargs['level']
        self.format = kwargs['format']
        self.factors = kwargs['factors']
        self.sample = kwargs['sample']