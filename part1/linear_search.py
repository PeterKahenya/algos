import unittest



def linear_search(data,key):
    """
        Searches for key in data and returns it's index or -1 if not found
    """
    for index,d in enumerate(data):
        if d == key:
            return index
    return -1


class TestLinearSearch(unittest.TestCase):

    def test_element_found(self):
        data = [1,2,3,4,55,1,23,5]
        key = 4
        found_index = linear_search(data,key)
        self.assertEqual(found_index,3)

    def test_element_not_found(self):
        data = [1,2,3,4,55,1,23,5]
        key = 9
        found_index = linear_search(data,key)
        self.assertEqual(found_index,-1)


if __name__ == "__main__":
    unittest.main()