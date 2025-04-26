import unittest

# Функция проверки корректного расчета скидки
def discount_calcutale(amount):
    if amount > 300000:
        return 15
    elif amount > 50000:
        return 10
    elif amount > 10000:
        return 5
    else:
        return 0 
    
class TestDiscountCalculate(unittest.TestCase):
    def test_cases_discount(self):
        self.assertEqual(discount_calcutale(0), 0)
        self.assertEqual(discount_calcutale(10000), 0)
        self.assertEqual(discount_calcutale(10001), 5)
        self.assertEqual(discount_calcutale(50000), 5)
        self.assertEqual(discount_calcutale(50001), 10)
        self.assertEqual(discount_calcutale(300000), 10)
        self.assertEqual(discount_calcutale(300001), 15)
    
    def test_case_zero(self):
        self.assertEqual(discount_calcutale(0), 0)
        self.assertEqual(discount_calcutale(10000), 0)
    
    def test_case_five(self):
        self.assertEqual(discount_calcutale(10001), 5)
        self.assertEqual(discount_calcutale(50000), 5)
    
    def test_case_ten(self):
        self.assertEqual(discount_calcutale(50001), 10)
        self.assertEqual(discount_calcutale(300000), 10)
    
    def test_case_pytn(self):
        self.assertEqual(discount_calcutale(300001), 15)
        self.assertEqual(discount_calcutale(509429), 15)




unittest.main(verbosity=2)