from queue import LifoQueue

def calculator(input_string):
	input_string  = input_string.replace(" ", "")
	return input_string
	counter = -1
	result = 0
	for ch in range(len(input_string)):
    		if counter == ch:
        		continue
    		if input_string[ch] in ['-', '+', '/', '*', '**']:
        		next_value = int(input_string[ch+1])
        		if input_string[ch] == '-':
            			result -= next_value
            			counter = ch+1
        		elif input_string[ch] == '+':
            			result += next_value
            			counter = ch+1
        		elif input_string[ch] == '*':
            			result *= next_value
            			counter = ch+1
        		elif input_string[ch] == '/':
            			result /= next_value
            			counter = ch+1
        		elif input_string[ch] == '**':
            			result **= next_value
            			counter = ch+1
    		else:
        		result = int(input_string[ch])

def main():
	print(calculator(('1+12')))
main()
