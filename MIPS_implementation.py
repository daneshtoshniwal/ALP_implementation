#Program for multiplication of two numbers and storing
#the absolute value of its product in a memory location

'''INPUT FOR MULTIPLICATION OF 10 NUMBERS
AND DETERMINE THE ABSOLUTE VALUE OF THE PRODUCT:

100 -1
101 1
102 2
103 3
104 4
105 5
106 6
107 -7
108 8
109 9
110 10
111 0
begin
1 LOAD MQ,M(101) NOP
2 MUL M(102) NOP
3 MUL M(103) NOP
4 MUL M(104) NOP
5 MUL M(105) NOP
6 MUL M(106) NOP
7 MUL M(107) NOP
8 MUL M(108) NOP
9 MUL M(109) NOP
10 MUL M(110) NOP
11 LOAD MQ NOP
12 JUMP+ M(15,0:19) NOP
13 MUL M(100) NOP
14 LOAD MQ NOP
15 STOR M(111) NOP
halt

'''

#--------Function unrelated to the main program
def binaryToDecimal(binary):

    decimal = 0
    i = 0
    while(binary != 0):
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, i)
        binary = int(binary)//10
        i += 1
    return(decimal)
#----------------------------------------------


#The assembler has a task of converting the opcodes into binary form,
#as pre-defined values.
#I also added the function of converting the address in the instruction
#into 12 bit binary number.
def assembler(str1):
    if(str1 == "LOAD"):
        return("00000001")
    elif(str1 == "ADD"):
        return("00000101")
    elif(str1 == "STOR"):
        return("00100001")
    elif(str1 == "MUL"):
        return("00001011")
    elif(str1 == "MQ,"):
        return("00001001")
    elif(str1 == "MQ"):
        return("00001010")
    elif(str1 == "JUMP+"):
        return("00001111")
    else:
        return((12-len(bin(int(str1)).replace("0b","")))*"0"+bin(int(str1)).replace("0b",""))



