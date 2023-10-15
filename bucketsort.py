def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up
	return b


def bucketSort(x):
	arr = []
	slot_num = 10 # 10 baldes, o tamanho de cada balde é 0.1
	for i in range(slot_num):
		arr.append([])

	# Colocando os elementos nos buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
		
	# Sort individual buckets 
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	# concatenando o resultado
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

# array
x = [0.3242, 0.9875, 0.2343, 0.534, 0.765, 0.7655, 0.1213, 0.43543, 0.9423, 0.9999]
print("O array ordenado é")
print(bucketSort(x))