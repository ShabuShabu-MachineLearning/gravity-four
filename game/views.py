from django.shortcuts import render


def display(request):

    print(request)
    print(request.session.get('goban_list'))

    init_goban_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 2, 0, 0, 0, 0],
                       [0, 0, 0, 2, 1, 2, 0, 0, 0],
                       [0, 0, 0, 1, 2, 1, 0, 0, 0]]

    goban_list = request.session.get('goban_list', init_goban_list)
    request.session['goban_list'] = goban_list

    game_data = {
        'goban_list': goban_list,
    }

    return render(request, 'game/game.html', game_data)
