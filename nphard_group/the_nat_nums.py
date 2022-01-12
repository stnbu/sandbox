
class X:

    cache = {}

    def __init__(self, value):
        self.value = value

    def get_next(self, other, gamma):
        import ipdb; ipdb.set_trace()
        x = secret_value()
        return X(self.value + other.value)
        

    def __add__(self, other):
        return self.get_next(other, list(range(0, self.value)))

    def __str__(self):
        return "X(%d)" % self.value

if __name__ == "__main__":

    x = X(0)
    y = X(29)
    z = X(30)
    print(y+z)