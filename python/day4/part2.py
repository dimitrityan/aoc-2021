#!/usr/bin/env python3

from typing import List, Dict

class BingoCard:
    def __init__(self, card: List[List[str]], pos_map: Dict):
        self.matrix = card
        self.row_sum = [0 for i in range(5)]
        self.col_sum = [0 for i in range(5)]
        self.pos_map = pos_map
        self.nums_set = set()
        self.won = False
        for row in self.matrix:
            for col in row:
                self.nums_set.add(col)

class Solve:
    def __init__(self, bingo_cards: List[BingoCard], draw_order: List[int]):
        self.bingo_cards = bingo_cards
        self.draw_order =  draw_order
        self.solve()

    def solve(self):
        for num in self.draw_order:
            self.add_num_and_check_winner(num)
                

    def add_num_and_check_winner(self, num):
        for card in self.bingo_cards:
            if not card.won:
                if num in card.pos_map:
                    row, col = card.pos_map[num]
                    card.row_sum[row] += 1
                    card.col_sum[col] += 1
                    card.nums_set.remove(num)
                    if card.row_sum[row] == 5 or card.col_sum[col] == 5:
                        # Won
                        res = 0
                        for left_nums in card.nums_set:
                            res += left_nums
                        res *= num
                        print(f"Winner card num: {res}")
                        card.won = True

def generate_empty_card():
    return [[0 for i in range(5)] for i in range(5)]

with open("input.txt", "r") as input:
    lines = input.read().splitlines()
    draw_order = list(map(int, lines[0].split(",")))
    cur_card_rows = generate_empty_card()
    i = 0
    cards = []
    val_to_pos_map = {}
    for idx in range(2, len(lines[2:])+2):
        row = lines[idx]
        if len(row) == 0:
            # Init new bingo card
            bingocard = BingoCard(card=cur_card_rows, pos_map=val_to_pos_map)
            cur_card_rows = generate_empty_card()
            i = 0
            val_to_pos_map = {}
            cards.append(bingocard)
            continue
        row = row.split(" ")
        row = list(filter(lambda x: x != "", row))
        row = list(map(int, row))
        cur_card_rows[i] = row
        for r in range(0, len(row)):
            val_to_pos_map[row[r]] = (i, r)
        i += 1

    solve = Solve(bingo_cards=cards, draw_order=draw_order)
