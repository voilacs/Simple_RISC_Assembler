def binaryconverter(number):
    l=[]
    while number!=0:
        rem=str(number%2)
        l.append(rem)
        number=number//2
    l.reverse()        
    while len(l) < 8:
        l.insert(0,'0')
    binary_string = ''.join(l)
    return binary_string
def reg_address(register):
    '''
    Use A capital letter + a number to refer to a register into the function 
    '''
    registers=['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'FLAGS']
    values=['000', '001', '010', '011', '100', '101', '110', '111']
    for i in range(8):
        if(register==registers[i]):
            return values[i]
    return -1
x=reg_address('R5')
print(x)
def opcode_return(cmd,move_type="null"):
    #imm for immediate and reg for register
    instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
    opcode=["00000","00001",["00010","00011"],"00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","11100","11101","11111","11010"]
    a=instructions.index(cmd)
    if(a==2):
        if(move_type=="imm"):
            return opcode[2][0]
        else:
            return opcode[2][1]
    else:
        return opcode[a]
       
