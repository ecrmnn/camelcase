# coding=utf-8

import unittest
from camelcase import camelcase


class CamelCaseTest(unittest.TestCase):

    def test_string_with_dashes(self):
        self.assertEqual(camelcase('foo-bar'), 'fooBar')

    def test_string_with_underscores(self):
        self.assertEqual(camelcase('FoO_BAR'), 'fooBar')

    def test_string_with_dunder(self):
        self.assertEqual(camelcase('__FOO__bar__'), 'fooBar')

    def test_string_with_space(self):
        self.assertEqual(camelcase('foo bar'), 'fooBar')

    def test_string_with_spaces(self):
        self.assertEqual(camelcase('foo   bar'), 'fooBar')

    def test_string_with_unicode_characters(self):
        self.assertEqual(camelcase('blå_bær_sylte-tøy'), 'blåBærSylteTøy')

    def test_is_variadic_function(self):
        self.assertEqual(
            camelcase('blå', 'bær', 'sylte', 'tøy'),
            'blåBærSylteTøy'
        )

    def test_accepts_list(self):
        self.assertEqual(camelcase(['spam', 'eggs']), 'spamEggs')

if __name__ == '__main__':
    unittest.main()
