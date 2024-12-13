class ButteredShrimp:
    def __init__(self, shrimp, butter, garlic, parsley):
        self.__shrimp = shrimp
        self.__butter = butter
        self.__garlic =garlic
        self.__parsley = parsley
    def __str__(self):
        return f'''My buttered shrimp has ingredients of {self.__shrimp}, {self.__butter}, {self.__garlic} and {self.__parsley}.'''
       
hipon = ButteredShrimp("hipon", "mantikilya","bawang", "parsley")
print(hipon)
