import re


class Person:
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise ValueError("名前は文字列でなければなりません。")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value,int) or value < 0:
            raise ValueError("年齢は0以上の整数でなければなりません。")
        self._age = value
