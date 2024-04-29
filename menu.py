
class Menu:
    def __init__(self, name: str, content: list):
        self.name = name
        self.content = content
        self.index = 0

    def display(self):
        result = f"\n{self.name}\n"
        result += "=" * 70 + "\n"
        for index, item in enumerate(self.content):
            if self.index == index:
                result += f"--> {item}\n"
            else:
                result += f"   {item}\n"
        return result

    def up(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.content) - 1

    def down(self):
        self.index += 1
        if self.index == len(self.content):
            self.index = 0
