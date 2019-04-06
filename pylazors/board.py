from pylazors.blocks import *
from pylazors.utils import deepcopy


class Board:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self._blocks = [[None for _ in range(width)] for _ in range(height)]
        self._lasers = []
        self._points = []
        self._available_blocks = []
        self._laser_segments = []

    def mod_block(self, x, y, btype):
        # assert isinstance(x, int) and 0 <= x < self.width
        # assert isinstance(y, int) and 0 <= y < self.height
        # assert isinstance(btype, Block)
        self._blocks[y][x] = btype

    def load_blocks(self, blocks):
        self._blocks = deepcopy(blocks)

    def get_movable_blocks_num(self):
        return len([b for bs in self._blocks for b in bs if not b.is_fixed()])

    def get_block(self, x, y):
        # assert isinstance(x, int) and 0 <= x < self.width
        # assert isinstance(y, int) and 0 <= y < self.height
        return self._blocks[y][x]

    def get_blocks(self):
        return deepcopy(self._blocks)

    def add_point(self, x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        self._points.append((x, y))

    def get_points(self):
        return deepcopy(self._points)

    def add_laser(self, x, y, vx, vy):
        assert isinstance(x, int) and 0 <= x <= (2 * self.width)
        assert isinstance(y, int) and 0 <= y <= (2 * self.height)
        assert isinstance(vx, int)
        assert isinstance(vy, int)
        assert abs(vx) == abs(vy)
        vx, vy = abs(vx) // vx, abs(vy) // vy
        self._lasers.append((x, y, vx, vy))

    def add_laser_segments(self, x0, y0, x1, y1):
        # assert isinstance(x0, int) and 0 <= x0 <= (2 * self.width)
        # assert isinstance(y0, int) and 0 <= y0 <= (2 * self.height)
        # assert isinstance(x1, int)
        # assert isinstance(y1, int)
        self._laser_segments.append((x0, y0, x1, y1))

    def load_laser_segments(self, laser_segments):
        self._laser_segments = deepcopy(laser_segments)

    def clear_laser_segments(self):
        self._laser_segments = []

    def get_laser_segments(self):
        return deepcopy(self._laser_segments)

    def get_lasers(self):
        return deepcopy(self._lasers)

    def add_available_blocks(self, block, count):
        assert not block.is_fixed()
        self._available_blocks += [block] * count

    def get_available_blocks(self):
        return deepcopy(self._available_blocks)

    def clean_board(self):
        """ Set all non-fixed block to BLANK. """

        for x in range(self.width):
            for y in range(self.height):
                if not self.get_block(x, y).is_fixed():
                    self.mod_block(x, y, Block.BLANK)

    def copy(self, with_blocks=True, with_lasers=True, with_points=True,
             with_available_blocks=True, with_laser_segs=True):
        new_board = Board(self.name, self.width, self.height)
        if with_blocks:
            new_board._blocks = deepcopy(self._blocks)
        if with_lasers:
            new_board._lasers = deepcopy(self._lasers)
        if with_points:
            new_board._points = deepcopy(self._points)
        if with_available_blocks:
            new_board._available_blocks = deepcopy(self._available_blocks)
        if with_laser_segs:
            new_board._laser_segments = deepcopy(self._laser_segments)
        return new_board

    def __str__(self):
        return '<Board: %s (%dx%d)>' % (self.name, self.width, self.height)
