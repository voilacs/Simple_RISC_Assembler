import math

pc_counter = 0
flagreg = "0000000000000000"
registers = ['000', '001', '010', '011', '100', '101', '110', '111']
regvalue = ['0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000']


def restore_default_reg():
    global flagreg
    flagreg = "0000000000000000"


def checkOverflow(value):
    if value > (2 ** 16 - 1):
        return True
    return False


def binaryconverter(number, bit=1):
    # give bit=0 for PC and bit=1 otherwise
    l = []
    while number != 0:
        rem = str(number % 2)
        l.append(rem)
        number = number // 2
    l.reverse()
    if bit == 1:
        while len(l) < 16:
            l.insert(0, '0')
    else:
        while len(l) < 7:
            l.insert(0, '0')
    binary_string = ''.join(l)
    return binary_string


def intconverter(binary):
    binary = int(binary)
    d = 0
    c = 0
    i = 0
    while binary > 0:
        d = binary % 10
        c += d * (math.pow(2, i))
        binary = binary // 10
        i+=1
    return int(c)




def setAddress(memory, memoryAddress, Value):
    memory[intconverter(memoryAddress)] = Value


def execute(j,pc,memory):
    global flagreg
    pc_counter=pc
    op_code = j[0:5]

    if op_code == "00000" or op_code == "00001":
        r1 = j[7:10]
        r2 = j[10:13]
        r3 = j[13:16]
        a = regvalue[registers.index(r2)]
        a = intconverter(a)
        b = regvalue[registers.index(r3)]
        b = intconverter(b)
        if op_code == "00000":
            c = a + b
            if checkOverflow(c):
                setoverflow()
            else:
                index = registers.index(r1)
                regvalue[index] = binaryconverter(c)
        elif op_code == "00001":
            c = a - b
            if checkOverflow(c):
                setoverflow()
            else:
                index = registers.index(r1)
                regvalue[index] = binaryconverter(c)
        reset()
        return False, pc_counter+1
    elif op_code == "00010":
        r1 = j[6:9]
        immediate = j[9:]
        index = registers.index(r1)
        
        regvalue[index] =  binaryconverter(intconverter(immediate))
        reset()
        return False, pc_counter+1
    elif op_code == "00011":
        r1 = j[10:13]
        r2 = j[13:16]
        c = regvalue[registers.index(r2)]
        index = registers.index(r1)
        regvalue[index] = c
        reset()
        return False, pc_counter+1
    elif op_code == "00100":
        r1 = j[6:9]
        adr = j[9:]
        reset()
        return False, pc_counter+1
    elif op_code == "00101":
        r1 = j[6:9]
        adr = j[9:]
        store=regvalue[registers.index(r1)]
        setAddress(memory, adr,store)
        reset()
        return False, pc_counter+1
    elif op_code == "00110":
        r1 = j[7:10]
        r2 = j[10:13]
        r3 = j[13:]
        a = regvalue[registers.index(r2)]
        a = intconverter(a)
        b = regvalue[registers.index(r3)]
        b = intconverter(b)
        c = a * b
        if checkOverflow(c):
            setoverflow()
        else:
            index = registers.index(r1)
            regvalue[index] = binaryconverter(c)
        reset()
        return False, pc_counter+1
    elif op_code == "00111":
        r1 = j[10:13]
        r2 = j[13:]
        a = regvalue[registers.index(r1)]
        a = intconverter(a)
        b = regvalue[registers.index(r2)]
        b = intconverter(b)
        rem = a % b
        quot = a // b
        regvalue[0] = binaryconverter(quot)
        regvalue[-1] = binaryconverter(rem)
        reset()
        return False, pc_counter+1
    elif op_code == "01000":
        r1 = j[5:8]
        immediate = intconverter(j[8:])
        immediate = int(immediate)
        ss = '0' * immediate + regvalue[registers.index(r1)][:len(registers) - immediate]
        index = registers.index(r1)
        regvalue[index] = ss
        reset()
        return False, pc_counter+1
    elif op_code == "01001":
        r1 = j[5:8]
        immediate = intconverter(j[8:])
        immediate = int(immediate)
        ss = regvalue[registers.index(r1)][:len(registers) - immediate] + '0' * immediate
        index = registers.index(r1)
        regvalue[index] = ss
        reset()
        return False, pc_counter+1
    elif op_code == "01010":
        r1 = j[7:10]
        r2 = j[10:13]
        r3 = j[13:]
        a = regvalue[registers.index(r2)]
        a = intconverter(a)
        b = regvalue[registers.index(r3)]
        b = intconverter(b)
        c = int(a) ^ int(b)
        index = registers.index(r1)
        regvalue[index] = binaryconverter(c)
        reset()
        return False, pc_counter+1
    elif op_code == "01011":
        r1 = j[7:10]
        r2 = j[10:13]
        r3 = j[13:]
        c = int(regvalue[registers.index(r2)], 2) | int(regvalue[registers.index(r3)], 2)
        regvalue[registers.index(r1)] = binaryconverter(c)
        reset()
        return False, pc_counter+1
    elif op_code == "01100":
        r1 = j[7:10]
        r2 = j[10:13]
        r3 = j[13:]
        c = int(regvalue[registers.index(r2)], 2) & int(regvalue[registers.index(r3)], 2)
        regvalue[registers.index(r1)] = binaryconverter(c)
        return False, pc_counter+1
    elif op_code == "01101":
        r1 = j[10:13]
        r2 = j[13:]
        inverted = ""
        for bit in r2:
            if bit == '1':
                inverted += '0'
            else:
                inverted += '1'
        regvalue[registers.index(r1)] = inverted
        reset()
        return False, pc_counter+1
    elif op_code == "01110":
        r1 = j[10:13]
        r2 = j[13:]
        if regvalue[registers.index(r1)] < regvalue[registers.index(r2)]:
            flagreg = "0000000000000100"
        elif regvalue[registers.index(r1)] > regvalue[registers.index(r2)]:
            flagreg = "0000000000000010"
        else:
            flagreg = "0000000000000001"
        regvalue[-1]=flagreg
        return False, pc_counter+1
    elif op_code == "01111":
        memoryAddress = j[8:]
        pc_counter = int(memoryAddress, 2)
        reset()
        return False, pc_counter
    elif op_code == "11100":
        if flagreg == "0000000000000100":
            memoryAddress = j[8:]
            pc_counter = int(memoryAddress, 2)
            reset()
            return False, pc_counter
        else:
            pc_counter += 1
            reset()
            return False, pc_counter
    elif op_code == "11101":
        if flagreg == "0000000000000010":
            memoryAddress = j[8:]
            pc_counter = int(memoryAddress, 2)
            reset()
            return False, pc_counter
        else:
            pc_counter += 1
            reset()
            return False, pc_counter
    elif op_code == "11111":
        if flagreg == "0000000000000001":
            memoryAddress = j[8:]
            pc_counter = int(memoryAddress, 2)
            reset()
            return False, pc_counter
        else:
            pc_counter += 1
            reset()
            return False, pc_counter
    elif op_code == "11010":
        pc_counter += 1
        reset()
        return True, pc_counter

# Set the initial values
flagreg = "0000000000000000"


def reset():
    global flagreg
    flagreg = "0000000000000000"
    regvalue[-1]=flagreg

def setoverflow():
    global flagreg
    flagreg = "0000000000001000"


def dump_state(pc):
    print(str(binaryconverter(pc,0)), end="        ")
    for i in regvalue:
        print(i, end=" ")
    print()


def dump_memory(memory):
    for i in memory:
        print(i)

import sys
def execute_program():
    global code
    memory = []
    lineDiff=0
    for i in sys.stdin:
        memory.append(i.rstrip())
    code = memory.copy()
    if len(memory) < 128:
        lineDiff = 128 - len(memory)
    while lineDiff:
        memory.append("0000000000000000")
        lineDiff -= 1
    pc = 0
    halted = False
    while not halted:
        j = code[pc]
        halted, new_pc = execute(j,pc,memory)  # Execute the j
        dump_state(pc)  # Print PC and RF state
        pc = new_pc if new_pc is not None else pc + 1  # Update PC
    dump_memory(memory)
execute_program()