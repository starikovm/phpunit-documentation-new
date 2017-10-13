import unittest
import subprocess
import os


class TestConversion(unittest.TestCase):
    def test_codeblock(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        print 'python ' + dir_path + '/../DocBookToReST.py'

        process = subprocess.Popen(
            [
                'python',
                dir_path + '/../DocBookToReST.py',
                dir_path + '/fixtures/code-example.xml'
            ],
            stdout=subprocess.PIPE
        )
        out, err = process.communicate()

        with open(dir_path + '/fixtures/expected-code-example.rst', 'r') as content_file:
            expected_content = content_file.read()

        self.assertEqual(out, expected_content)


if __name__ == '__main__':
    unittest.main()
