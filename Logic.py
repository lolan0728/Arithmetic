###############################################################################
# Lolan 2020/08/04
###############################################################################
import math
import random

class QuestionMarker:
    def __init__(self):
        pass

    def makeAddAndSub(self, calSymbol=['+'], limits=100, quantity=100):
        questions = []
        answers = []
        while True:
            total = fst = random.randint(1, limits-1)
            r = []
            q = str(fst)
            for y in range(len(calSymbol)):
                if calSymbol[y] == '+':
                    factor = random.randint(0, limits-total)
                    total +=  factor
                elif calSymbol[y] == '-':
                    factor = random.randint(0, total - 1) if total > 0 else 0
                    total -=  factor
                r.append(factor)
                q += ' ' + calSymbol[y] + ' ' +  str(factor)
            if not 0 in r:
                q += ' = '
                questions.append(q)
                q += str(total)
                answers.append(q)
                if len(questions) == quantity:
                    break
        return questions, answers
    
    def makeAdvAddSubExec(self, calSymbol=['+'], limits=1000, factorRange=(1, 10), quantity=100):
        questions = []
        answers = []
        while True:
            total = fst = random.randint(100, limits)
            r = []
            q = str(fst)
            for y in range(len(calSymbol)):
                if calSymbol[y] == '+':
                    factor = random.randint(factorRange[0], factorRange[1])
                    total +=  factor
                elif calSymbol[y] == '-':
                    factor = random.randint(factorRange[0], factorRange[1])
                    total -=  factor
                r.append(factor)
                q += ' ' + calSymbol[y] + ' ' +  str(factor)
            if total > 0 and total < limits:
                q += ' = '
                questions.append(q)
                q += str(total)
                answers.append(q)
                if len(questions) == quantity:
                    break
        return questions, answers
    
    
    
    def makeSimpleMultiAndDiv(self, calSymbol='*', 
                                                singleLimits=10, limits=100, quantity=100):
        questions = []
        answers = []
        while True:
            # if calSymbol == '*':
            #     fst = random.randint(2, singleLimits)
            #     sec = random.randint(2, singleLimits)
            #     calSy = '×'
            #     # calSy = '*'
            #     ans = fst * sec
            # elif calSymbol == '/':
            #     fst = self._randomDividendSimple()
            #     sec = self._rendomDivisorSimple(fst, [2, singleLimits])
            #     calSy = '÷'
            #     # calSy = '/'
            #     ans = fst / sec
            # q = str(fst) + ' ' + calSy + ' ' + str(sec) + ' = '
            # if fst != sec and sec != 1:
            #     if ans <= limits:
            #         questions.append(q)
            #         q += str(ans)
            #         answers.append(q)
            #         if len(questions) == quantity:
            #                 break
            if calSymbol == '*':
                fst = random.randint(2, singleLimits)
                formula, answer = self._getMultiplicationFormula([2, singleLimits], str(fst), fst)
            elif calSymbol == '/':
                fst = self._randomDividendSimple()
                formula, answer = self._getDivisionFormula([2, singleLimits], str(fst), fst)
            q = formula + ' = '
            if answer <= limits:
                questions.append(q)
                q += str(answer)
                answers.append(q)
                if len(questions) == quantity:
                        break
        return questions, answers

    def makeAdvancedMultiplication(self, singleLimits=[[11, 19], [1, 10]], quantity=100):
        questions = []
        answers = []
        while True:
            fst = random.randint(singleLimits[0][0], singleLimits[0][1])
            formula, answer = self._getMultiplicationFormula(singleLimits[1], str(fst), fst)
            q = formula + ' = '
            questions.append(q)
            q += str(answer)
            answers.append(q)
            if len(questions) == quantity:
                    break
        return questions, answers

    def _getAdditionFormula(self, limits=100, formula='', answer=0, result=0):        
        factor = random.randint(1, limits-answer) if result==0 else result-answer
        formula += ' + ' + str(factor)
        answer += factor
        return formula, answer

    def _getSubtractionFormula(self, limits=100, formula='', answer=0, result=0):
        if result == 0:
            if limits < answer:
                factor = random.randint(answer-limits, answer-1)
            else:
                factor = random.randint(1, answer-1)
        else: 
            factor = answer-result
        formula += ' - ' + str(factor)
        answer -= factor
        return formula, answer
    
    def _getMultiplicationFormula(self, factorLimits=[2, 10], formula='', answer=1, result=0):
        factor = random.randint(factorLimits[0], factorLimits[1]) if result==0 else result/answer
        formula += ' × ' + str(factor)
        answer *= factor
        return formula, answer

    def _getDivisionFormula(self, factorLimits=[2, 10], formula='', answer=0, result=0):
        if answer != 0:
            factor = self._rendomDivisorSimple(answer, factorLimits) if result==0 else answer/result
            if factor != 0:
                formula += ' ÷ ' + str(factor)
                answer /= factor
        return formula, answer

    def makeSampleMixedOP(self, quantity=100):
        questions = []
        answers = []
        allType = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        while True:
            q = a = ''
            # formulaType = random.randint(16, 16)
            formulaType = random.choice(allType)
            if formulaType == 1:
                # (a + b) * c
                a = random.randint(1, 8)
                subFml, subAns = self._getAdditionFormula(limits=10, formula=str(a), answer=a)            
                c = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(c) + ' = '
                ans = que + str(int(subAns * c))
            elif formulaType == 2:
                # (a - b) * c
                a = random.randint(2, 99)
                subFml, subAns = self._getSubtractionFormula(limits=10, formula=str(a), answer=a)            
                c = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(c) + ' = '
                ans = que + str(int(subAns * c))
            elif formulaType == 3:
                # (a + b) / c
                fst = self._randomDividendSimple()
                a = random.randint(1, fst-1)
                subFml, subAns = self._getAdditionFormula(formula=str(a), answer=a, result=fst)
                c = self._rendomDivisorSimple(fst)
                que = self._addBrackets(subFml) + ' ÷ ' + str(c) + ' = '
                ans = que + str(int(subAns / c))
            elif formulaType == 4:
                # (a - b) / c
                fst = self._randomDividendSimple()
                a = random.randint(fst+1, 99)
                subFml, subAns = self._getSubtractionFormula(formula=str(a), answer=a, result=fst)
                c = self._rendomDivisorSimple(fst)
                que = self._addBrackets(subFml) + ' ÷ ' + str(c) + ' = '
                ans = que + str(int(subAns / c))
            elif formulaType == 5:
                # a + b * c
                b = random.randint(1, 9)
                subFml, subAns = self._getMultiplicationFormula(formula=str(b), answer=b)
                a = random.randint(1, 99-subAns)
                que = str(a) + ' + ' + subFml + ' = '
                ans = que + str(int(a + subAns))
            elif formulaType == 6:
                # a + b / c
                b = self._randomDividendSimple()
                subFml, subAns = self._getDivisionFormula(formula=str(b), answer=b)
                a = random.randint(1, 99-subAns)
                que = str(a) + ' + ' + subFml + ' = '
                ans = que + str(int(a + subAns))
            elif formulaType == 7:
                # (a + b) * (c + d)
                a = random.randint(1, 8)
                c = random.randint(1, 8)
                subFml_1, subAns_1 = self._getAdditionFormula(limits=10, formula=str(a), answer=a)
                subFml_2, subAns_2 = self._getAdditionFormula(limits=10, formula=str(c), answer=c)
                que = self._addBrackets(subFml_1) + ' × ' + self._addBrackets(subFml_2) + ' = '
                ans = que + str(int(subAns_1 * subAns_2))
            elif formulaType == 8:
                # (a + b) / (c + d)
                fst = self._randomDividendSimple()
                a = random.randint(1, fst-1)
                subFml_1, subAns_1 = self._getAdditionFormula(formula=str(a), answer=a, result=fst)
                sec = self._rendomDivisorSimple(fst)
                c = random.randint(1, sec-1)
                subFml_2, subAns_2 = self._getAdditionFormula(formula=str(c), answer=c, result=sec)
                que = self._addBrackets(subFml_1) + ' ÷ ' + self._addBrackets(subFml_2) + ' = '
                ans = que + str(int(subAns_1 / subAns_2))
            elif formulaType == 9:
                # (a - b) * (c + d)
                a = random.randint(2, 99)
                subFml_1, subAns_1 = self._getSubtractionFormula(limits=10, formula=str(a), answer=a)
                c = random.randint(1, 8)
                subFml_2, subAns_2 = self._getAdditionFormula(limits=10, formula=str(c), answer=c)
                que = self._addBrackets(subFml_1) + ' × ' + self._addBrackets(subFml_2) + ' = '
                ans = que + str(int(subAns_1 * subAns_2))
            elif formulaType == 10:
                # (a - b) * (c - d)
                a = random.randint(2, 99)
                subFml_1, subAns_1 = self._getSubtractionFormula(limits=10, formula=str(a), answer=a)
                c = random.randint(2, 99)
                subFml_2, subAns_2 = self._getSubtractionFormula(limits=10, formula=str(c), answer=c)
                que = self._addBrackets(subFml_1) + ' × ' + self._addBrackets(subFml_2) + ' = '
                ans = que + str(int(subAns_1 * subAns_2))
            elif formulaType == 11:
                # (a + b + c) * d
                a = random.randint(1, 8)
                subFml, subAns = self._getAdditionFormula(limits=9, formula=str(a), answer=a)
                subFml, subAns = self._getAdditionFormula(limits=10, formula=subFml, answer=subAns)
                d = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(d) + ' = '
                ans = que + str(int(subAns * d))
            elif formulaType == 12:
                # (a + b - c) * d
                a = random.randint(1, 99)
                subFml, subAns = self._getAdditionFormula(formula=str(a), answer=a)
                subFml, subAns = self._getSubtractionFormula(limits=10, formula=subFml, answer=subAns)
                d = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(d) + ' = '
                ans = que + str(int(subAns * d))
            elif formulaType == 13:
                # (a - b - c) * d
                a = random.randint(4, 99)
                while True:
                    subFml, subAns = self._getSubtractionFormula(formula=str(a), answer=a)
                    if subAns > 1:
                        break
                subFml, subAns = self._getSubtractionFormula(limits=10, formula=subFml, answer=subAns)
                d = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(d) + ' = '
                ans = que + str(int(subAns * d))
            elif formulaType == 14:
                # (a - b + c) * d
                a = random.randint(3, 99)
                subFml, subAns = self._getSubtractionFormula(limits=9, formula=str(a), answer=a)
                subFml, subAns = self._getAdditionFormula(limits=10, formula=subFml, answer=subAns)
                d = random.randint(1, 9)
                que = self._addBrackets(subFml) + ' × ' + str(d) + ' = '
                ans = que + str(int(subAns * d))
            elif formulaType == 15:
                # (a + b + c) / d
                fst = self._randomDividendSimple()
                a = random.randint(1, fst-2)
                subFml, subAns = self._getAdditionFormula(limits=fst-1, formula=str(a), answer=a)
                subFml, subAns = self._getAdditionFormula(formula=subFml, answer=subAns, result=fst)
                d = self._rendomDivisorSimple(fst)
                que = self._addBrackets(subFml) + ' ÷ ' + str(d) + ' = '
                ans = que + str(int(subAns / d))
            elif formulaType == 16:
                # (a - b - c) / d
                fst = self._randomDividendSimple()
                a = random.randint(fst+2, 99)
                b = random.randint(1, a-fst-1)
                fm = str(a) + ' - ' + str(b)
                subFml, subAns = self._getSubtractionFormula(formula=fm, answer=a-b, result=fst)
                d = self._rendomDivisorSimple(fst)
                que = self._addBrackets(subFml) + ' ÷ ' + str(d) + ' = '
                ans = que + str(int(subAns / d))
            if que != '':
                questions.append(que)
                answers.append(ans)
            if len(questions) == quantity:
                    break
        return questions, answers

    def _addBrackets(self, formula):
        return '(' + formula + ')'
        
            

    def _getCalUnit(self, factorNum=2, limits=100, result=0):
        
        symAll = ['+', '-', '*', '/']
        answer = ''

        if factorNum == 1:
            answer = random.randint(1, limits) if result==0 else result
        elif factorNum == 2:
            sym = random.choice(symAll)
            if sym == '+':
                fst = random.randint(1, limits) if result==0 else random.randint(1, result)
                f, a = self._getAdditionFormula(limits, str(fst), fst, result)
            elif sym == '-':
                fst = random.randint(1, limits) if result==0 else random.randint(result, limits)
                f, a = self._getSubtractionFormula(str(fst), fst, result)
            result = ' ( ' + str(q[0]).replace(' = ', '') + ' ) '
        else:
            sym = []
            for i in range(factorNum-1):
               sym.append(random.choice(['+', '-'])) 
            
            q, a = self.makeAddAndSub(sym, limits, 1)
            result = ' ( ' + str(q[0]).replace(' = ', '') + ' ) '

        return answer
        

    def _getNotPrime(self, limit):
        return list(filter(lambda x: [x%i for i in range(2, 
                        int(math.sqrt(x))+1) if x%i ==0], range(2, limit+1)))
    
    def _randomDividend(self, limit):
        return random.choice(self._getNotPrime(limit))

    def _randomDividendSimple(self, fLimits=[2, 10]):
        return random.choice([i*j for i in range(fLimits[0], fLimits[1]) \
                                        for j in range(fLimits[0], fLimits[1])])

    def _rendomDivisor(self, dividend, limit=10):
        return random.choice([d for d in range(2, limit) if dividend%d == 0 ])

    def _rendomDivisorSimple(self, dividend, fLimits=[2, 10]):
        divisor = [d for d in range(fLimits[0], fLimits[1]) \
                                    if dividend%d == 0 and dividend/d < fLimits[1]]
        if len(divisor) > 0:                                    
            return random.choice(divisor)
        else:
            return 0

if __name__ == "__main__":

    q = QuestionMarker()
    for i in range(20):
        f, a = q._getDivisionFormula(factorLimits=[[2,10]], formula='(4 + 7)', answer=11) 
        print(f + ' = ' + str(a))
    # print(q._getCalUnit(2, 100))
    #self tester
    # q, a = QuestionMarker(factorNum=3, calSymbol=['-', '+'], quantity=50).makeQuestions()
    # print(q)
    # print(a)
                

