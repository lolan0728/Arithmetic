# & *********************************************
# & @Date: 2023-04-26 15:18:33
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 15:51:11
# & @FilePath: /Arithmetic/Interface/AbsQuestionMaker.py
# & @Description: アブストラクト
# & *********************************************
import abc as abc


class AbsQuestionMaker(abc.ABC):

    # *********************************************
    # * @description: パラメーター設定
    # *********************************************
    @abc.abstractmethod
    def setParams(self, *args, **kwargs):
        pass

    # *********************************************
    # * @description: 数式作成
    # *********************************************
    @abc.abstractmethod
    def getQuestions(self, *args, **kwargs):
        pass

    # *********************************************
    # * @description: 数字取得
    # *********************************************
    @abc.abstractmethod
    def getFormula(self, *args, **kwargs):
        pass
