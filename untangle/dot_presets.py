patterns = {
    6: [
        [[(1, 0), (1, 1), (0, 1)], []],
        [[(2, 0), (2, 1), (1, 1)], [(0, 0)]],
        [[(2, 1)], [(1, 0)]],
        [[(1, 1)], [(0, 0)]],
        [[(2, 1)], [(1, 0), (0, 0), (0, 1)]],
        [[], [(1, 1), (1, 0), (2, 0)]],
    ],
    7: [
        [[(0, 1), (1, 0)], []],
        [[(0, 1), (1, 1), (2, 1), (2, 0)], [(0, 0)]],
        [[(2, 1)], [(1, 0)]],
        [[(1, 1), (0, 2)], [(0, 0), (1, 0)]],
        [[(2, 1), (0, 2)], [(0, 1), (1, 0)]],
        [[], [(1, 1), (1, 0), (2, 0)]],
        [[], [(0, 1), (1, 1)]],
    ],
    8: [
        [[(0, 1), (1, 1), (1, 0)], []],
        [[(2, 0), (1, 1), (2, 1)], [(0, 0)]],
        [[(2, 1)], [(1, 0)]],
        [[(0, 2)], [(0, 0)]],
        [[(0, 2), (1, 2)], [(0, 0), (1, 0)]],
        [[(1, 2)], [(1, 0), (2, 0)]],
        [[(1, 2)], [(0, 1), (1, 1)]],
        [[], [(0, 2), (1, 1), (2, 1)]],
    ],
    9: [
        [[(1, 0), (0, 1)], []],  # 1
        [[(0, 1), (1, 1), (2, 1), (2, 0)], [(0, 0)]],  # 2
        [[(2, 1)], [(1, 0)]],  # 3
        [[(0, 2), (1, 1)], [(0, 0), (1, 0)]],  # 4
        [[(0, 2), (1, 1)], [(0, 0), (1, 0)]],  # 5
        [[(2, 2)], [(1, 1), (1, 0), (2, 0)]],  # 6
        [[(1, 2)], [(0, 1), (1, 1)]],  # 7
        [[(2, 2)], [(0, 1)]],  # 8
        [[(2, 2)], [(1, 2)]],  # 9
    ],
    10: [
        [[(1, 0), (1, 1), (0, 1)], []],  # 1
        [[(2, 0)], [(0, 0)]],  # 2
        [[(3, 0), (3, 1), (2, 1)], [(1, 1)]],  # 3
        [[(3, 1)], [(2, 0)]],  # 4
        [[(0, 2)], [(0, 0)]],  # 5
        [[(2, 1), (1, 2), (0, 2)], [(0, 0)]],  # 6
        [[(3, 1), (1, 2)], [(2, 0), (1, 1)]],  # 7
        [[], [(2, 0), (3, 0), (2, 1)]],  # 8
        [[(1, 2)], [(0, 1), (1, 1)]],  # 9
        [[], [(0, 2), (1, 1), (2, 1)]],  # 10
    ],
    11: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(1, 1), (2, 0), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 1), (3, 0), ], [(1, 0), ]],
        [[(3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), ], [(0, 0), ]],
        [[(1, 2), (0, 2), ], [(0, 0), (1, 0), (2, 0), (0, 1), ]],
        [[(2, 2), (3, 1), ], [(2, 0), ]],
        [[(2, 2), ], [(2, 0), (3, 0), (2, 1), ]],
        [[(1, 2), ], [(0, 1), (1, 1), ]],
        [[(2, 2), ], [(1, 1), (0, 2), ]],
        [[], [(2, 1), (3, 1), (1, 2), ]],
    ],
    12: [
        [[(1, 0), (0, 1), ], []],
        [[(2, 0), (1, 1), (2, 1), (0, 1), ], [(0, 0), ]],
        [[(2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), ], [(0, 0), (1, 0), ]],
        [[(0, 2), (1, 2), ], [(1, 0), (0, 1), ]],
        [[(2, 2), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(2, 2), (3, 2), ], [(3, 0), ]],
        [[(1, 2), ], [(0, 1), (1, 1), ]],
        [[(2, 2), ], [(1, 1), (0, 2), ]],
        [[(3, 2), ], [(2, 1), (3, 1), (1, 2), ]],
        [[], [(3, 1), (2, 2), ]],
    ],
    13: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(2, 0), (1, 1), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 1), ], [(0, 0), (1, 0), (2, 0), (0, 1), ]],
        [[(3, 1), (2, 2), ], [(2, 0), (3, 0), (1, 1), ]],
        [[(3, 2), ], [(3, 0), (2, 1), ]],
        [[(0, 3), (1, 2), ], [(0, 1), ]],
        [[(2, 2), (0, 3), ], [(0, 1), (1, 1), (0, 2), ]],
        [[(3, 2), (0, 3), ], [(1, 2), (2, 1), ]],
        [[], [(2, 2), (3, 1), ]],
        [[], [(0, 2), (1, 2), (2, 2), ]],
    ],
    14: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(1, 1), (2, 0), (2, 1), ], [(0, 0), ]],
        [[(3, 0), (2, 1), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(2, 2), (3, 1), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), ], [(0, 1), ]],
        [[(0, 3), (1, 3), ], [(0, 1), (1, 1), (0, 2), ]],
        [[(1, 3), (3, 2), ], [(1, 1), (2, 1), (3, 1), ]],
        [[], [(3, 1), (2, 2), ]],
        [[(1, 3), ], [(0, 2), (1, 2), ]],
        [[], [(1, 2), (2, 2), (0, 3), ]],
    ],
    15: [
        [[(1, 0), (1, 1), (0, 1)], []],  # 1
        [[(2, 0), (2, 1)], [(0, 0)]],  # 2
        [[(3, 0), (3, 1), (2, 1)], [(1, 0)]],  # 3
        [[(3, 1)], [(2, 0)]],  # 4
        [[(1, 1), (1, 2), (0, 2)], [(0, 0)]],  # 5
        [[(2, 1)], [(0, 0), (0, 1)]],  # 6
        [[(3, 1), (2, 2)], [(2, 0), (1, 0), (1, 1)]],  # 7
        [[(3, 2), (2, 2)], [(2, 1), (2, 0), (3, 0)]],  # 8
        [[(0, 3), (1, 3)], [(0, 1)]],  # 9
        [[(2, 2), (2, 3), (1, 3)], [(0, 1)]],  # 10
        [[(3, 2)], [(3, 1), (2, 2)]],  # 11
        [[(2, 3)], [(3, 1), (2, 2)]],  # 12
        [[(1, 3)], [(0, 2)]],  # 13
        [[(2, 3)], [(1, 2), (0, 2), (0, 3)]],  # 14
        [[], [(1, 3), (1, 2), (3, 2)]],  # 15
    ],
    16: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(1, 1), (2, 0), (2, 1), ], [(0, 0), ]],
        [[(3, 0), (2, 1), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 1), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(2, 2), ], [(1, 0), (2, 0), (3, 0), (1, 1), ]],
        [[(2, 2), (3, 2), ], [(3, 0), ]],
        [[(1, 2), (0, 3), ], [(0, 1), ]],
        [[(0, 3), (1, 3), ], [(0, 1), (1, 1), (0, 2), ]],
        [[(1, 3), (2, 3), (3, 3), ], [(2, 1), (3, 1), ]],
        [[(3, 3), ], [(3, 1), ]],
        [[(1, 3), ], [(0, 2), (1, 2), ]],
        [[(2, 3), ], [(1, 2), (2, 2), (0, 3), ]],
        [[(3, 3), ], [(2, 2), (1, 3), ]],
        [[], [(2, 2), (3, 2), (2, 3), ]],
    ],
    17: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(1, 1), (2, 0), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (1, 2), (0, 2), ], [(0, 0), ]],
        [[(2, 1), ], [(1, 0), (0, 0), (2, 0), (0, 1), ]],
        [[(3, 1), (1, 2), (2, 2), ], [(2, 0), (3, 0), (1, 1), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(0, 3), ], [(0, 1), ]],
        [[(0, 3), (2, 2), (1, 3), ], [(0, 1), (2, 1), ]],
        [[(3, 2), (3, 3), ], [(2, 1), (3, 1), (1, 2), ]],
        [[(3, 3), ], [(3, 1), (2, 2), ]],
        [[(0, 4), (1, 3), ], [(0, 2), (1, 2), ]],
        [[(0, 4), (2, 3), ], [(0, 3), (1, 2), ]],
        [[(3, 3), (0, 4), ], [(1, 3), ]],
        [[], [(3, 2), (2, 2), (2, 3), ]],
        [[], [(0, 3), (1, 3), (2, 3), ]],
    ],
    18: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(1, 1), (2, 1), (2, 0), ], [(0, 0), ]],
        [[(2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(2, 1), (1, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(3, 1), ], [(1, 0), (2, 0), (3, 0), (1, 1), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), ], [(0, 1), ]],
        [[(2, 3), (0, 3), ], [(0, 1), (1, 1), (0, 2), ]],
        [[(3, 2), ], [(3, 1), ]],
        [[(2, 3), (3, 3), ], [(3, 1), (2, 2), ]],
        [[(1, 3), (0, 4), ], [(0, 2), (1, 2), ]],
        [[(2, 3), (0, 4), (1, 4), ], [(0, 3), ]],
        [[(3, 3), (1, 4), ], [(1, 2), (3, 2), (1, 3), ]],
        [[], [(3, 2), (2, 3), ]],
        [[(1, 4), ], [(0, 3), (1, 3), ]],
        [[], [(1, 3), (2, 3), (0, 4), ]],
    ],
    19: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(2, 0), (1, 1), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), ], [(0, 0), (1, 0), (2, 0), (0, 1), ]],
        [[(1, 2), (2, 2), (3, 1), ], [(2, 0), (3, 0), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), ]],
        [[(1, 3), ], [(0, 1), (1, 1), (2, 1), (0, 2), ]],
        [[(1, 3), (2, 3), (3, 2), ], [(2, 1), (3, 1), ]],
        [[(2, 3), (3, 3), ], [(3, 1), (2, 2), ]],
        [[(1, 3), (0, 4), ], [(0, 2), ]],
        [[(0, 4), (1, 4), ], [(0, 2), (1, 2), (2, 2), (0, 3), ]],
        [[(1, 4), (2, 4), (3, 3), ], [(2, 2), (3, 2), ]],
        [[(2, 4), ], [(3, 2), (2, 3), ]],
        [[(1, 4), ], [(0, 3), (1, 3), ]],
        [[], [(0, 4), (2, 3), (1, 3), ]],
        [[], [(2, 3), (3, 3), ]],
    ],
    20: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(2, 0), (2, 1), (1, 1), ], [(0, 0), ]],
        [[(3, 0), (2, 1), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(3, 1), (2, 2), (3, 2), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(3, 2), ], [(2, 1), (3, 0), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), ]],
        [[(1, 3), (2, 2), ], [(0, 2), (0, 1), (1, 1), ]],
        [[(1, 3), (3, 2), (2, 3), ], [(1, 1), (2, 1), (1, 2), ]],
        [[(2, 3), (3, 3), ], [(2, 1), (3, 1), (2, 2), ]],
        [[(1, 3), (0, 4), ], [(0, 2), ]],
        [[(1, 4), ], [(0, 2), (1, 2), (2, 2), (0, 3), ]],
        [[(1, 4), (2, 4), ], [(2, 2), (3, 2), ]],
        [[(2, 4), (3, 4), ], [(3, 2), ]],
        [[(1, 4), ], [(0, 3), ]],
        [[], [(1, 3), (2, 3), (0, 4), ]],
        [[(3, 4), ], [(2, 3), (3, 3), ]],
        [[], [(3, 3), (2, 4), ]],
    ],
    21: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(1, 1), (2, 1), (2, 0), ], [(0, 0), ]],
        [[(2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(2, 2), (3, 1), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), ]],
        [[(1, 3), (2, 3), ], [(1, 1), (0, 2), (0, 1), ]],
        [[(2, 3), ], [(1, 1), (2, 1), (3, 1), ]],
        [[(2, 3), (3, 3), ], [(3, 1), ]],
        [[(1, 3), (0, 4), (1, 4), ], [(0, 2), ]],
        [[(2, 4), (2, 3), ], [(0, 2), (1, 2), (0, 3), ]],
        [[(3, 3), ], [(1, 2), (2, 2), (3, 2), (1, 3), ]],
        [[(3, 4), ], [(3, 2), (2, 3), ]],
        [[(1, 4), (0, 5), ], [(0, 3), ]],
        [[(2, 4), (0, 5), ], [(0, 3), (0, 4), ]],
        [[(3, 4), (0, 5), ], [(1, 3), (1, 4), ]],
        [[], [(3, 3), (2, 4), ]],
        [[], [(0, 4), (1, 4), (2, 4), ]],
    ],
    22: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(2, 0), (1, 1), (2, 1), ], [(0, 0), ]],
        [[(2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[(1, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(1, 2), (3, 1), (2, 2), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(3, 2), (2, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), ]],
        [[(1, 3), ], [(0, 1), (1, 1), (2, 1), (0, 2), ]],
        [[(1, 3), (2, 3), (3, 2), ], [(2, 1), (3, 1), ]],
        [[(2, 3), (3, 3), ], [(3, 1), (2, 2), ]],
        [[(1, 3), (0, 4), (1, 4), ], [(0, 2), ]],
        [[], [(0, 2), (1, 2), (2, 2), (0, 3), ]],
        [[(1, 4), (2, 4), (3, 3), ], [(2, 2), (3, 2), ]],
        [[(2, 4), (3, 4), ], [(3, 2), (2, 3), ]],
        [[(1, 4), (0, 5), ], [(0, 3), ]],
        [[(0, 5), (1, 5), ], [(0, 3), (2, 3), (0, 4), ]],
        [[(1, 5), ], [(2, 3), (3, 3), ]],
        [[(1, 5), ], [(3, 3), ]],
        [[(1, 5), ], [(0, 4), (1, 4), ]],
        [[], [(1, 4), (2, 4), (3, 4), (0, 5), ]],
    ],
    23: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(2, 0), (1, 1), (2, 1), ], [(0, 0), ]],
        [[(2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), ], [(0, 0), ]],
        [[(0, 2), (1, 2), ], [(0, 0), (1, 0), (0, 1), ]],
        [[(1, 2), (2, 2), ], [(1, 0), (2, 0), (3, 0), ]],
        [[(2, 2), (3, 2), ], [(3, 0), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), (1, 1), ]],
        [[(2, 2), (1, 3), ], [(1, 1), (2, 1), (0, 2), ]],
        [[(3, 2), (1, 3), (2, 3), ], [(2, 1), (3, 1), (1, 2), ]],
        [[(2, 3), (3, 3), ], [(3, 1), (2, 2), ]],
        [[(0, 4), ], [(0, 2), ]],
        [[(0, 4), (2, 3), ], [(0, 2), (1, 2), (2, 2), ]],
        [[(3, 3), (1, 4), ], [(2, 2), (3, 2), (1, 3), ]],
        [[(2, 4), (3, 4), ], [(3, 2), (2, 3), ]],
        [[(1, 4), (0, 5), ], [(0, 3), (1, 3), ]],
        [[(2, 4), (0, 5), (1, 5), ], [(0, 4), (2, 3), ]],
        [[(3, 4), (1, 5), (2, 5), ], [(1, 4), (3, 3), ]],
        [[(2, 5), ], [(3, 3), (2, 4), ]],
        [[(1, 5), ], [(0, 4), (1, 4), ]],
        [[(2, 5), ], [(0, 5), (1, 4), (2, 4), ]],
        [[], [(1, 5), (3, 4), (2, 4), ]],
    ],
    24: [
        [[(1, 0), (1, 1), (0, 1), ], []],
        [[(1, 1), (2, 0), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 1), (0, 2), (1, 2), ], [(0, 0), ]],
        [[], [(0, 0), (1, 0), (2, 0), (0, 1), ]],
        [[(2, 2), (1, 2), (3, 1), (3, 2), ], [(2, 0), (3, 0), ]],
        [[(3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), (1, 3), ], [(0, 1), ]],
        [[(2, 2), (1, 3), ], [(0, 1), (2, 1), (0, 2), ]],
        [[(3, 2), (1, 3), (3, 3), ], [(2, 1), (1, 2), ]],
        [[(3, 3), ], [(2, 1), (3, 1), (2, 2), ]],
        [[(1, 3), (0, 4), (1, 4), ], [(0, 2), ]],
        [[(2, 3), ], [(0, 2), (1, 2), (2, 2), (0, 3), ]],
        [[(1, 4), (2, 4), (3, 3), (3, 4), ], [(1, 3), ]],
        [[(3, 4), ], [(2, 2), (3, 2), (2, 3), ]],
        [[(0, 5), (1, 4), ], [(0, 3), ]],
        [[(2, 4), (0, 5), ], [(0, 3), (2, 3), (0, 4), ]],
        [[(3, 4), (2, 5), (3, 5), ], [(2, 3), (1, 4), ]],
        [[(3, 5), ], [(2, 3), (2, 4), (3, 3), ]],
        [[(1, 5), ], [(0, 4), (1, 4), ]],
        [[(2, 5), ], [(0, 5), ]],
        [[(3, 5), ], [(1, 5), (2, 4), ]],
        [[], [(2, 5), (3, 4), (2, 4), ]],
    ],
    25: [
        [[(1, 0), (0, 1), (1, 1), ], []],
        [[(2, 0), (1, 1), ], [(0, 0), ]],
        [[(1, 1), (2, 1), (3, 0), ], [(1, 0), ]],
        [[(2, 1), (3, 1), ], [(2, 0), ]],
        [[(1, 2), (0, 2), ], [(0, 0), ]],
        [[(1, 2), (2, 1), ], [(0, 0), (1, 0), (2, 0), ]],
        [[(3, 1), (2, 2), ], [(2, 0), (3, 0), (1, 1), ]],
        [[(2, 2), (3, 2), ], [(3, 0), (2, 1), ]],
        [[(1, 2), (0, 3), ], [(0, 1), ]],
        [[(2, 2), ], [(0, 1), (1, 1), (0, 2), ]],
        [[(2, 3), ], [(2, 1), (3, 1), (1, 2), ]],
        [[(2, 3), (3, 3), ], [(3, 1), ]],
        [[(1, 3), (0, 4), (1, 4), ], [(0, 2), ]],
        [[(2, 3), (1, 4), (2, 4), ], [(0, 3), ]],
        [[(2, 4), (3, 3), ], [(2, 2), (3, 2), (1, 3), ]],
        [[(2, 4), (3, 4), ], [(3, 2), (2, 3), ]],
        [[(1, 4), (0, 5), ], [(0, 3), ]],
        [[(0, 5), (1, 5), ], [(0, 3), (1, 3), (0, 4), ]],
        [[(1, 5), (2, 5), ], [(1, 3), (2, 3), (3, 3), ]],
        [[(3, 5), ], [(3, 3), ]],
        [[(0, 6), (1, 5), ], [(0, 4), (1, 4), ]],
        [[(0, 6), ], [(1, 4), (2, 4), (0, 5), ]],
        [[(3, 5), (0, 6), ], [(2, 4), ]],
        [[], [(3, 4), (2, 5), ]],
        [[], [(0, 5), (1, 5), (2, 5), ]],
    ],
}

base_dots = [
    [[(1, 0), ], []],
    [[(2, 0), ], [(0, 0), ]],
    [[(3, 0), ], [(1, 0), ]],
    [[(4, 0), ], [(2, 0), ]],
    [[(5, 0), (6, 0), ], [(3, 0), ]],
    [[(6, 0), ], [(4, 0), ]],
    [[(7, 0), ], [(5, 0), (4, 0), ]],
    [[(8, 0), ], [(6, 0), ]],
    [[(9, 0), ], [(7, 0), ]],
    [[], [(8, 0), ]],
]
