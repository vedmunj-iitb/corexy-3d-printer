"""CoreXY kinematics: how a head move turns into motor moves.

    A = X + Y
    B = X - Y
"""


def to_motors(x, y):
    return x + y, x - y


def to_head(a, b):
    return (a + b) / 2, (a - b) / 2


if __name__ == '__main__':
    print('  dX    dY  ->    dA    dB')
    for dx, dy in [(100, 0), (0, 100), (100, 100), (-50, 25)]:
        da, db = to_motors(dx, dy)
        assert to_head(da, db) == (dx, dy)
        print(f'{dx:4} {dy:5}  -> {da:5} {db:5}')
