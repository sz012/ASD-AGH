#O(n)
def insertion_sort(T):
    if len(T) > 1:
        for i in range(len(T)):
            j = i
            while j > 0 and T[j-1] > T[j]:
                T[j-1], T[j] = T[j], T[j-1]
                j -= 1

def bucket_sort(T):
    buckets = [[] for k in range(len(T))]
    for element in T:
        buckets[int(len(T) * element)].append(element)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for number in bucket:
            T[index] = number
            index += 1

arr = [0.5, 0.1, 0.6, 0.65, 0.9]
bucket_sort(arr)
print(arr)
