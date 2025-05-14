import unittest

# Функция расчета скидки
def discount_calculate(amount):
    if amount > 300000:
        return 15
    elif amount > 50000:
        return 10
    elif amount > 10000:
        return 5
    else:
        return 0

class TestDiscount(unittest.TestCase):
    def test_discount_0(self):
        self.assertEqual(discount_calculate(0), 0)
        self.assertEqual(discount_calculate(10000), 0)

    def test_discount_5(self):
        self.assertEqual(discount_calculate(10001), 5)
        self.assertEqual(discount_calculate(50000), 5)

    def test_discount_10(self):
        self.assertEqual(discount_calculate(50001), 10)
        self.assertEqual(discount_calculate(300000), 10)

    def test_discount_15(self):
        self.assertEqual(discount_calculate(300001), 15)
        self.assertEqual(discount_calculate(82482342343244234232431), 15)

if __name__ == "__main__":
    unittest.main(verbosity=2)