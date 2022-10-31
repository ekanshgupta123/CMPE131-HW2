def sort_dictionary(input): 
	sorted_dict = {k: values for k, values in sorted(input.items(), key = lambda item: item[1][1])}	
	list = []
	for i in sorted_dict:
		list.append(tuple((i, sorted_dict[i][0])))
	return list
