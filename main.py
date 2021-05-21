Option = {
    'ADD' : [1, 2],
    'SUB' : [2, 2],
    'AND' : [3, 2],
    'INC' : [4, 1],
    'LD'  : [5, 2],
    'LAD' : [5, 2],
    'ST'  : [6, 2],
    'STO' : [6, 2],
    'JC'  : [7, 1],
    'JZ'  : [8, 1],
    'JMP' : [9, 1],
    'OUT' : [10, 1],
    'IRET': [11, 0],
    'DI'  : [12, 0],
    'EI'  : [13, 0],
    'STOP': [14, 0],
    'STP' : [14, 0],
}
err = 'ERROR'

def Number(num) : 
    try :
        if num[-1] == 'H' :
            return int(num[:-1], 16)
        elif num[-1] == 'B' :
            return int(num[:-1], 2)
        elif num[-1] == 'O' :
            return int(num[:-1], 8)
        elif num[0:2] == '0X' :
            return int(num[2:], 16)
        elif num[0:2] == '0B' :
            return int(num[2:], 2)
        elif num[0] == '0' and len(num) > 1 :
            return int(num[1:], 8)
        else :
            return int(num)
    except :
        raise

def Bin(num) :
    s = ""
    for i in range(4) :
        s += str( (num>>3-i)&1)
    return s

def toRegister(name) : 
    if name[0] != 'R' or len(name) != 2:
        return err
    n = int(name[1:])
    return Bin(n)[2:]

def toBitString() :
    try :
        s = input().upper()
        s = s.replace(',', ' ')
        s = s.replace('(', ' ')
        s = s.replace(')', ' ')
        s = s.replace('，', ' ')
        s = s.replace('（', ' ')
        s = s.replace('）', ' ')
        s = s.split()
        if s[0] not in Option :
            return err
        if len(s) != Option[s[0]][1]+1 :
            return err
        Type = Option[s[0]][0]
        if Type <= 3 or Type == 5 or Type == 6 :
            s[1], s[2] = toRegister(s[1]), toRegister(s[2])
            if s[1] == err or s[2] == err :
                return err
            s[1] += s[2]
        elif Type == 4 or Type == 9 :
            s[1] = toRegister(s[1])
            if s[1] == err :
                return err
            s[1] += '00'
        elif Type == 10 :
            s[1] = toRegister(s[1])
            if s[1] == err :
                return err
            s[1] = '00'+s[1]
        elif Type == 7 or Type == 8 :
            try :
                s[1] = Number(s[1])
                s[1] = Bin(s[1])
            except :
                return err
        else :
            s.append('0000')
        return Bin(Type) + s[1]
    except :
        raise

while True :
    try :
        print( toBitString() )
    except :
        exit(0)