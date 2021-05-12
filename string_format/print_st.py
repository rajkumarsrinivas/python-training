#val1 = input("value 1 :")
#val2 = input("value 2 :")

#p = f"this is the value no.1  {val1} , also the val no.2 {val2}"
#print(p)

def print_board():
    number_board =[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    print(number_board)
    for row in number_board:
        print('| '+' | '.join(row)+' |')

def board():
    b = [' ' for z in range(9)]
    print(b)
    for row in [b[i*3:(i+1)*3] for i in range(3)]:
        print(' | '.join(row))
        #print('| '+' | '.join(row)+' |')
#print_board()
board()