import secrets
import random
class convert():
    def str_to_list(string):
        list1=[]
        list1[:0]=string
        return list1

    def list_to_str(list):
        key=''.join([str(x) for x in list])
        return key

def key(size,number=True,upper=True,symbol=True,lower=True):
    lower_ = 0
    upper_ = 0
    number_ = 0
    symbol_ = 0
    _lower_ = ''
    _upper_ = ''
    _number_ = ''
    _symbol_ = ''
    if number == True:
        number = '1234567890'
    if upper == True:
        upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if symbol == True:
        symbol = '@#$%&!'
    if lower == True:
        lower = 'qwertyuiopasdfghjklzxcvbnm'
    if number == False:
        number = ""
    if upper == False:
        upper = ""
    if symbol == False:
        symbol = ""
    if lower == False:
        lower = ""
    if type(number) == str:
        number = number
    if type(upper) == str:
        upper = upper
    if type(symbol) == str:
        symbol = symbol
    if type(lower) == str:
        lower = lower
    if type(number) == int:
        number_ = number
        _number_ = random.choices('1234567890', k = number)
        number = ''
    if type(upper) == int:
        upper_ = upper
        _upper_ = random.choices('QWERTYUIOPASDFGHJKLZXCVBNM', k = upper)
        upper = ''
    if type(symbol) == int:
        symbol_ = symbol
        _symbol_ = random.choices('@#$%&!', k = symbol)
        symbol = ''
    if type(lower) == int:
        lower_ = lower
        _lower_ = random.choices('qwertyuiopasdfghjklzxcvbnm', k = lower)
        lower = ''
    if size < lower_ + upper_ + number_ + symbol_:
        raise Exception("Can't the size is higher than it requirement")
    _number_ = convert.str_to_list(_number_)
    _upper_ = convert.str_to_list(_upper_)
    _lower_ = convert.str_to_list(_lower_)
    _symbol_ = convert.str_to_list(_symbol_)
    number = convert.str_to_list(number)
    upper = convert.str_to_list(upper)
    lower = convert.str_to_list(lower)
    symbol = convert.str_to_list(symbol)
    key = []
    all_ = _number_ + _upper_ + _lower_ + _symbol_
    all = number + upper + lower + symbol
    try:
        for i in range(0,size-(lower_ + upper_ + number_ + symbol_)):
            random.shuffle(all)
            shuff = secrets.choice(all)
            key.append(shuff)
    except IndexError:
        key = []
    key = key
    all = all_ + key
    random.shuffle(all)
    return convert.list_to_str(all)

