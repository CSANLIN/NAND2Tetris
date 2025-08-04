// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

//在主循环检查键盘状态进行分支
(MAIN_LOOP)
    //加载键盘内存地址
    @KBD   
    D=M   

    //加载内循环，填充黑色
    @FILL_BLACK
    D;JNE

    //加载内循环，填充白色
    @FILL_WHITE
    0;JMP

(FILL_BLACK)
    //加载屏幕起始地址
    @SCREEN
    D=A
    //存储当前屏幕内存地址
    @currentAddress
    M=D

    //屏幕共有8192个16位字
    @8192
    D=A
    //循环计数器
    @counter
    //初始为末地址
    M=D
    //内循环，用于填充
    (LOOP_BLACK)
        //判断是否完成填充
        @counter
        D=M
        @MAIN_LOOP
        D;JEQ
        
        //当前变量地址
        @currentAddress
        A=M
        //填充黑色
        M=-1
        @currentAddress
        M=M+1

        @counter
        M=M-1
        
        @LOOP_BLACK
        0;JMP

(FILL_WHITE)
    @SCREEN
    D=A
    @currentAddress
    M=D

    @8192
    D=A
    @counter
    M=D
    (LOOP_WHITE)
        @counter
        D=M
        @MAIN_LOOP
        D;JEQ

        @currentAddress
        A=M
        M=0

        @currentAddress
        M=M+1

        @counter
        M=M-1
        
        @LOOP_WHITE
        0;JMP
