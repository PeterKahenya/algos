import unittest



def insertion_sort(data,dsc=False):
    """
        Sorts a list in desc or asc order(asc is default)
        Sample data = [56,55,2,7,23,6]
    """
    try:
        for j in range(1,len(data)):
            key = data[j]
            i=j-1
            while i>-1 and (data[i] > key) != dsc:
                data[i+1] = data[i]
                i=i-1
            data[i+1]=key
    except TypeError as e:
        raise TypeError("Cannot sort object of multiple types")
    return data






#Tests
class TestInsertionSort(unittest.TestCase):
    def test_list_sort(self):
        data = [56,55,2,7,23,6]
        data_sorted = [2,6,7,23,55,56]
        result = insertion_sort(data)
        self.assertEqual(result,data_sorted)

    def test_multitype_list_sort(self):
        data = [56,"55",2,0.07,-23,6]
        with self.assertRaises(TypeError) as context:
            insertion_sort(data)
        self.assertTrue('Cannot sort object of multiple types' == str(context.exception))

    def test_desc_list_sort(self):
        data = [56,55,2,0.07,-23,6]
        data_sorted = [56,55,6,2,0.07,-23]
        result = insertion_sort(data,True)
        self.assertEqual(result,data_sorted)


if __name__ == '__main__':
    unittest.main()
