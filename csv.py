class CommaSeparatedValues:
    """
    This class takes is made to take a number
    and add the correct comma placement relating
    to hundreds, thousands, etc. and account for
    arbitrary decimal numbers
    """
    def __init__(self, num):
        self.num_str = str(num).split('.')
        self.output = ''
        self.output = self.insert_commas()

    def insert_commas(self):
        for pos, numeric in enumerate(self.num_str[0][::-1]):
            if not pos % 3 and pos != 0:
                self.output += ',' + numeric
            else:
                self.output += numeric
        self.output = self.output[::-1]
        if len(self.num_str) > 1:
            self.output += '.' + self.num_str[1]
        return self.output
