'''
    developer: Jing
    date: Aug 23, 2020
    roll a dice
'''
import random

def roll_dice():
    '''
        roll a dice
    '''
    roll = random.randint(1,6)
    return roll

def main():
        '''
            主函数 
        '''
        total_time = 10000
        # 初始化列表[0,0,0,0,0,0,]
        result_list = [0]*6

        for i in range(total_time):
            roll = roll_dice()
            for j in range(1,7):
                if roll == j:
                    result_list[j-1] +=1

        for i,result in enumerate(result_list):
            print('点数{}的出现次数{}，概率是{}'.format(i+1, result,result/total_time))

if __name__ =='__main__':
    main()