#It carries out the maximum task of this program.
def processor(str1):
    # Condition when instruction is of 40 bits (both LHS and RHS are present)
    if(str1[-1]!="NOP"): 
        global IR
        global IBR
        global MAR
        global MBR
        global address_data
        global accumulator
        global MQ
        global PC
        global negative_checker

        #If the str1 = "1 LOAD M(100) ADD M(101)", 
        #IR will store the binary of LOAD
        #MAR will store the binary of address 100
        #IBR will store the binary of the entire RHS instruction,
        #which is ADD M(101)
        IR = assembler(str1[1])  # The binary of the opcode is stored.
        print("The opcode of LHS:",IR,"(",str1[1],")",",goes into IR(Instruction Register)")

        MAR = assembler(str1[2][2:-1])
        print("The address of LHS:",MAR,"(",str1[2][2:-1],")",",goes into MAR(Memory Address Register)")

        IBR = assembler(str1[3])+" "+assembler(str1[4][2:-1])
        print("The 20 bit RHS part of the instructions:",IBR,"(",str1[3]," ",str1[4],")",",goes into IBR")

        #The required operations take place in 
        #accordance with that given opcode.
        print("Executing the LHS of the instruction")
        #Conditions of IR and MAR:
        if IR == "00000001":  #LOAD
            accumulator = address_data[int(str1[2][2:-1])]
        elif IR == "00000101":#ADD
            accumulator += address_data[int(str1[2][2:-1])]
        elif IR == "00100001":#STOR
            address_data[int(str1[2][2:-1])] = accumulator

        #Printing the content of accumulator after the decode and execute part of the LHS
        print("(after LHS)Accumulator:",accumulator)

        #Now coming on the the RHS part of the instruction:
        #The instruction stored in IBR is shifted to IR and MAR and
        #it is again decoded and executed as previously mentioned.
        print("Now the content of IBR shitfs to IR and MAR")
        IBR=IBR.split()
        IR=IBR[0]
        MAR=IBR[1]
        #Conditions of IBR (now IR and MAR):
        if IR == "00000001":  #LOAD
            accumulator = address_data[int(str1[4][2:-1])]
        elif IR == "00000101":#ADD
            accumulator += address_data[int(str1[4][2:-1])]
        elif IR == "00100001":#STOR
            address_data[int(str1[4][2:-1])] = accumulator

        #Printing the content of accumulator after the decode and execute part of the LHS
        print("(after RHS)Accumulator:",accumulator)
        

    else: #Condition when only 20 bits of instruction is present!


        #This if statement is for LOAD MQ,M(X)
        #I have separated it from other instructions as to differentiate
        #between LOAD MQ,M(X)  and   LOAD opcodes.
        if(str1[1]=="LOAD" and str1[2][:3]=="MQ,"):  #Using some trick to obtain the opcode for LOAD MQ,M(X)
            IR = assembler(str1[2][:3])  # The binary of the opcode is stored.
            print("The opcode of LHS:",IR,"(",str1[1],"MQ,M )",",goes into IR(Instruction Register)")

            MAR = assembler(str1[2][5:-1])
            print("The address of LHS:",MAR,"(",str1[2][5:-1],")",",goes into MAR(Memory Address Register)")

            MQ = address_data[int(str1[2][5:-1])]
            print("MQ:",MQ)
            

        elif(str1[1]=="LOAD" and str1[2][:2]=="MQ"):  #Using some trick to obtain the opcode for LOAD MQ,M(X)
            IR = assembler(str1[2][:2])  # The binary of the opcode is stored.
            print("The opcode of LHS:",IR,"(",str1[1],"MQ )",",goes into IR(Instr1uction Register)")
            
            accumulator = MQ

            if(negative_checker%2==1):
                accumulator = -accumulator
                
            print("Accumulator:",accumulator)
            print("MQ:",MQ)


        #It has the other opcodes including:
        #LOAD, ADD, STOR, JUMP+, MUL
        else:
            if(str1[1]=="JUMP+"): 
                IBR = assembler(str1[1])+" "+assembler(str1[2][2:-6])
            else:
                IBR = assembler(str1[1])+" "+assembler(str1[2][2:-1])
            
            print("The 20 bits instr1uction:", IBR,"(",str1[1]," ",str1[2][2:-6],")",",was shifted to IBR earlier")
            print("But as the IR and MAR have become empty now, the content of IBR shifts there")
            IBR=IBR.split()
            IR=IBR[0]
            MAR=IBR[1]

            if IR == "00000001":  #LOAD
                accumulator = address_data[int(str1[2][2:-1])]
            elif IR == "00000101":#ADD
                accumulator += address_data[int(str1[2][2:-1])]
            elif IR == "00100001":#STOR
                address_data[int(str1[2][2:-1])] = accumulator

            elif IR == "00001111":#JUMP+
                if(negative_checker%2==0):
                    PC = int(str1[2][2:-6])
                print("PC:",PC)

            elif IR == "00001011":#MUL
                #Logic of multiplication:
                a=address_data[int(str1[2][2:-1])]

                s = MQ*a
                bin_of_s = bin(s).replace("0b","")
                
                local_negative = 0

                if bin_of_s[0]=="-":
                    local_negative += 1
                    bin_of_s = bin_of_s.replace("-","")

                bin_of_s = (80-len(bin_of_s))*"0" + bin_of_s
                
                if local_negative == 0:
                    accumulator = bin_of_s[0:40]
                    MQ = bin_of_s[40:80]
                else:
                    accumulator = bin_of_s[0:39] + "1" 
                    #For ease of the program, instead of adding 1 at
                    #the leftmost position of accumulator, i have added 1 
                    #at the last position of accumulator's content.
                    MQ = bin_of_s[40:80]
                    negative_checker += 1
                
                accumulator = binaryToDecimal(accumulator)
                MQ = binaryToDecimal(MQ)
                #The MSB half part of product is stored in MQ and
                #the LSB half part of product is stored in accumulator

                if(accumulator == 1):
                    accumulator = -1
            
            print("Accumulator:",accumulator)
            if(MQ!=""):
                print("MQ:",MQ)


# This is the Main Memory M implemented in a dictionary.
address_data = {}
# It contains the addresses and the content stored in them.
# 0 contains the length of the rectangle,
# 1 contains the breadth of the rectangle.

IR = ""
MAR = ""
IBR = ""
MBR = ""
MQ=""
accumulator=0
negative_checker = 0

str1=""

my_list=[]

while(True):
    str1=input().split()
    if(str1[0]=="begin"):
        break
    address_data[int(str1[0])]=int(str1[1])
    #This adds the content and the address in the address_data dictionary

while(True):
    str1=input()
    if(str1=="halt"):
        break
    my_list.append(str1.split())

PC = 1 
for i in range(1,int(my_list[-1][0])+1):
    for j in range(1,int(my_list[-1][0])+1):
        if(int(my_list[j-1][0])==PC):
            print("\n(Program Counter) PC =", PC)
            MAR=PC
            PC+=1
            print("The value of PC goes to MAR")
            processor(my_list[j-1])
            print("Memory Locations and their content: ",address_data)
    
print("\nAccumulator:",accumulator,";  MQ:",MQ)