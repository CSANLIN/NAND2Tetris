# code.py
class Code:
    """
    Code 类，负责将 Hack 汇编语言的助记符翻译成二进制代码。
    """

    def __init__(self):
        """
        初始化所有助记符到二进制代码的映射表。
        """
        # dest 字段的映射表 (3 位)
        self.dest_map = {
            None: "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }

        # comp 字段的映射表 (7 位)
        self.comp_map = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "M": "1110000",
            "!D": "0001101",
            "!A": "0110001",
            "!M": "1110001",
            "D+1": "0011111",
            "A+1": "0110111",
            "M+1": "1110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "M-1": "1110010",
            "D+A": "0000010",
            "D+M": "1000010",
            "D-A": "0010011",
            "D-M": "1010011",
            "A-D": "0000111",
            "M-D": "1000111",
            "D&A": "0000000",
            "D&M": "1000000",
            "D|A": "0010101",
            "D|M": "1010101"
        }

        # jump 字段的映射表 (3 位)
        self.jump_map = {
            None: "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

    def dest(self, mnemonic):
        """
        将 dest 助记符翻译成 3 位二进制代码。
        :param mnemonic: dest 助记符字符串。
        :return: 3 位二进制代码。
        """
        # 使用 .get() 方法，如果找不到键，则返回默认值 "000"
        return self.dest_map.get(mnemonic, "000")

    def comp(self, mnemonic):
        """
        将 comp 助记符翻译成 7 位二进制代码。
        :param mnemonic: comp 助记符字符串。
        :return: 7 位二进制代码。
        """
        return self.comp_map.get(mnemonic)

    def jump(self, mnemonic):
        """
        将 jump 助记符翻译成 3 位二进制代码。
        :param mnemonic: jump 助记符字符串。
        :return: 3 位二进制代码。
        """
        return self.jump_map.get(mnemonic, "000")