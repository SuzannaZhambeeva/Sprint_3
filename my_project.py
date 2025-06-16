import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name(self):
        return self.__name_items
    
    @property
    def number(self):
        return self.__number_items
    
    @number.setter
    def number(self, value):
        self.__number_items = value
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.name.append(name)
            self.number += 1
    
    def delete_item_from_check(self, name):
        if name not in self.name:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.name.remove(name)
            self.number -= 1
    
    def check_amount(self):
        total=[]
        for item in self.name:
            price = self.item_price.get(item, 0)
            total.append(price)
        amount = sum(total)
        if self.number > 10:
            amount *= 0.9
        return amount
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.name:
            if self.tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)

        for item in twenty_percent_tax:
            total.append(self.item_price.get(item, 0))

        total_sum = sum(total)

        if self.number > 10:
            total_sum *= 0.9

        vat = total_sum * 0.2

        return vat
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.name:
            if self.tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
        
        for item in ten_percent_tax:
            total.append(self.item_price.get(item, 0))

        total_sum = sum(total)

        if self.number > 10:
            total_sum *= 0.9

        vat = total_sum * 0.1

        return vat
    
    def total_tax(self):
        tax_20 = self.twenty_percent_tax_calculation()
        tax_10 = self.ten_percent_tax_calculation()
        return tax_20 + tax_10
    
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            telephone_number = int(telephone_number)
        except:
            raise ValueError('Необходимо ввести цифры')
    
        number_str = str(telephone_number)
    
        if len(number_str) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
    
        number_str = number_str.zfill(10)
    
        return f'+7{number_str}'
