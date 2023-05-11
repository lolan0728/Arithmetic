# & *********************************************
# & @Date: 2023-04-28 20:15:34
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 16:59:40
# & @FilePath: /Arithmetic/Tools/MathTools.py
# & @Description: 
# & *********************************************
import math
import random
from Entity.Factors import Element


class MathTools:

    # *********************************************
    # * @description: ランダム整数取得
    # * @param {Element} element: 桁数など設定条件
    # * @return {int}: 取得した整数
    # *********************************************
    @classmethod
    def __getRandomInt(cls, element: Element) -> int:
        result = -1
        # 1桁の場合
        if element.intDigits == 1:
            lstNum = list(range(2, 10))
            # 0可能の場合、0もリストに追加
            if element.allowZero:
                lstNum.append(0)
            # 1可能の場合、1もリストに追加
            if element.allowOne:
                lstNum.append(1)
            result = random.choice(lstNum)
        # 2桁の場合
        elif element.intDigits == 2:
            result = random.randint(10, 99)
        # 3桁の場合
        elif element.intDigits == 3:
            result = random.randint(100, 999)
        return result

    # *********************************************
    # * @description: ランダム小数取得
    # *********************************************
    @classmethod
    def __getRandomDecimal(cls, digits: int) -> int:
        # Todo
        pass

    # *********************************************
    # * @description: ランダム数字取得
    # *********************************************
    @classmethod
    def getElement(cls, element: Element):
        # TODO 小数数式まだ対応していない
        return cls.__getRandomInt(element)

    # *********************************************
    # * @description: 指定範囲内、素数以外の自然数全部取得
    # * @param {int} limit: 上限
    # * @return {list[int]}：素数以外の自然数のリスト
    # *********************************************
    @classmethod
    def getNotPrime(cls, limit: int) -> list[int]:
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
    element = Element(**param)
    print(MathTools.getElement(element))
