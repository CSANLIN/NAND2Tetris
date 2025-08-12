# symbol_table.py
class SymbolTable:
    """
    符号表类，负责存储所有符号（预定义符号、标签、变量）及其对应的内存地址。
    """

    def __init__(self):
        """
        初始化符号表，并预先填入 Hack 平台的所有预定义符号。
        """
        self.table = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4,
            "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9,
            "R10": 10, "R11": 11, "R12": 12, "R13": 13,
            "R14": 14, "R15": 15,
            "SCREEN": 16384, "KBD": 24576
        }

    def add_entry(self, symbol, address):
        """
        将一个新的符号和地址添加到符号表中。
        :param symbol: 符号名称（字符串）。
        :param address: 内存地址（整数）。
        """
        self.table[symbol] = address

    def contains(self, symbol):
        """
        检查符号表中是否包含某个符号。
        :param symbol: 符号名称（字符串）。
        :return: 如果符号存在，返回 True；否则返回 False。
        """
        return symbol in self.table

    def get_address(self, symbol):
        """
        返回符号对应的地址。
        :param symbol: 符号名称（字符串）。
        :return: 符号对应的地址（整数）。
        """
        return self.table.get(symbol)