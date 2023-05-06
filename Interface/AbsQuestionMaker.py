# *********************************************
# * @Date: 2023-04-26 15:18:33
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-05 19:54:53
# * @FilePath: /Arithmetic/Interface/AbsQuestionMaker.py
# * @Description: アブストラクト
# *********************************************
import abc as abc


class AbsQuestionMaker(abc.ABC):

    # 数式
    questions = []
    # 結果つき数式
    answers = []

    # *********************************************
    # * @description: パラメーター設定
    # * @param {dict} params: パラメーターコレクション
    # * @return {*}: None
    # * @Date: 2023-04-30 17:17:39
    # *********************************************
    @abc.abstractmethod
    def setParams(self, *args, **kwargs) -> None:
        pass

    # *********************************************
    # * @description: 数式作成
    # * @param {array} args: 任意パラメーター
    # * @param {object} kwargs: 任意パラメーター
    # * @return {*}: None
    # * @Date: 2023-04-30 17:21:15
    # *********************************************
    @abc.abstractmethod
    def makeQuestions(self, *args, **kwargs) -> None:
        pass

    # *********************************************
    # * @description:
    # * @param {list} lstFactors: 数字リスト
    # * @param {list} lstOperators: オペレーターリスト
    # * @return {*}: 数式の文字列
    # * @Date: 2023-04-30 17:26:18
    # *********************************************
    @abc.abstractmethod
    def getFormula(self, *args, **kwargs) -> str:
        pass
