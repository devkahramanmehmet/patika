list_of_lists = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []
def flatten_list(list_of_lists):
    for item in list_of_lists:
        if type(item) is list:
            flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list
flatten_list(list_of_lists)
print(flat_list)

for i in reversed(list_of_lists):
    print(i)