class ButteredShrimp:
    def __init__(self, shrimp, butter, garlic, parsley):
        self.shrimp = shrimp
        self._butter = butter
        self.__garlic =garlic
        self.__parsley = parsley
    def __str__(self):
        return f'''My buttered shrimp has ingredients of {self.__shrimp}, {self._butter}, {self.__garlic} and {self.__parsley}.'''
    def may_garlic_ba(self):
        return self.__garlic
       
    def i_set_to(self, bago):
         self.__garlic = bago
         
hipon = ButteredShrimp("hipon", "mantikilya","bawang", "parsley")
hipon.i_set_to("buong bawang")
print(hipon.may_garlic_ba())