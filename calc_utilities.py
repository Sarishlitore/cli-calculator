import operator

SUPPORTED_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
    }

def clean_string(raw_string):
    result = ' '.join(raw_string.split()).lower()
    return result

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_expression(data):
    if len(data) != 3:
        return False
    if not is_number(data[0]) or not is_number(data[2]):
        return False 
    if data[1] not in SUPPORTED_OPERATIONS:
        return False
    return True

def evaluate(data):
    a, operation, b = float(data[0]), data[1], float(data[2])
    if operation == '/' and b == 0:
        return 'Error: Division by zero is not allowed'
    return SUPPORTED_OPERATIONS[operation](a, b)