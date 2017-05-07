from django.shortcuts import render


def display(request):

    print(request)

    goban_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 2, 0, 0, 0, 0],
                  [0, 0, 0, 2, 1, 2, 0, 0, 0],
                  [0, 0, 0, 1, 2, 1, 0, 0, 0]]

    game_data = {
        'goban_list': goban_list,
    }

    return render(request, 'game/game.html', game_data)
