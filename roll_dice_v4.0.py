'''
    developer: Jing
    date: Aug 23, 2020
    roll two dices
    Histograms
'''
import random
import matplotlib.pyplot as plt

# # to visualize, put the results in a list:
# roll1_list = []
# roll2_list = []

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
        total_time = 1000

        roll_list = []

        for i in range(total_time):
            roll1 = roll_dice()
            roll2 = roll_dice()

            roll_list.append(roll1+roll2)

        # hist:
        plt.hist(roll_list, bins = range(2,14), normed = 1, edgecolor = 'black', linewidth = 1)
        plt.show()


if __name__ =='__main__':
    main()