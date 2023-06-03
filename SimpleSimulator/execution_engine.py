import math
# line 30 tak sab kuchh bas initialize hi ho raha hai uske baad code hai kuch
# jump ke alawa saare opcodes ke liye pc_counter+=1 zaroor karein
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
