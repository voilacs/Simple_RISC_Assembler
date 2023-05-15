**Co project assignment** for implementing a simple assembler and simulator in python for the course CSE112 at IIITD.
This repository contains the files for implementing a simple assembler and simulator
**Group A9:**
1) Ansh Varshney  2022083
2) Dhawal Bansal  2022159
3) Dhawal Garg    2022160
4) Anmol Adarsh Kumar 2022081

opcodes
00000 Addition 
Performs reg1 =reg2 + reg3.
add reg1 reg2 reg3

00001 Subtraction 
Performs reg1 =reg2- reg3.
sub reg1 reg2 reg3

00010 Move Immediate
Performs reg1 =$Imm
where Imm is a 7 bit value.
mov reg1 $Imm

00011 Move Register
Move content of reg2 into reg1.
mov reg1 reg2

00100 Load 
Loads data from mem_addr into reg1.
ld reg1 mem_addr

00101 Store 
Stores data from reg1 to mem_addr.
st reg1 mem_addr

00110 Multiply 
Performs reg1 =reg2 x reg3.
mul reg1 reg2 reg3

00111 Divide 
Performs reg3/reg4.
div reg3 reg4

01000 Right Shift 
Right shifts reg1 by $Imm, 
where $Imm is a 7 bit value.
rs reg1 $Imm

01001 Left Shift 
Left shifts reg1 by $Imm, 
where $Imm is a 7 bit value.
ls reg1 $Imm

01010 Exclusive OR
Performs bitwise XOR of reg2 and reg3. 
Stores the result in reg1.
xor reg1 reg2 reg3

01011 Or 
Performs bitwise OR of reg2 and reg3. 
Stores the result in reg1.
or reg1 reg2 reg3

01100 And 
Performs bitwise AND of reg2 and reg3. 
Stores the result in reg1.
and reg1 reg2 reg3

01101 Invert 
Performs bitwise NOT of reg2.
Stores the result in reg1.
not reg1 reg2

01110 Compare 
Compares reg1 and reg2 and sets up the FLAGS register.
cmp reg1 reg2

01111 Unconditional Jump
Jumps to mem_addr,
where mem_addr is a memory address.
jmp mem_addr

11100 Jump if Less Than
Jump to mem_addr if the less than flag is set (less than flag = 1),
where mem_addr is a memory address.
jlt mem_addr

11101 Jump If Greater Than
Jump to mem_addr if the greater than flag is set (greater than flag = 1), 
where mem_addr is a memory address.
jgt mem_addr E

11111 Jump If Equal
Jump to mem_addr if the equal flag is set (equal flag = 1),
where mem_addr is a memory address.
je mem_addr E

11010 Halt 
Stops the machinefrom executing until reset
hlt F

For assigning a memory address to a variable we have used length of the code as first address and then kept incrementing it by 1.
For assigning a memory address to a label we have used the (line number -1) as the address of the label in that particular line.
