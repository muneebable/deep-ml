import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	# print(len(a[0]))
	# print(len(a[1]))
	# print(len(b))
	if len(a[0]) != len(b):
		return -1
	return np.matmul(a,b)