from datetime import datetime, timedelta

type_dict = {
    'str': type(''),
    'int': type(0),
    'dict': type({}),
    'list': type([])
}
re_type_dict = {
    type(''): 'str',
    type(0): 'int',
    type({}): 'dict',
    type([]): 'list'
}

def validate_type(*args, **kwargs):
    '''
    Validating Data Type

    Description: 
        Validate type of one / more variable with one / more data type class

    Usage:
        0. Sample data
            variable = 'test data'
            variable
            # test data

            variable2 = 4
            variable2
            # 4

        1.  Check only one variable with certain data type:
            data_type(variable, str)
            # None

        2.  Check only one variable with multiple possible data type:
            data_type(variable, str, int)
            # None

        3.  Check two / more variables with one / multiple possible data type:
            data_type([
                (variable, str, int),
                (variable2, int)    
            ])
            # None

        4.  When the data has different accepted type(s):
            data_type(variable, int, list)
            # "Data has invalid accepted type! (Index: 0, Input: str, Accepted: int, list)"

    '''
    checks = []
    if len(args) == 0:
        pass
    elif len(args) == 1:
        checks = args[0]
    elif len(args) >= 2:
        check = []
        for arg in args:
            if arg != args[0]:
                if type(arg) != type(type('')):
                    raise ReferenceError("Doesn't accept another argument after a 'dict' argument!")
            check.append(arg)
        checks.append(tuple(check))
    for check in checks:
        index = checks.index(check)
        result = []
        check = list(check)
        type_input = type(check[0])
        check.pop(0)
        for validation in check:
            if type(validation) == type(''):
                result.append(type_input == type_dict[validation])
            else:
                result.append(type_input == validation)
        if True not in result:
            error_input_string = re_type_dict[type_input]
            error_args_string = ", ".join(repr(re_type_dict[v]) for v in check).replace("'","").replace('"','')
            if kwargs.get('name') == None:
                raise TypeError("Data has invalid accepted type! (Index: %s, Input: %s, Accepted: %s)"%(index, error_input_string, error_args_string))
            else:
                raise TypeError("'%s' data has invalid accepted type! (Index: %s, Input: %s, Accepted: %s)"%(kwargs.get('name'), index, error_input_string, error_args_string))

def utcnow():
    return datetime.utcnow()

def now(**kwargs):
    if len(kwargs) == 0:
        return datetime.now()
    elif len(kwargs) == 1:
        return utcnow() + timedelta(kwargs)
    else:
        pass
    