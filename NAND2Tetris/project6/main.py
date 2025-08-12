import sys
from Parser import Parser
from Code import Code
from symbol_table import SymbolTable

def main(input):
    """
    主函数执行解析器
    """
    try:
        #创建输出文件名
        output=input.replace('.asm','.hack')

        #初始化符号表和变量地址
        symbol_table=SymbolTable()
        next_ram_address=16

        with open(input,'r') as input_file,\
             open(output,'w') as output_file:
            #实例化对象
            parser = Parser(input_file)
            code=Code()
            #遍历所有指令
            while parser.has_more_commands():
                parser.advance()
                """
                if parser.current_command:
                    print(f"有效指令:{parser.current_command}")
                """
                command_type = parser.command_type()
                binary_code = ""

                #根据指令类型进行翻译
                if command_type == "A":
                    symbol_str = parser.symbol()
                    # 将十进制字符串转换为整数
                    decimal_value = int(symbol_str)
                    # 将整数转换为15位二进制，填充0
                    binary_value = bin(decimal_value)[2:].zfill(15)
                    #A指令以 ‘0’ 开头
                    binary_code = '0' + binary_value

                elif command_type == "C":
                    dst = parser.dest()
                    cmp = parser.comp()
                    jmp = parser.jump()

                    #使用Code类将助记符翻译成二进制代码
                    dst_bin = code.dest(dst)
                    cmp_bin = code.comp(cmp)
                    jmp_bin = code.jump(jmp)

                    #C指令以 '111'开头，然后拼接comp , dest , jump
                    binary_code = '111' + cmp_bin + dst_bin + jmp_bin

                #L指令不产生机器代码跳过
                elif command_type == "L":
                    continue

                #将生成的二进制代码写输入输出文件
                output_file.write(binary_code+'\n')
        print(f"汇编完成！输出文件{output}")

    except FileNotFoundError:
        #捕获文件找不到
        print("Add.asm文件找不到")
    except Exception as e:
        print(f"发生错误:{e}")

if __name__ == "__main__":
    #检查命令行确保传入文件
    if len(sys.argv)!=2:
        sys.exit(1)
    input_file=sys.argv[1]
    main(input_file)