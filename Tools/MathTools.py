# *********************************************
# * @Date: 2023-04-28 20:15:34
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-03 20:33:04
# * @FilePath: /Arithmetic/Tools/MathTools.py
# * @Description: 数字に関するツールクラス
# *********************************************
import math
import random


class MathTools:

    # *********************************************
    # * @description: ランダム自然数取得
    # * @param {int} digits: 桁数指定
    # * @param {int} startFrom: 下限値。1桁の場合のみ有効、デフォルト値あり
    # * @return {*}: 取得した自然数
    # * @Date: 2023-04-30 17:06:40
    # *********************************************
    @classmethod
    def getRandomInt(cls, digits: int, startFrom: int = 1) -> int:
        result = -1
        if digits == 1:
            result = random.randint(startFrom, 9)
        elif digits == 2:
            result = random.randint(10, 99)
        elif digits == 3:
            result = random.randint(100, 999)
        return result

    # *********************************************
    # * @description: 指定範囲内、素数以外の自然数全部取得
    # * @param {*} limit: 上限
    # * @return {*}：素数以外の自然数のリスト
    # * @Date: 2023-04-30 17:14:40
    # *********************************************
    @classmethod
    def getNotPrime(cls, limit) -> list:
        return list(
            filter(
                lambda x:
                [x % i for i in range(2,
                                      int(math.sqrt(x)) + 1) if x % i == 0],
                range(2, limit + 1)))
