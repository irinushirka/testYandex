from random import randint, sample
result = 'practIce makeS perfect'

rand_symb = ''
for i in range(32, 64):
	rand_symb += chr(i) * 31
rand_symb = ''.join(sample(rand_symb, len(rand_symb)))

kr_5 = ''
for i in range(65, 123):
	if i % 5 == 0:
		kr_5 += chr(i) * 32
kr_5 = ''.join(sample(kr_5, len(kr_5)))

more_33 = ''
for i in range(32, 123):
	if chr(i) not in rand_symb and chr(i) not in kr_5:
		if chr(i) not in result:
			more_33 += chr(i) * randint(33, 133)
more_33 = ''.join(sample(more_33, len(more_33)))

common = more_33 + rand_symb + kr_5
common = ''.join(sample(common, len(common)))

random_positions = [randint(0, len(common + result) - 1) for i in range(len(result))]
random_positions.sort()

common = list(common)
counter = 0
for i in result:
    common.insert(random_positions[counter], i)
    counter += 1
common = ''.join(common)
# Resulted common:
print(common)

# Decoding
for i in common:
	if not i.isalpha():
		common = common.replace(i, '')
	if ord(i) % 5 == 0:
		common = common.replace(i, '')
	if common.count(i) >= 33:
		common = common.replace(i, '')
print(common)
