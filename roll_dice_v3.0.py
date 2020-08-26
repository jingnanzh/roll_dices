'''
    developer: Jing
    date: Aug 23, 2020
    roll two dices
    visualization
'''
import random
import matplotlib.pyplot as plt

# to visualize, put the results in a list:
roll1_list = []
roll2_list = []

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
        total_time = 100
        # 初始化列表[0,0,0,0,0,0,]
        result_list = [0]*11
        roll_list = list(range(2,13))
        roll_dict = dict(zip(roll_list, result_list))

        for i in range(total_time):
            roll1 = roll_dice()
            roll2 = roll_dice()

            # append the result to the rollX_list
            roll1_list.append(roll1)
            roll2_list.append(roll2)

            for j in range(2,13):
                if (roll1+roll2) == j:
                    roll_dict[j] += 1

        for i,result in roll_dict.items():
            print('点数{}的出现次数{}，概率是{}'.format(i, result,result/total_time))

        # visualization:
        x = range(1,total_time+1)
        # alpha: opacity, c:color
        plt.scatter(x,roll1_list, c='red', alpha=0.5)
        plt.show()


if __name__ =='__main__':
    main()