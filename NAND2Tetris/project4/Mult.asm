// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.

//初始化R2作为总和
@R2
M=0
// 检查特殊情况：如果 R1 为 0，乘积就是 0，直接结束
@R1
D=M
@EMD
D;JEQ

//循环开始
(LOOP)
@R1
D=M
//如果已经加载到0就结束
@END
D;JEQ

@R0
D=M
@R2
M=D+M
@R1
M=M-1
@LOOP
0;JMP

(END)
@END
0;JMP



