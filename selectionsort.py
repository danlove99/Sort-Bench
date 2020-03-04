def selectionsort(arr):
	for i in range(len(arr)):
		min_el = i
		for j in range(i+1, len(arr)):
			if arr[min_el] > arr[j]:
				min_el = j
		arr[i], arr[min_el] = arr[min_el], arr[i]

