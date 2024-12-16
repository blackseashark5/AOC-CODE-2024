from dataclasses import dataclass
from typing import Set
def iter(size: complex):
    pos = complex(0,0)
    while pos.imag < size.imag:
        while pos.real < size.real:
            yield pos
            pos += 1
        pos += complex(-size.real, 1)
def gps(pos: complex) -> int:
    return 100*int(pos.imag) + int(pos.real)
@dataclass
class Warehouse:
    directions = { '>' : 1, '<' : -1, 'v': 1j, '^': -1j }
    walls : Set[complex]
    boxes : Set[complex]
    bot   : complex
    size  : complex
    moves : str
    def botmove(self, m: str):
        if m[0] not in Warehouse.directions:
            return
        dir = Warehouse.directions[m[0]]
        objs = []
        pos = self.bot
        while True:
            pos += dir
            if pos in self.walls:
                return
            if pos in self.boxes:
                objs.append(pos)
                continue
            self.bot += dir
            for obj in objs:
                self.boxes.remove(obj)
            for obj in objs:
                self.boxes.add(obj+dir)
            return
    def botmoves(self):
        moves = self.moves
        while moves:
            self.botmove(moves)
            moves = moves[1:]
    @classmethod
    def from_file(cls, path: str) -> 'Warehouse':
        with open(path, mode='r') as wf:
            wh = Warehouse(walls=set(), boxes=set(), bot=0j, size=0j, moves='')
            for row, line in enumerate(wf):
                if not line:
                    continue
                if line[0] in '<>^v':
                    wh.moves = wh.moves + line.strip()
                else:
                    wh.size = complex(max(wh.size.real,len(line)-1),row)
                    for col,sym in enumerate(line.strip()):
                        if sym == 'O':
                            wh.boxes.add(complex(col, row))
                        if sym == '@':
                            wh.bot = complex(col, row)
                        if sym == '#':
                            wh.walls.add(complex(col, row))
            return wh
wh = Warehouse.from_file('input.txt')
wh.botmoves()
print(f'day 15, part 1: {sum([gps(pos) for pos in wh.boxes])}')
@dataclass
class Widehouse:
    directions = { '>' : 1, '<' : -1, 'v': 1j, '^': -1j }
    walls : Set[complex]
    lboxes : Set[complex]
    rboxes: Set[complex]
    bot   : complex
    size  : complex
    moves : str
    def botmove(self, m: str):
        if m[0] not in Widehouse.directions:
            return
        dir = Widehouse.directions[m[0]]
        boxes = set()
        front = { self.bot }
        while front:
            nfront = set()
            for pos in front:
                pos += dir
                if pos in self.walls:
                    return
                if pos in self.lboxes:
                    assert dir != -1
                    assert pos + 1 in self.rboxes
                    boxes.add(pos)
                    nfront.add(pos + 1)      # right
                    if dir.imag:
                        nfront.add(pos)      # left
                if pos in self.rboxes:
                    assert dir != 1
                    assert pos-1 in self.lboxes
                    boxes.add(pos-1)
                    nfront.add(pos - 1)      # left
                    if dir.imag:
                        nfront.add(pos)      # right
            front = nfront
        self.bot += dir
        for pos in boxes:
            self.lboxes.remove(pos)
            self.rboxes.remove(pos+1)
        for pos in boxes:
            self.lboxes.add(pos+dir)
            self.rboxes.add(pos +1+ dir)
        return
    def botmoves(self):
        moves = self.moves
        while moves:
            self.botmove(moves)
            moves = moves[1:]
    @classmethod
    def from_file(cls, path: str) -> 'Widehouse':
        with open(path, mode='r') as wf:
            wh = Widehouse(walls=set(), lboxes=set(), rboxes=set(), bot=0j, size=0j, moves='')
            for row, line in enumerate(wf):
                if not line:
                    continue
                if line[0] in '<>^v':
                    wh.moves = wh.moves + line.strip()
                else:
                    wh.size = complex(max(wh.size.real,2*(len(line)-1)),row)
                    for col,sym in enumerate(line.strip()):
                        if sym == 'O':
                            wh.lboxes.add(complex(2*col, row))
                            wh.rboxes.add(complex(2 * col+1, row))
                        if sym == '@':
                            wh.bot = complex(2*col, row)
                        if sym == '#':
                            wh.walls.add(complex(2*col, row))
                            wh.walls.add(complex(2*col+1, row))
            return wh
wh = Widehouse.from_file('input.txt')
wh.botmoves()
print(f'day 15, part 2l: {sum([gps(pos) for pos in wh.lboxes])}')