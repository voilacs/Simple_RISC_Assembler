import sys
l_=[]
def assembly_code(number):
	for i in range(1,100):
		l_.append(" ")
def binaryconverter(number):
    l=[]
    while number!=0:
        rem=str(number%2)
        l.append(rem)
        number=number//2
    l.reverse()        
    while len(l) < 7:
        l.insert(0,'0')
    binary_string = ''.join(l)
    return binary_string
def decimal_to_floating_point(decimal_number):
    decimal_number = abs(decimal_number)
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part
    integer_binary = binaryconverter(integer_part)  # Remove the "0b" prefix
    fractional_binary = ""
    while fractional_part != 0:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
    binary_representation = integer_binary + "." + fractional_binary
    if len(binary_representation) > 8:
        return 2
    integer_part = binary_representation.split(".")[0]
    fractional_part = binary_representation.split(".")[1]
    exponent = len(integer_part) - 1
    bias = 2**(3 - 1) - 1
    exponent_ = exponent + bias
    integer_part_5bit = integer_part[1:].zfill(3)
    fractional_part_5bit = fractional_part[:5].ljust(5, "0")
    floating_point_representation = bin(exponent_)[2:].zfill(3) + integer_part_5bit + fractional_part_5bit
    return floating_point_representation
def decimal(num):
	while num > 1:
		num /= 10
	return num
