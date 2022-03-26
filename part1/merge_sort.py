import unittest
import math


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    for i in range(0,n):
       yield fib(i)


def merge(a,i,j,k):
    left_subset = a[i:j]
    right_subset = a[j:k]
    left_subset.append(math.inf)
    right_subset.append(math.inf)
    x=0
    w=0
    for i in range(i,k):
        if left_subset[x]<=right_subset[w]:
            a[i]=left_subset[x]
            x = x+1
        else:
            a[i]=right_subset[w]
            w = w+1

def merge_sort(data,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        merge_sort(data,p,q)
        merge_sort(data,q+1,r)
        merge(data,p,q+1,r+1)

    return data




class TestMergeSort(unittest.TestCase):
    def test_fibo(self):
        result = fibonacci(10)
        fibos = list(result)
        self.assertEqual(fibos,[0,1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_list_sort(self):
        data = [56,55,2,7,23,6]
        data_sorted = [2,6,7,23,55,56]
        result = merge_sort(data,0,len(data)-1)
        self.assertEqual(result,data_sorted)
    
    def test_empty_sort(self):
        data = []
        data_sorted = []
        result = merge_sort(data,0,len(data)-1)
        self.assertEqual(result,data_sorted)

if __name__ == "__main__":
    unittest.main()