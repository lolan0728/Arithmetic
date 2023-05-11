# & *********************************************
# & @Date: 2023-05-05 10:52:20
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 16:43:46
# & @FilePath: /Arithmetic/Enums/OperatorEnum.py
# & @Description: オペレーター符号Enum
# & *********************************************
from enum import Enum


class OpEnum(Enum):
    ADD = '+'
    SUB = '-'
    MULTI = '×'
    DIV = '÷'
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'
    EQUALS = '='
    BLANK = ' '
