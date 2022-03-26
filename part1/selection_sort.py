import unittest



def selection_sort(data,desc=False):
    """
        Searches for the largest/smallest element and swaps it with the first/i-th element
    """
    for i in range(len(data)):
        target_index = i
        target_value = data[i]
        for j in range(i,len(data)):
            if desc:
                if data[j] > target_value:
                    target_value=data[j]
                    target_index = j
            else:
                if data[j] < target_value:
                    target_value=data[j]
                    target_index = j
        hold = data[i]
        data[i] = data[target_index]
        data[target_index]=hold
    return data





class TestSelectionSort(unittest.TestCase):
    def test_list_sort(self):
        data = [4,1,7,2,6,2,7,9,233,6,34,-0.23,44]
        data_sorted = [-0.23,1,2,2,4,6,6,7,7,9,34,44,233]
        result = selection_sort(data)
        self.assertEqual(result,data_sorted)
    
    def test_desc_sort(self):
        data = [4,1,7,2,6,2,7,9,233,6,34,-0.23,44]
        data_sorted = [-0.23,1,2,2,4,6,6,7,7,9,34,44,233]
        result = selection_sort(data,True)
        self.assertEqual(result,list(reversed(data_sorted)))



if __name__ == "__main__":
    unittest.main()