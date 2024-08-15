

def print_rec(n):
	if n == 1:
		print(1)
	else:
		print_rec(n - 1)
		print(n)


def print_rec_rev(n):
	if n == 1:
		print(n)
		return
	print(n)
	print_rec_rev(n - 1)


if __name__ == "__main__":
	# print_rec(7)
	print_rec_rev(9)
