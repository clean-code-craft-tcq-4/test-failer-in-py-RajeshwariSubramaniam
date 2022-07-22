import io
import sys
from unittest import TestCase

import src.misaligned as misaligned


class TestMisaligned(TestCase):

    def test_print_color_map(self):
        result = misaligned.print_color_map()
        assert (result == 25)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        misaligned.print_color_map()
        console_output = capturedOutput.getvalue()
        self.assertTrue(console_output.index('25 | Violet | Slate'))
        self.assertTrue(console_output.index('2  | White  | Orange'))
