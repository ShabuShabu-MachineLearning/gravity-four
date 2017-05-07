from itertools import combinations
import numpy as np


def judgea(goban, playerID):

    print("start1")

    if judge_single_player(goban, playerID) == "win":
        return "win"
    elif not 0 in goban.banmen:
        return "draw"
    else:
        return "continue"


def judge_single_player(goban, playerID):
    occupied = np.array(np.where(goban.banmen == playerID)).T
    for coor1, coor2 in combinations(occupied, 2):
        diffset = set(np.absolute(coor1 - coor2)) - set([0])
        if diffset == set([3]):
            mid1 = (coor2 + (coor1 - coor2) * 1 / 3).astype(np.int)
            mid2 = (coor2 + (coor1 - coor2) * 2 / 3).astype(np.int)
            if goban.banmen[mid1[0], mid1[1]] == playerID and\
                    goban.banmen[mid2[0], mid2[1]] == playerID:
                return "win"
    return "not"


def check_correct(goban, goisi_row, goisi_column):
    if not 1 in goban.banmen and not 2 in goban.banmen:  # １手目かどうかの判定
        if goisi_row == 8:
            return "OK"  # １手目、かつ接地している場合 "OK" を返す
        else:
            return "NG"  # 接地していない場合にNG
    elif not goban.banmen[goisi_row][goisi_column] == 0:  # 重複しているかどうかの判定（0以外なら重複）
        return "NG"  # 重複してるならば "NG" を返す
    elif goisi_row == 8:  # 置いた碁石が一番下かどうか（0ならば下にいる）
        if goban.banmen[goisi_row][goisi_column - 1] == 0 \
                and goban.banmen[goisi_row][goisi_column + 1] == 0:  # 一番下に置くとき、両側に碁石があるかの判定
            return "NG"  # 両側に碁石がなければ "NG" を返す
        else:
            return "OK"
    elif goban.banmen[goisi_row + 1][goisi_column] == 0:  # 中空に碁石があるかどうかの判定
        return "NG"  # 中空に碁石がある場合 "NG" を返す
    else:
        return "OK"
