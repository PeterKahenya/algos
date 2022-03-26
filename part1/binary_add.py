import unittest



def binary_add(first_num,second_num):
    """
        Adds two lists of binary numbers expressed as the integers 1 and 0 and returns a list that is their sum.
        Uses the full adder logic circuit.
    """

    addition = []
    s=0
    c=0
    for a,b in zip(reversed(first_num),reversed(second_num)):
        s = (bool(a)^bool(b))^bool(c)
        addition.insert(0,int(s)) # Insert element at the beginning and push the others
        c = int(a & b)
    if bool(c):
        addition.insert(0,int(c))
    return addition





class TestBinaryAdd(unittest.TestCase):

    def test_binary_add_with_carry(self):
        a = [1,1,1,1,1]
        b = [1,1,1,1,1]
        a_plus_b = [1,1,1,1,1,0]
        result = binary_add(a,b)
        self.assertEqual(result,a_plus_b)


    def test_binary_add_without_carry(self):
        a = [1,0,1]
        b = [0,0,1]
        a_plus_b = [1,1,0]
        result = binary_add(a,b)
        self.assertEqual(result,a_plus_b)
    
    def test_zeros(self):
        a = [0,0,0,0,0,0,0,0,0,0,0,0]
        b = [0,0,0,0,0,0,0,0,0,0,0,0]
        a_plus_b = [0,0,0,0,0,0,0,0,0,0,0,0]
        result = binary_add(a,b)
        self.assertEqual(result,a_plus_b)
    
    def test_ones(self):
        a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        a_plus_b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
        result = binary_add(a,b)
        self.assertEqual(result,a_plus_b)


if __name__ == "__main__":
    unittest.main()