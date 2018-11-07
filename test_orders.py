import unittest
from order_verify import check_order_status


class TestOrder(unittest.TestCase):
    
    def test_order_status(self):
        self.assertEqual(check_order_status(2), True)

    def test_check_order_status(self):
        order_id = 100
        order_id_1 = -6
        self.assertEqual(check_order_status(order_id), True)
        # use assertFalse to test for an order still pending
        self.assertFalse(check_order_status(order_id_1), False)
        
        

    # test if the input is an integer
    

    # test for an order id that does not exist in both lists

    # test if there are orders added to the list

    # test for adding of a new order

    # test for marking an order delivered