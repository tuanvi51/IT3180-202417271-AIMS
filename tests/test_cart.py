import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa DVD -> đều phải thành công (True)
        for i in range(20):
            res = cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0))
            self.assertTrue(res)

        # Thêm đĩa thứ 21 -> phải bị từ chối (False)
        res_21 = cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0))
        self.assertFalse(res_21)


class TestCartDiscount(unittest.TestCase):
    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        # 100 giảm 20% = 80
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_invalid_discount_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
