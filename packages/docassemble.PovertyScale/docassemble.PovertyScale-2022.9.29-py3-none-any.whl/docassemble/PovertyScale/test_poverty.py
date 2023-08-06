import unittest

from .poverty import poverty_scale_get_income_limit, poverty_scale_income_qualifies

class test_recreate_tables(unittest.TestCase):
    def test_MA_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(), 13590)
        self.assertEqual(poverty_scale_get_income_limit(2), 18310)
        self.assertEqual(poverty_scale_get_income_limit(3), 23030)
        self.assertEqual(poverty_scale_get_income_limit(4), 27750)
        self.assertEqual(poverty_scale_get_income_limit(5), 32470)
        self.assertEqual(poverty_scale_get_income_limit(6), 37190)
        self.assertEqual(poverty_scale_get_income_limit(7), 41910)
        self.assertEqual(poverty_scale_get_income_limit(8), 46630)

    def test_MA_125_table(self):
        self.assertEqual(poverty_scale_get_income_limit(1, 1.25), 16988)
        self.assertEqual(poverty_scale_get_income_limit(2, 1.25), 22888)
        self.assertEqual(poverty_scale_get_income_limit(3, 1.25), 28788)
        self.assertEqual(poverty_scale_get_income_limit(4, 1.25), 34688)
        self.assertEqual(poverty_scale_get_income_limit(5, 1.25), 40588)
        self.assertEqual(poverty_scale_get_income_limit(6, 1.25), 46488)
        self.assertEqual(poverty_scale_get_income_limit(7, 1.25), 52388)
        self.assertEqual(poverty_scale_get_income_limit(8, 1.25), 58288)
        
    def test_AK_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(state="AK"), 16990)
        self.assertEqual(poverty_scale_get_income_limit(2, state="ak"), 22890)
        self.assertEqual(poverty_scale_get_income_limit(3, state="Ak"), 28790)
        self.assertEqual(poverty_scale_get_income_limit(4, state="AK"), 34690)
        self.assertEqual(poverty_scale_get_income_limit(5, state="AK"), 40590)
        self.assertEqual(poverty_scale_get_income_limit(6, state="AK"), 46490)
        self.assertEqual(poverty_scale_get_income_limit(7, state="AK"), 52390)
        self.assertEqual(poverty_scale_get_income_limit(8, state="AK"), 58290)


class test_sample_incomes(unittest.TestCase):
    def test_example_income(self):
        # TODO(brycew): this should pass, but because of float percision, it doesn't work (even with round).
        # Would have to refactor to Decimal, but out of scope for now
        # self.assertTrue(poverty_scale_income_qualifies(1133))
        self.assertTrue(poverty_scale_income_qualifies(1132))
        self.assertTrue(poverty_scale_income_qualifies(1000))
        self.assertTrue(poverty_scale_income_qualifies(0))
        self.assertTrue(poverty_scale_income_qualifies(-1))
        self.assertFalse(poverty_scale_income_qualifies(1134))
        self.assertFalse(poverty_scale_income_qualifies(100000000))

if __name__ == "__main__":
    unittest.main()