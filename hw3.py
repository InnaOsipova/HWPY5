#Создайте программу для игры в ""Крестики-нолики"".
import random as r

board = list(range (1, 10))
def play_form ():
    print('-------------')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')
play_form ()


def vin_table(chec_vin, pl, step):
    if step == 8:
        print ("Победителей нет")
        return True
    for i in range(len(chec_vin)-1):
        if chec_vin[i][0] == chec_vin[i][1] == chec_vin[i][2]:
                print (f'Победил игрок играющией под номером {pl}')
                return True





def enter_simbol (simbol, pl, memory_vin):
    num = int(input(f'Игрок номер {pl} определите номер ячейки в которую ставим {simbol} : '))
    board [num-1] = simbol
    for i in range(len(memory_vin)):
        for j in range(3):
            if memory_vin[i][j] == num:
                memory_vin[i][j] = simbol
    return memory_vin


print ('Первый игрок  "X", второй игрок играет "O"\n Выберите кто играет первым первый или второй игрок\n')
player = int(input("Введите номер игрока :"))
step = 0

memory = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
while vin_table(memory, player, step) != True:
    if player == 1:
        sim_play = "X"
        enter_simbol(sim_play, 1, memory)
        player =2
        step +=1
        play_form()
    elif player == 2:
        sim_play = "O"
        enter_simbol(sim_play, 2, memory)
        player =1
        step +=1
        play_form()
    

