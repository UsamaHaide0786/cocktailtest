import unittest
from main import get_cocktail


class GetCocktailTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = get_cocktail('Gin,Triple Sec,Lillet Blanc,Lemon Juice,Absinthe')
        self.assertEqual(len(result), 2)
        self.assertEqual(list(result[0].keys())[0], 'Corpse Reviver')
        self.assertEqual(list(result[1].keys())[0], 'White Lady')
