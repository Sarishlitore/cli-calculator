import calc_utilities

def calculator():
    print(f'Hello, its CLI calculator. Supported operations: {', '.join(calc_utilities.SUPPORTED_OPERATIONS)}.')
    print('Type "exit" or "e" to quit.')

    while True:
        try:
            input_string = calc_utilities.clean_string(input('Input expression. Example: 5 + 6\n'))
            
            if input_string in ['exit', 'e']:
                exit()

            data = input_string.split()

            if not calc_utilities.is_valid_expression(data):
                print('Something went wrong. Please follow the format: number operator number')
                continue
            
            result = calc_utilities.evaluate(data)
            print('Expression result:', result)
        except Exception as e:
            print('Something went wrong:', e)

if __name__ == '__main__':
    calculator()

