import sys
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
    
def typeOfInstruction(ins, isRegister= -1):
    if(isRegister==0):
        return 'b'
    elif (isRegister==1):
        return 'c'
    l1=["add", "sub", "mul", "xor", "or", "and"]
    l2=["mov", "rs", "ls"]
    l3=["mov", "div", "not", "cmp"]
    l4=["ld", "st"]
    l5=["jmp", "jlt", "jgt", "je"]
    l6=["hlt"]
    if ins in l1:
      return 'a'
    elif ins in l2:
      return 'b'
    elif ins in l3:
      return 'c'
    elif ins in l4:
      return 'd'
    elif ins in l5:
      return 'e'
    elif ins in l6:
      return 'f'
    else:
      return -1;
Asscode=[]
tmp_vars=[]
errors=[]
vars=dict()
for i in sys.stdin:
    Asscode.append(i)
tmp=len(Asscode)
asscode=[i for i in Asscode if (i)] #removing blank lines
for i in range(len(Asscode)):
    j=Asscode[i].split()
    if(j[0]=="var" and len(j)==2 and j[1] not in tmp_vars):
        tmp_vars.append(j[1])
    elif(j[0]=="var" and len(j)==2 and j[1] in tmp_vars):
        errors.append(f'Error in line {i+1} : Multiple usage of same variable')
    elif(j[0]=="var" and len(j)!=2):
        errors.append(f'Error in line {i+1} : Invalid declaration of variable')
for i in tmp_vars:
    vars[i]=binaryconverter(tmp)
    tmp+=1
