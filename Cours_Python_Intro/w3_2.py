class Value:
    def __get__(self, obj, value):
        return self.value * (1 - obj.commission)

    def __set__(self, obj, value):
        self.value = value
