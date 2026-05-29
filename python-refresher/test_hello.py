import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "eric")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertNotEqual(hello.sin(0.5), 1)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertNotEqual(hello.sin(0.5), 1)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)

    def test_add(self):
        self.assertEqual(hello.add(10, 134), 144)
        self.assertEqual(hello.add(0, -1), -1)
        self.assertNotEqual(hello.add(-2, -7), 9)

    def test_sub(self):
        self.assertEqual(hello.sub(2398, 203219), -200821)
        self.assertEqual(hello.sub(5, -2), 7)
        self.assertNotEqual(hello.sub(-1, -6), -7)

    def test_mul(self):
        self.assertEqual(hello.mul(100, 96), 9600)
        self.assertEqual(hello.mul(5, -3), -15)
        self.assertNotEqual(hello.mul(-7, -3), -21)


if __name__ == "__main__":
    unittest.main()
