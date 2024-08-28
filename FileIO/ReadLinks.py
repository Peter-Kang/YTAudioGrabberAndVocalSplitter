# class to read in the input and turn it into an array of strings to scrap

class ReadLinks:
    def __init__(self):
        self.FILENAME = "input.txt"
        self.Results = []
    
    def ReadIn(self):
        self.Results = []
        try:
            inputFileLinks = open(self.FILENAME, 'r')
            Lines = inputFileLinks.readlines()
            for line in Lines:
                self.Results.append(line)
        except Exception as error:
            print(error)
        return self.Results