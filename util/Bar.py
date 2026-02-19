# Min value is always 0
BAR_TOTAL_CHARS = 20
FILL_CHAR = "#"
EMPTY_CHAR = "-"

class Bar:
    def __init__(self, label, max):
        self.label = label
        self.max = max
    
    def render(self, value):
        percentage = value/self.max
        fill_chars = round(BAR_TOTAL_CHARS * percentage)
        empty_chars = round(BAR_TOTAL_CHARS - fill_chars)

        return f"{self.label}: [{FILL_CHAR * fill_chars}{EMPTY_CHAR * empty_chars}] ({round(percentage * 100)}%)"