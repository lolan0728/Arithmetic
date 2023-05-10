# *********************************************
# * @Date: 2023-04-28 20:15:34
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-09 15:40:27
# * @FilePath: /Arithmetic/Tools/MathTools.py
# * @Description: 数字に関するツールクラス
# *********************************************
import math
import random
from Entity.Factors import FactorUnit


class MathTools:

    # *********************************************
    # * @description: ランダム整数取得
    # * @param {Factor} factor: 桁数指定
    # * @return {int}: 取得した整数
    # * @Date: 2023-04-30 17:06:40
    # *********************************************
    @classmethod
    def getRandomInt(cls, factor: FactorUnit) -> int:
        result = -1
        if factor.intDigits == 1:
            lstNum = list(range(2, 10))
            if factor.allowZero:
                lstNum.append(0)
            if factor.allowOne:
                lstNum.append(1)
            result = random.choice(lstNum)
        elif factor.intDigits == 2:
            result = random.randint(10, 99)
        elif factor.intDigits == 3:
            result = random.randint(100, 999)
        return result

    # *********************************************
    # * @description: ランダム小数取得
    # * @Date: 2023-04-30 17:06:40
    # *********************************************
    @classmethod
    def getRandomDecimal(cls, digits: int) -> int:
        # Todo
        pass

    @classmethod
    def getFactor(cls, factor: FactorUnit):
        return cls.getRandomInt(factor) 

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


# テスト用
if __name__ == "__main__":
    # print(MathTools.getRandomInt(1, False, False))
    param = {
        'intDigits': '1',
        'decimalPlaces': '0',
        'allowZero': 'True',
        'allowOne': 'True',
    }
    factor = FactorUnit(**param)
    print(MathTools.getRandomInt(factor))
