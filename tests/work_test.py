from unittest import TestCase, main
from body.model import max_min_goods_on_the_list, create_good_from_list, delete_goods_from_list
import logging

logger = logging.getLogger('app.unittest')

class MaxMinTest(TestCase):
    logger.debug('Test is create')

    def setUp(self):
        self.good_01 = create_good_from_list(['Audi_test', 10000, 1])
        self.good_02 = create_good_from_list(['lighter_test', 1, 200])

    def test_max_price(self):
        self.assertEqual(max_min_goods_on_the_list()['max_value'], 10000)

    def test_min_price(self):
        self.assertEqual(max_min_goods_on_the_list()['min_value'], 1)

    def tearDown(self):
        delete_goods_from_list('Audi_test')
        delete_goods_from_list('lighter_test')

if __name__ == '__main__':
    main()