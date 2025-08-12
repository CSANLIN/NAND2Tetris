class Parser:
    def __init__(self,input_file):
        """
        初始化解析器，接收一个文件对象
        :param input_file: add.asm
        """
        self.file=input_file
        self.current_command=""
        self.commands=self.file.readlines() #读取所有行到一个列表
        self.line_number=-1
    def has_more_commands(self):
        """
        检查是否还有更多需要处理的指令
        :return: 如果行号小于总行数减一说明还有更多行
        """
        return self.line_number<len(self.commands)-1
    def advance(self):
        """
        读取下一条有效指令，跳过注释和空行
        :return:
        """
        self.line_number+=1
        print(f"尝试处理第 {self.line_number} 行：{self.commands[self.line_number].strip()}")
        while self.line_number<len(self.commands):
            #获取当前行并移除首尾的空白字符（包括空格和换行符）
            line=self.commands[self.line_number].strip()
            #判断是否为有效指令
            #line.split("//")：如果一行是 D=A //注释，split("//")
            # 会把它分割成 ['D=A ', '注释'] 这样的列表
            #[0]只读取D=A,.strip()移除D=A后面的空格
            if line and not line.startswith("//"):
                self.current_command=line.split("//")[0].strip()
                return
            self.line_number+=1
         #设置为空字符串，表示没有更多指令
        self.current_command=""

    def command_type(self):
        """
        返回当前的指令类型
        :return: A C L EMPTY
        """
        command=self.current_command
        if not command:
            return "EMPTY_OR_COMMENT"
        if command.startswith('@'):
            return "A"
        if command.startswith('(') and command.endswith(')'):
            return "L"
        return "C"

    def symbol(self):
        """
        当前指令的符号或十进制值
        :return: A-->@后面的内容
        L-->()里面的内容
        """
        command_type=self.command_type()
        if command_type == "A":
            return self.current_command[1:] #去掉开头'@'
        if command_type == "L":
            return self.current_command[1:-1]#去掉开头结尾（）
        return None

    def dest(self):
        """
        :return:当前C指令的dest字段
        """
        if self.command_type() == "C":
            if '=' in self.current_command:
                #如果有等号,dest在等号左边
                return self.current_command.split('=')[0]
            return None
        return None
    def comp(self):
        """
        :return:当前c指令的comp字段
        """
        if self.command_type() == "C":
            comp_part=self.current_command
            if '=' in comp_part:
                comp_part = comp_part.split('=')[1]
            if ';' in comp_part:
                comp_part = comp_part.split(';')[0]
            return comp_part
        return None

    def jump(self):
        """
        :return:jump字段
        """
        if self.command_type() == "C":
            if ';' in self.current_command:
                return self.current_command.split(';')[1]
            return None
        return None
