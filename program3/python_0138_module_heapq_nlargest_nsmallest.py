import heapq

tup1 = (10, 30, 50, 20, 60, 40, 100, -1000, 95, 46, 87)

def solution3():

    largest_2 = heapq.nlargest(2, tup1)
    smallest_2 = heapq.nsmallest(2, tup1)

    # print(f"heapq.nlargest(2, tup1) returns: {largest_2}")
    # print(f"heapq.nsmallest(2, tup1) returns: {smallest_2}")

    result = tuple(smallest_2 + largest_2[::-1])
    print(result)


solution3()



'''
heapq means: heap + queue
heap: 
queue: 
'''