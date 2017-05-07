from django.shortcuts import render
import numpy as np
from .goban import Goban
from .util import separate_row_and_column
from .check import judgea


def display(request):

    message = None
    goban = None

    if request.session.get('goban_list') == None:
        init_goban_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        goban_list = request.session.get('goban_list', init_goban_list)
        request.session['goban_list'] = goban_list
        goban = Goban(np.array(request.session.get('goban_list')))

        player_id = request.session.get('player_id', 1)
        request.session['player_id'] = player_id

        if request.method == "GET":

            game_data = {
                'goban_list': goban.banmen.tolist(),
                'player_id': request.session['player_id'],
                'message': message,
            }

            return render(request, 'game/game.html', game_data)

    else:
        goban = Goban(np.array(request.session.get('goban_list')))
        row, column = separate_row_and_column(request.POST["id"])

        try:
            goban.add(8 - int(row), int(column),
                      request.session.get('player_id'))
            request.session['goban_list'] = goban.banmen.tolist()

            print("aaa")
            print(type(request.session['player_id']))
            judge = judgea(goban, request.session['player_id'])
            print("bbb")

            if judge == "continue":
                if request.session.get('player_id') == 1:
                    request.session['player_id'] = 2
                else:
                    request.session['player_id'] = 1

            elif judge == "win":
                del request.session['goban_list']
                message = str(request.session['player_id']) + "の勝ち"

            else:
                del request.session['goban_list']
                message = "引き分け"

        except:
            message = "もう一度入力してください"

    game_data = {
        'goban_list': goban.banmen.tolist(),
        'player_id': request.session['player_id'],
        'message': message,
    }

    return render(request, 'game/game.html', game_data)
