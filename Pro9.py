b = {'top-L':' ','top-M':' ','top-R':' ',
     'mid-L':' ','mid-M':' ','mid-R':' ',
     'low-L':' ','low-M':' ','low-R':' '}

def show():
    print(b['top-L']+'|'+b['top-M']+'|'+b['top-R'])
    print("-+-+-")
    print(b['mid-L']+'|'+b['mid-M']+'|'+b['mid-R'])
    print("-+-+-")
    print(b['low-L']+'|'+b['low-M']+'|'+b['low-R'])

turn = 'X'

for i in range(9):
    show()
    m = input("Turn for " + turn + ". Move on which space? ")
    b[m] = turn
    turn = 'O' if turn == 'X' else 'X'

show()
