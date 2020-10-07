class Matrix:

    def __init__(self, arg):
        self.my_list = arg.split('\n')

    def my_function(self):
        self.rows = []
        self.columns = []
        for item in self.my_list:
            self.rows.append(list(map(int, item.split(' '))))

        self.columns = list(zip(*self.rows))


example = Matrix('1 2 3\n4 5 6\n7 8 9')
example.my_function()
print(example.columns)
print(example.rows)

