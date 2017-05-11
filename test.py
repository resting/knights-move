import numpy as np
import sys
import unittest as ut

import getnextmoves as gnm


class TestGetNextMoves(ut.TestCase):
    def test_should_return_right_legal_moves_3_4_grid(self):
        # 3x4 grid, starting (0,0) should return [1,2] and [2,1]
        bounds = [3 - 1, 4 - 1]
        v = np.array([0, 0])

        nextMoves = gnm.getNextMoves(v, bounds)

        m1 = np.array([1, 2])
        m2 = np.array([2, 1])

        self.assertTrue(np.equal(m1, nextMoves[1]).all())
        self.assertTrue(np.equal(m2, nextMoves[3]).all())

    def test_should_return_right_legal_moves_3_3_grid(self):
        # 3x3 grid, starting (0,2) should return [1,0] and [2,1]
        bounds = [3 - 1, 3 - 1]
        v = np.array([0, 2])

        nextMoves = gnm.getNextMoves(v, bounds)

        m1 = np.array([1, 0])
        m2 = np.array([2, 1])

        self.assertTrue(np.equal(m1, nextMoves[0]).all())
        self.assertTrue(np.equal(m2, nextMoves[3]).all())


if __name__ == '__main__':
    ut.main()
