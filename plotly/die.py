from random import randint
class Die():


    '''表示一个骰子的类'''
    def _int_(self,num_sides=6):
        '''骰子的默认面'''
        self.num_sides=num_sides


    def roll(self):# 方法使用roll（） 使用randint()返回1-面数之间的随机数
        '''返回一个位于1和骰子面数之间的数值'''
        return randint(1,self.num_sides)