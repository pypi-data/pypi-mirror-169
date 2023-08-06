import unittest
import sys
import io
from VisageScript import *


"""
The code for the following test cases is inspired by the following source.
https://stackoverflow.com/questions/35779023/get-text-contents-of-what-has-been-printed-python
"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example1.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "5\n", "Incorrect output of parsing 'example1.vsgsc'.")

    def test_example2(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example2.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "5\n6\n", "Incorrect output of parsing 'example2.vsgsc'.")

    def test_example3(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example3.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "11\n1\n30\n1.2\n18\n", "Incorrect output of parsing 'example3.vsgsc'.")

    def test_example4(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example4.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "30\n11\n", "Incorrect output of parsing 'example4.vsgsc'.")

    def test_example5(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example5.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "5.23\n6.44\n33.6812\n1.21\n11.67\n149.544528\n", "Incorrect output of parsing 'example5.vsgsc'.")

    def test_example6(self):
        # Initialising the terminal
        terminal: Terminal = Terminal()

        # Initialising the stdout stream to be used to get printed text
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        # Printing the output of parsing the '.vsgsc' file
        parse_file("example6.vsgsc", terminal)

        # Getting the printed text
        sys.stdout = old_stdout
        contents = buffer.getvalue()

        # Closing the buffer since we have got the printed text
        buffer.close()
        self.assertEqual(contents, "210.666\n37.1332\n47.1332\n631.998\n", "Incorrect output of parsing 'example6.vsgsc'.")


if __name__ == '__main__':
    unittest.main()
