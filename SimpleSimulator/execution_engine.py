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
