import math
import sys
# line 30 tak sab kuchh bas initialize hi ho raha hai uske baad code hai kuch
# jump ke alawa saare opcodes ke liye pc_counter+=1 zaroor karein
pc_counter=0
flagreg="0000000000000000"
registers=['000', '001', '010', '011', '100', '101', '110']
regval=[0, 0, 0, 0, 0, 0, 0]
def restore_default_reg(self):
        '''
        refreshes the value of flag register to the default value set at the start of program
        '''
        flagRegister = "0000000000000000"
def checkOverflow(value):
    '''
    returns true if the range of register's value is exceeded.
    '''
    if(value > (2**16 - 1)):
        return True
    return False
#flagRegister = "0000000000001000"  use this line of code to set flag when overflow
#flagRegister = "0000000000000100"  use this line of code to set flag of less than
#flagRegister = "0000000000000010"  use this line of code to set flag of greater than
#flagRegister = "0000000000000001"  This flag is set by the "cmp reg1 reg2" instruction if reg1 = reg2
#print(flagRegister, end=" ") prints the current value of flag register
#yeh neeche if else wali harkat mat karna hamara code mein vahin per flagregister set karna padega
# if(checkOverflow(res)):
#                 RF.setOverflowFlag()
#             else:
#                 RF.resetFlagRegister()
def binaryconverter(number,bit=1):
    #give bit=0 for PC and bit=1 otherwise    
    l=[]
    while number!=0:
        rem=str(number%2)
        l.append(rem)
        number=number//2
    l.reverse()
    if(bit==1):    
            while len(l) < 16:
                l.insert(0,'0')
    else:
        while len(l) < 7:
                l.insert(0,'0')
    binary_string = ''.join(l)
    return binary_string
def intconverter(binary):
        d=0
        c=0
        i=0
        while(binary>0):
                d=binary%10
                c+=d*(math.pow(2,i))
                binary=binary//10
        return binary   
def getData(memory,PC):
    return memory[PC]

# def dump_memory(memory):
#     Function to dump the memory onto stdout
#     for ins in memory:
#         print(ins)
        
def getAddress(memory, memoryAddress):
    return intconverter(memoryAddress)

def setAddress(memory, memoryAddress,Value):
    memory[intconverter(memoryAddress)] = binaryconverter(Value)
