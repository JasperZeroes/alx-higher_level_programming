a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
for k,v in a_dictionary.items():
    max = 0
    if v > max:
        max = v
for k, v in a_dictionary.items():
    if v == max:
        print(k)
        print(max) 


'''
def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

    OR

def square_matrix_simple(matrix = []):
    new_matrix = []
    for row in matrix:
        inner = []
        for num in row:
            inner.append( num ** 2)
        new_matrix.append(inner)
    return new_matrix
'''
