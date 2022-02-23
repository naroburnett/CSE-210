from log import Log
class Item:


    def __init__(self,name,price,calorie,code,exp_date,type):
        self._name = name
        self._price = price
        self._calorie = calorie
        self._code = code
        self._exp_date = exp_date
        self._type = type

    def get_price(self):
        return self._price

ham_sand = Item("Ham Sandwich",5.99,200,"ABCD","2022-02-07 15:00","Sandwich")
print(ham_sand.__dict__)

mt_dew = Item("Mountain Dew",0.69,250,"MTDEWRULZ","2052-01-01 03:00", "Drink")
print(mt_dew.__dict__)

log = Log("3:00","2022-02-07",mt_dew)
print([ m for m in dir(Item) if not m.startswith('__')])