for i in range(len(code)):
        j=code[i]
        op_code=j[0:5]
        if(op_code="00000" or op_code="00001"):
                r1=j[7:10]
                r2=j[10:13]
                r3=j[13:16]
                a=getRegister(r2)
                b=getRegister(r3)
                if(op_code="00000"):
                        c=a+b
                        if(checkOverflow(c)):
                                setOverflow()
                        else:
                                index=registers.index(r1)
                                regvalue[index]=binaryconverter(c)
                elif(op_code="00001"):
                        c=a-b
                        if(checkOverflow(c)):
                                setOverflow()
                        else:
                                index=registers.index(r1)
                                regvalue[index]=binaryconverter(c)
        elif(op_code="00010"):
                r1=j[6:9]
                immediate=intconverter(j[9:])
        elif(op_code="00011"):
                r1=j[10:13]
                r2=j[13:16]
        elif(op_code="00100"):
                r1=j[5:8]
                adr=j[8:]
        elif(op_code="00101"):
                r1=j[5:8]
                adr=j[8:]
        elif(op_code="00110"):
                r1 = j[7:10]
                r2 = j[10:13]
                r3 = j[13:]
                a=getRegister(r2)
                b=getRegister(r3)
                c=a*b
                if(checkOverflow(c)):
                        setOverflow()
                else:
                        index=registers.index(r1)
                        regvalue[index]=binaryconverter(c)
        elif(op_code="00111"):
                r1=j[10:13]
                r2=j[13:]
                a=getRegister(r1)
                b=getRegister(r2)
                rem=a%b
                quot=a//b
        elif(op_code="01000"):
                r1=j[5:8]
                immediate=intconverter(j[8:])
                ss='0'*immediate+getRegister(r1)[:len(getRegister)-immediate]
        elif(op_code="01001"):
                r1=j[5:8]
                immediate=intconverter(j[8:])
                ss=getRegister(r1)[:len(getRegister)-immediate]+'0'*immediate
        elif(op_code="01010"):
                r1=j[7:10]
                r2=j[10:13]
                r3=j[13:]
                a=getRegister(r1)
                b=getRegister(r2)
                c=a^b
        elif(op_code="01011"):
            reg1 = instruction[ 7:10:]
            reg2 = instruction[10:13:] 
            reg3 = instruction[13:16:]
            res = getreg(reg2,False) | getreg(reg3,False)
            setreg(reg1,res)
            restore_default_reg()
            halt=False
            pc_counter+=1
         elif(op_code == "01100"):
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = getreg(reg2,False) & getreg(reg3,False)
            setreg(reg1,res)
            restore_default_reg()
            halt=False
            pc_counter+=1
        elif(op_code == "01101"):
            reg1 = instruction[10:13:]      # Reading address of reg1
            reg2 = instruction[13::]        # Reading address of reg2
            inverted = ""
            for bit in reg2:
                if bit=='1':
                    inverted += '0'
                else:
                    inverted += '1'
            setreg(reg1, int(inverted, 2))
            restore_default_reg()
            halt=False
            pc_counter+=1
        elif(op_code == "01110"):
            reg1 = instruction[10:13:]  
            reg2 = instruction[13::]
            if getreg(reg1, False) < getreg(reg2, False):
                flagRegister = "0000000000000100"
            elif getreg(reg1, False) > getreg(reg2, False):
                flagRegister = "0000000000000010"
            else:
                flagRegister = "0000000000000001"
            halt=False
            pc_counter+=1
        elif(op_code == "01111"):
            # jmp unused mem_addr
            # 5   3      8
            memoryAddress = instruction[8::]
            (halt, pc_counter) = (False, int(memoryAddress,2))
            restore_default_reg()
        elif(op_code == "11100"):
            # jlt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000100":
                memoryAddress = instruction[8::]
                (halt, pc_counter) = (False, int(memoryAddress,2))
            else:
                (halt, pc_counter) = (False, pc_counter+1)
            restore_default_reg()
        elif(op_code == "11101"):
            # jgt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000010":
                memoryAddress = instruction[8::]
                (halt, pc_counter) = (False, int(memoryAddress,2))
            else:
                (halt, pc_counter) = (False, pc_counter+1)
            restore_default_reg()
        elif(op_code == "11111"):
            if flagRegister == "0000000000000001":
                memoryAddress = instruction[8::]
                (halt, pc_counter) = (False, int(memoryAddress,2))
            else:
                (halt, pc_counter) = (False, pc_counter+1)
            restore_default_reg()
        # ........................................................................................................................

        elif(op_code == "11010"):
            restore_default_reg()
            (halt, newpc) = (True, pc_counter+ 1)
        elif(op_code=="10000"):
                r1=j[7:10]
                r2=j[10:13]
                r3=j[13:16]
                a=getRegister(r2)
                b=getRegister(r3)
                if(op_code="00000"):
                        c=a+b
                        if(checkOverflow(c)):
                                setOverflow()
                        else:
                                index=registers.index(r1)
                                regvalue[index]=binaryconverter(c)
                elif(op_code="00001"):
                        c=a-b
                        if(checkOverflow(c)):
                                setOverflow()
                        else:
                                index=registers.index(r1)
                                regvalue[index]=binaryconverter(c)
#     memory = initialize_memory()
#     dump_memory(memory)
#     data = get_data(memory, 0)
#     print(data)
#     value = get_value_from_address(memory, '00000000')
#     print(value)
#     set_value_of_address(memory, '00000000', 42)
#     dump_memory(memory)
flagreg = "0000000000000000" 
def reset():
    global flagreg
    flagreg = "0000000000000000"
def setoverflow():
    global flagreg
    flagreg = "0000000000001000"
def setless():
    global flagreg
    flagreg = "0000000000000100"
def setmore():
    global flagreg
    flagreg = "0000000000000010"
def setequal():
    global flagreg
    flagreg = "0000000000000001"
def setreg(r, v):
    global register_dict
    if (not checkOverflow(value)):
        register_dict[r] = v
    else:
        rawBinary = bin(value)[2:]
        register_dict[r] = int(rawBinary[-16:], 2)
def getreg(registerAddress, binaryOrDecimal):
    global register_dict, flagreg
    if binaryOrDecimal:
        if registerAddress == "111":
            return flagreg
        rawBinary = bin(register_dict[registerAddress])[2:]
        if len(rawBinary) > 16:
            return rawBinary[-16:]
        else:
            return intToBinary16bit(register_dict[registerAddress])
    else:
        if registerAddress == "111":
            return int(flagreg, 2)
        return register_dict[registerAddress]
def dump():
    global register_dict, flagreg
    for key in register_dict.keys():
        print(intToBinary16bit(register_dict[key]), end=" ")
    print(flagreg)
def execute_program():
        global code
        memory = []
        for i in stdin:
                memory.append(i.rstrip("\n"))
        code=memory.copy()
        if len(memory) < 128:
                lineDiff = 128 - len(memory)
        while lineDiff:
                memory.append("0000000000000000")
                lineDiff=lineDiff-1
        pc = 0
        halted = False
        while not halted:
                instruction = format(memory[pc], "016b")  # Get current instruction
                halted, new_pc = execute(instruction)  # Execute the instruction
                dump_state()  # Print PC and RF state
                pc = new_pc if new_pc is not None else pc + 1  # Update PC
        dump_memory()
