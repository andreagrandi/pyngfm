from twisted.trial.unittest import TestCase

from pyngfm.util import convert_boolean, get_boolean_as_int


class UtilitiesTestCase(TestCase):

    def test_convert_boolean_true(self):
        for value in [1, 20, "1", "1017", "Yes", True, "TRUE", "true", "t",
                     "on", "On"]:
            self.assertTrue(convert_boolean(value))

    def test_convert_boolean_false(self):
        for value in [0, "0", "No", False, "FALSE", "false", "f",
                     "off", "Off", "any old string"]:
            self.assertFalse(convert_boolean(value))

    def test_get_boolean_as_int(self):
        self.assertEquals(get_boolean_as_int(True), 1)
        self.assertEquals(get_boolean_as_int(False), 0)
