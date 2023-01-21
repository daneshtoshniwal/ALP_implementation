# ALP_implementation
MIPS IAS is implemented in python language
____________________________________________

The registers involved in IAS computer are:
AC  : Accumulator
	Accumulate/hold results of an ALU operation

IR  : Instructions Register
	8 bit opcode of the instruction to be executed
	
IBR : Instructions Buffer register
	Holds the RHS instruction temporarily

MQ  : Multiplier/Quotioent Register
	LSB of product

MBR : Memory BUffer register
	Contains a word to be read/stored in memory or I/O

MAR : Memory Adress register
	Specifies the address in memory of the word to be written/read into MBR

PC  : Program Counter
	Holds the next instruction’s address

_______________________________________________________________


Program: To multiple any number of numbers and return the absolute value of the product.
In the specific example, I have multiplied 10 numbers (1 to 10) with 7 interchanged with -7


----------------------- E X P L A I N A T I O N ------------------------

I have stored -1 in 100 memory location for future purposes.

You can store any number of values by your choice in the next few lines, I have taken 10 of them.
I have taken memory location 111 to store the final product.
begin starts the program.

I store the value at 101 in MQ and start multiplying all numbers to MQ,
and consecutively storing the product(40-40 bits) in the accumulator and MQ.
Then finally, I load the value of MQ in the accumulator. If it is negative, the instructions
at PC=12,13 and 14 will execute, and the accumulator's value will be multiplied by -1, which
was earlier stored in memory location 100

And at last, with the 15th instruction, the content of the accumulator is stored in memory location 111.

(If we made the memory location (110 10) to (110 -10), the product will be positive, 
and so, the JUMP instruction will shift the control to the 15th instruction.)




_______________________________________________________________

Another program:
To calculate the perimeter and area of a rectangle
100 and 101 contain length and breadth, so they can be varied.
the perimeter (PC: 1 to 6) will be stored at 104 and
the area (PC: 7 onwards) will be stored at 106

------------- E X P L A I N A T I O N --------------

To calculate the perimeter of a rectangle, the formula is: 2*(length+breadth)
So we load the length in the accumulator, then add the breadth to the accumulator
then we multiply the sum by 2 (constant which was stored in location 102)
and finally, store the value of the accumulator or the answer in the memory location 104.

To calculate the area of a rectangle, the formula is: length*breadth
So we load the length in the accumulator and store it in location 105
then we load the breadth M(101) in MQ as we have to multiply it to the length
then we multiply M(105) with the content of MQ, that is,
we multiple length by breadth.
then we store the content of MQ to accumulator as generally, the product
will be under 20 bits and so, the content of the accumulator would be 0

_______________________________________________________________
