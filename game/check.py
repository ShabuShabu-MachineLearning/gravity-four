import numpy as np


def check_correct(goban, goisi_row, goisi_column):
    if 0 in goban.banmen:  # １手目かどうかの判定
        if goisi_row == 0:
            return "OK"  # １手目、かつ接地している場合 "OK" を返す
        else:
            return "NG"  # 接地していない場合にNG
    elif not goban.banmen[goisi_row][goisi_column] == 0:  # 重複しているかどうかの判定（0以外なら重複）
        return "NG"  # 重複してるならば "NG" を返す
    elif goisi_row == 0:  # 置いた碁石が一番下かどうか（0ならば下にいる）
        if goban.banmen[goisi_row][goisi_column - 1] == 0 \
                and goban.banmen[goisi_row][goisi_column + 1] == 0:  # 一番下に置くとき、両側に碁石があるかの判定
            return "NG"  # 両側に碁石がなければ "NG" を返す
    elif goban.banmen[goisi_row - 1][goisi_column] == 0:  # 中空に碁石があるかどうかの判定
        return "NG"  # 中空に碁石がある場合 "NG" を返す
    else:
        return "OK"
