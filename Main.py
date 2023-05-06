###############################################################################
# Lolan 2020/07/29
###############################################################################
import datetime
import random
import Logic as Logic
import Outputer as Outputer
import Interface.AbsQuestionMaker as abs

class Arithmetic:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.abs = abs.AbsQuestionMaker

    def makeAddAndSubExercise(self, factorNum, calSymbol, limits, quantity):
        ques, ans = Logic.QuestionMarker().makeAddAndSub(
                                            # factorNum=factorNum, 
                                            calSymbol=calSymbol,
                                            limits=limits,
                                            quantity=quantity)

        self.questions += ques
        self.answers += ans

    def makeAdvAddSubExecStep1(self, factorNum, calSymbol, limits, quantity):
        ques, ans = Logic.QuestionMarker().makeAdvAddSubExec(
                                            # factorNum=factorNum, 
                                            calSymbol=calSymbol,
                                            limits=limits,
                                            factorRange=(1, 9),
                                            quantity=quantity)

        self.questions += ques
        self.answers += ans

    def makeAdvAddSubExecStep2(self, factorNum, calSymbol, limits, quantity):
        ques, ans = Logic.QuestionMarker().makeAdvAddSubExec(
                                            # factorNum=factorNum, 
                                            calSymbol=calSymbol,
                                            limits=limits,
                                            factorRange=(10, 99),
                                            quantity=quantity)

        self.questions += ques
        self.answers += ans

    def makeAdvAddSubExecStep3(self, factorNum, calSymbol, limits, quantity):
        ques, ans = Logic.QuestionMarker().makeAdvAddSubExec(
                                            # factorNum=factorNum, 
                                            calSymbol=calSymbol,
                                            limits=limits,
                                            factorRange=(100, 999),
                                            quantity=quantity)

        self.questions += ques
        self.answers += ans

    def makeSimpleMultiAndDivExercise(self, calSymbol, limits, quantity):
        ques, ans = Logic.QuestionMarker().makeSimpleMultiAndDiv(
                                            calSymbol=calSymbol,
                                            singleLimits=limits,
                                            quantity=quantity)
        self.questions += ques

    def makeAdvancedMultiplicationExercise(self, singleLimits, quantity):
        ques, ans = Logic.QuestionMarker().makeAdvancedMultiplication(
                                            singleLimits=singleLimits,
                                            quantity=quantity)
        self.questions += ques
        self.answers += ans
    
    def makeSampleMixedOPExercise(self, quantity):
        ques, ans = Logic.QuestionMarker().makeSampleMixedOP(quantity=quantity)
        self.questions += ques
        self.answers += ans
    
    def exportAll(self, name, exppath, date=None):
        # random.shuffle(self.questions)
        self.questions = self._split_4_25(self.questions)
        self.answers = self._split_4_25(self.answers)

        self._export(name + "'s Math Exercises", 
            name, 
            exppath, 
            'Questions_',
            self.questions,
            date
            )

        self._export(name + "'s Math Exercises With Answers", 
            name, 
            exppath, 
            'Answers_',
            self.answers,
            date
            )

    def _split_4_25(self, records):
        result = []
        while len(records) > 0:
            blockSize = 50 if len(records) > 99 else len(records)
            ls = records[:blockSize]
            records = records[blockSize:]
            rd = []
            while len(ls) > 0:
                rs = 4 if len(ls) > 3 else len(ls)
                row = ls[:rs]
                if rs < 4:
                    for x in range(4-rs):
                        row.append('')
                rd.append(row)
                ls = ls[rs:]
            result.append(rd)
        return result

    def _export(self, title, name , path, filename, records, date=None):
        ep = Outputer.OutputDocx(title, name, path, date)
        for r in records:
            file = filename + str(records.index(r) + 1) + '.docx'
            ep.output(file, r)

if __name__ == "__main__":
    ar = Arithmetic()
    # ar.makeAddAndSubExercise(2, ['-'], 100, 100)
    # ar.makeAddAndSubExercise(3, ['-', '+'], 100, 100)
    # ar.makeAddAndSubExercise(3, ['+', '+'], 50, 300)
    # ar.makeAddAndSubExercise(3, ['-', '-'], 50, 300)
    # ar.makeAddAndSubExercise(3, ['+', '-'], 50, 300)
    # ar.makeAddAndSubExercise(2, ['+'], 99, 25)
    # ar.makeAddAndSubExercise(2, ['-'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['+'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['-'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['+'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['-'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['+'], 99, 5)
    # ar.makeAddAndSubExercise(2, ['-'], 50, 400)
    # ar.makeSimpleMultiAndDivExercise('/', 10, 40)
    # ar.makeSimpleMultiAndDivExercise('*', 10, 60)
    # ar.makeAdvancedMultiplicationExercise([[11, 99], [2, 9]], 50)
    # ar.makeSampleMixedOPExercise(50)
    ar.makeAdvAddSubExecStep2(2, ['+'], 1000, 10)
    ar.makeAdvAddSubExecStep2(2, ['-'], 1000, 10)
    ar.makeAdvAddSubExecStep2(2, ['+'], 1000, 10)
    ar.makeAdvAddSubExecStep2(2, ['-'], 1000, 10)
    ar.makeAdvAddSubExecStep2(2, ['+'], 1000, 5)
    ar.makeAdvAddSubExecStep2(2, ['-'], 1000, 5)
    
    ar.exportAll('Harvey', '//Users//lolan//Desktop//Arithmetic//')
    # ar.exportAll('Olaf', 'C:\\Users\\vampi\\Desktop')
    # ar.exportAll('Mogi', 'C:\\Users\\eos\\Desktop\\')
