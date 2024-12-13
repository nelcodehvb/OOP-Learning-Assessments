class ButteredShrimp:
    def __init__(self, shrimp, butter, garlic, parsley):
        self.__shrimp = shrimp
        self._butter = butter
        self.__garlic =garlic
        self.__parsley = parsley
    def __str__(self):
        return f'''My buttered shrimp has ingredients of {self.__shrimp}, {self._butter}, {self.__garlic} and {self.__parsley}.'''
    def may_garlic_ba(self):
        return self.__garlic
hipon = ButteredShrimp("hipon", "mantikilya","bawang", "parsley")
print(hipon.may_garlic_ba())