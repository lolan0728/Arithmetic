# *********************************************
# * @Date: 2023-05-04 09:29:00
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 10:26:26
# * @FilePath: /Arithmetic/TestMain.py
# * @Description: 
# *********************************************
import Logic.Factory as factory


class test:
    def __init__(self) -> None:
        pass
    
    # *********************************************
    # * @description: 
    # * @param {*} self
    # * @param {list} lst
    # * @return {*}
    # * @Date: 2023-05-06 09:17:20
    # *********************************************
    def func(self, lst: list[int]):
        pass

if __name__ == '__main__':
    factory.ClassFactory.importer()
    ins = factory.ClassFactory.instance('add')
    params = {'ansRange': [0, 1000], 'digits': [3, 2], 'quantity': 50}
    ins.setParams(params)
    ins.makeQuestions()
    print(ins.answers)