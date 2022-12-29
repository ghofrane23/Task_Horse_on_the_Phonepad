import unittest
import task


class Testfunc(unittest.TestCase):
    def test_count_p1(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 1)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p2(self):
        results = {1: 1, 2: 2, 3: 4, 4: 10, 5: 20, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 2)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p3(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 3)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p4(self):
        results = {1: 1, 2: 3, 3: 6, 4: 16, 5: 32, 6: 84}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 4)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p5(self):
        results = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 5)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p6(self):
        results = {1: 1, 2: 3, 3: 6, 4: 16, 5: 32, 6: 84}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 6)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p7(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 7)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p8(self):
        results = {1: 1, 2: 2, 3: 4, 4: 10, 5: 20, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 8)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_p9(self):
        results = {1: 1, 2: 2, 3: 5, 4: 10, 5: 26, 6: 52}
        for N in range(1, 7):
            distinct_numbers = task.count(N - 1, 9)

            self.assertEqual(distinct_numbers, results[N])


if __name__ == '__main__':
    unittest.main()