def reg_address(register):
    #Use A capital letter + a number to refer to a register into the function 
    registers=['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'FLAGS']
    values=['000', '001', '010', '011', '100', '101', '110', '111']
    for i in range(8):
        if(register==registers[i]):
            return values[i]
    return -1
def object_reader(number):
	x=number%10
	y+=str(x)
	number/=10
def opcode_return(cmd,move_type="null"):
    #imm for immediate and reg for register
    instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt","addf","subf","movf"]
    opcode=["00000","00001",["00010","00011"],"00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","11100","11101","11111","11010","10000","10001","10010"]
    a=instructions.index(cmd)
    print
    if(a==2):
        if(move_type=="imm"):
            return opcode[2][0]
        else:
            return opcode[2][1]
    return opcode[a]
    
def InstructionType(ins, isRegister= -1):
    if(isRegister==0):
        return 'b'
    elif (isRegister==1):
        return 'c'
    l1=["add", "sub", "mul", "xor", "or", "and","addf","subf"]
    l2=["mov", "rs", "ls","movf"]
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
      return -1
Asscode=[]
tmp_vars=[]
errors=[]
vars=dict()
labels=dict()
tmp_labels=[]
binary=[]
r1=sys.stdin.readlines()
for i in r1:
    i=i.rstrip("\n")
    Asscode.append(i)
tmp=0
lab=0
asscode=[i for i in Asscode if (i)] #removing blank lines
def assembly_code_(number2):
    p=0
    l__=[]
    for j in range(1,number2*(2**p)):
        l__.append(str(p*2))
        p+=1
for i in range(len(Asscode)):
    j=Asscode[i].split()
    if(j[0]!="var"):
        r=i
        break
    elif(j[0]=="var" and len(j)==2):
        tmp_vars.append(j[1])
    elif(j[0]=="var" and len(j)!=2):
        errors.append(f'Error in line {i+1} : Invalid declaration of variable')
for i in tmp_vars:
    vars[i]=binaryconverter(tmp)
    tmp+=1
    Asscode.pop(0)
for i in range(len(Asscode)):
    j=Asscode[i].split()
    if j[0][-1]==':' and j[0][0:len(j[0])-1] not in tmp_labels:
        tmp_labels.append(j[0][0:len(j[0])-1])
        labels[j[0][0:len(j[0])-1]]=binaryconverter(i)
    elif j[0][-1]==':' and j[0][0:len(j[0])-1] in tmp_labels:
        errors.append(f'Error in line {i+1} : Multiple usage of same labels')
    elif ":" in j:
        errors.append(f'Error in line {i+1} : invalid declaration of label')
    elif(InstructionType(j[0])=='e' and j[1][0:len(j[1])-1] not in tmp_labels):
        tmp_labels.append(j[0][0:len(j[0])-1])
        labels[j[0][0:len(j[0])-1]]=binaryconverter(i)
halt=0
var_loc=len(Asscode)
for i in vars:
    vars[i]=binaryconverter(var_loc)
    var_loc+=1       
for i in range(len(Asscode)-1):
    j=Asscode[i].split()
    if(j[0]=="var"):
        errors.append(f'Error at line {i+tmp+1} : Variables not declared at the beginning')
        continue
    if (j[0] == "mov" and len(j) == 3):
        if (reg_address(j[2]) != -1):
            if (reg_address(j[1])==-1):
                errors.append(f'Error in line {i+tmp+1} : Typo in register name')
            elif(reg_address(j[1]) == "111"):
                errors.append(f'Error in line {i+tmp+1} : Illegal use of FLAGS register')
            elif(reg_address(j[1]) != -1 and reg_address(j[2]) != -1):
                binary.append(opcode_return(j[0], "reg") + "00000" + reg_address(j[1]) + reg_address(j[2]))
            continue
        elif (j[2][1:len(j[2])].isdecimal()):
            a=int(j[2][1:len(j[2])])
            if (reg_address(j[1]) == -1):
                errors.append(f'Error in line {i+tmp+1} : Typo in register name')
            elif(reg_address(j[1]) == "111"):
                errors.append(f'Error in line {i+tmp+1} : Illegal use of FLAGS register')
            elif (a < 0 or a > 127):
                errors.append(f'Error in line {i+tmp+1} : Immediate value out of range')
            elif(j[2][0]!="$"):
                errors.append(f'Error in line {i+tmp+1} : Wrong syntax for immediate value')
            elif(reg_address(j[1]) != -1 and a>=0 and a<=127):
                binary.append(opcode_return(j[0],"imm") +"0"+ reg_address(j[1]) + binaryconverter(a))
            continue
    elif(j[0]=="movf" and len(j)==3):
        a=float(j[2][1:len(j[2])])
        if (reg_address(j[1]) == -1):
                errors.append(f'Error in line {i+tmp+1} : Typo in register name')
        elif(reg_address(j[1]) == "111"):
                errors.append(f'Error in line {i+tmp+1} : Illegal use of FLAGS register')
        elif(j[2][0]!="$"):
                errors.append(f'Error in line {i+tmp+1} : Wrong syntax for immediate value')
        elif(decimal_to_floating_point(a)==2):
                errors.append(f'Error in line {i+tmp+1} : Floating point cannot be represented using 8 bits')
        elif(reg_address(j[1]) != -1):
                binary.append(opcode_return(j[0]) +reg_address(j[1]) + decimal_to_floating_point(a))
        continue
    elif (j[0] == "mov" and len(j)!=3 ):
        errors.append(f'Error in line {i+tmp+1} : Syntax Error')
        continue
    if (InstructionType(j[0]) == 'a' and len(j)!=4):
      errors.append(f'Error in line {i+tmp+1}: Syntax error')
    elif (InstructionType(j[0]) == 'a' and len(j) == 4):
            if (reg_address(j[1]) == -1 or reg_address(j[2]) == -1 or reg_address(j[3]) == -1):
              errors.append(f'Error in line {i+tmp+1}: Register not valid')
            elif (reg_address(j[1]) == "111" or reg_address(j[2]) == "111" or reg_address(j[3]) == "111"):
              errors.append(f'Error in line {i+tmp+1}: Invalid flag')
            else:
              binary.append(opcode_return(j[0]) + "00" + reg_address(j[1]) + reg_address(j[2]) + reg_address(j[3]))

    if (InstructionType(j[0]) == 'b' and len(j)!=3):
      errors.append(f'Error in line {i+tmp+1}: Invalid syntax')
      continue
    elif (InstructionType(j[0]) == 'b' and len(j) == 3):
      if(reg_address(j[1])==-1):
        errors.append(f'Error in line {i+tmp+1}: Register not valid')
        continue
      if (j[2][0] != "$"):
        errors.append(f'Error in line {i+tmp+1}:Syntax Invalid')
        continue
      if(int(j[2][1::]) not in range(0,128)):
        errors.append(f'Error in line {i+tmp+1}: Immediate value wrong')
        continue
      if(reg_address(j[1]) == "111"):
        errors.append(f'Error in line {i+tmp+1}: Flag invalid')
        continue
      binary.append(opcode_return(j[0]) +'0'+ reg_address(j[1]) + binaryconverter(int(j[2][1::])))
    if (InstructionType(j[0]) == 'c' and len(j)!=3):
        errors.append(f'Error in line {i+tmp+1}: Syntax used for instruction is wrong')
        continue
    elif (InstructionType(j[0]) == 'c' and len(j) == 3):
        if (reg_address(j[1]) == -1 or reg_address(j[2]) == -1):
            errors.append(f'Error in line {i+tmp+1}: Register is invalid')
            continue
        if(reg_address(j[1]) == "111" or reg_address(j[2]) == "111"):
            errors.append(f'Error in line {i+tmp+1}: Illegal usage of flags')
            continue
        binary.append((opcode_return(j[0]) + "00000" + reg_address(j[1]) + reg_address(j[2])))
        continue
    if (InstructionType(j[0]) == 'd' and len(j)!=3):
        errors.append(f'Error in line {i+tmp+1}: Wrong syntax used for instruction')
        continue
    elif (InstructionType(j[0]) == 'd' and len(j) == 3):
        if (reg_address(j[1]) == -1):
            errors.append(f'Error in line {i+tmp+1}: Invalid register')
            continue
        if(reg_address(j[1]) == "111"):
            errors.append(f'Error in line {i+tmp+1}: Illegal use of flags')
            continue
        if (j[2] not in vars):
            if(j[2] in labels.keys()):
                errors.append(f'Error in line {i+tmp+1}: Label misused as variable')
                continue
            else:
                errors.append(f'Error in line {i+tmp+1}: Variable used is undefined')
                continue
        else:
            binary.append((opcode_return(j[0]) +"0"+ reg_address(j[1]) + vars[j[2]]))
            var_loc+=1
            continue
    if(InstructionType(j[0])=='e'):
        if(len(j)!=2):
            errors.append(f'Error in line {i+tmp+1} : Syntax Error')
            continue
        else:
            if(j[1] not in labels.keys()):
                errors.append(f'Error in line {i+tmp+1} : Use of undefined labels')
                continue
            else:
                if(j[0] in vars.keys()):
                    errors.append(f'Error in line {i+tmp+1} : Misuse of variable as label')
                else:
                    binary.append(opcode_return(j[0])+'0'*4+labels[j[1]])  
                continue
    if j[0][-1]==':':
        label_inst=InstructionType(j[1])
        if(label_inst=="a"):
            binary.append(opcode_return(j[1]) + "00" + reg_address(j[2]) + reg_address(j[3]) + reg_address(j[4]))
        elif(label_inst=='b'):
            binary.append(opcode_return(j[1],"imm") +'0'+ reg_address(j[2]) + binaryconverter(int(j[3][1::])))
        elif(label_inst=='c'):
             binary.append(binaryconverter(opcode_return(j[1],"reg") + "00000" + reg_address(j[2]) + reg_address(j[3])))
        elif(label_inst=='d'):
            binary.append((opcode_return(j[1]) +"0"+ reg_address(j[2]) + vars[j[3]]))
            var_loc+=1
        elif(label_inst=='e'):
           binary.append(opcode_return(j[1])+'0'*4+labels[j[2]])
        continue  
    if (InstructionType(j[0])=='f'):
        errors.append(f'Error in line {i+tmp+1} : Hlt not being used as the last instruction')
        halt+=1
    elif(InstructionType(j[0])==-1):
        errors.append(f'Error in line {i+tmp+1} : Invalid operand')
if(InstructionType(asscode[-1])=='f'):
    j=asscode[-1].split()
    if(len(j)!=1):
        errors.append(f'Error in line {i+tmp+1} : Syntax Error')
        halt=1
    else:
        binary.append(opcode_return(j[0])+'0'*11)
        halt=1
elif(asscode[-1].split()[0][-1]==':' and InstructionType(asscode[-1].split()[1])=="f"):
        binary.append(opcode_return("hlt")+'0'*11)
        halt=1
if(halt==0):
    errors.append(f'Error : Halt instruction missing')
if(len(binary)>128):
    print("ERROR: Length of code out of range(>128)")
elif (len(errors)!=0):
    for i in errors:
        sys.stdout.write(str(i)+"\n")
else:
    for i in binary:
        sys.stdout.write(str(i)+"\n")
