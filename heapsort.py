import heapq

def heapsort(arr):
	h = []
	for x in arr: heapq.heappush(h, x)
	return [heapq.heappop(h) for i in range(len(h))]
