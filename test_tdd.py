import unittest
from orders import check_order_status

class TestOrder(unittest.TestCase):

    def test_check_order_status(self):
        order_id = 100
        self.assertEqual(check_order_status(order_id), True)
        self.assertFalse(False)
        