def data_type(arg):
    if arg == None:
        return 'no value'
    elif type(arg) == str:
        return len(arg)
    elif type(arg) == bool:
        if arg == True:
            return True
        return 'the boolean'
    elif type(arg) == list:
        if len(arg) >= 3:
            return arg[2]
        else:
            return None
    else:
        if type(arg) == int:
            if arg < 100:
                return 'less than 100'
            elif arg == 100:
                return 'equal to 100'
            else:
                return 'more than 100'

print(data_type(569))
