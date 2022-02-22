from django.http import HttpResponse
from django.template import loader
import pandas as pd
import requests
import random


def filter_by_size(words, size):
    return [word for word in words if len(word) == size]


def get_random_word():
    language = 'de' #Currently supported languages: [de, es, zh]
    word_length = 5
    response = requests.get(f'https://random-word-api.herokuapp.com/all/?lang={language}')
    response.raise_for_status()
    body = response.json()
    word = filter_by_size (body, word_length)
    rnd_word = random.choice(word)
    print(f"the random word is: {rnd_word}")
    return rnd_word


word_to_guess = list(get_random_word().lower())
desired_length = len(word_to_guess)
game_grid = pd.DataFrame()

def string_to_dic(word):
    result = {}
    l = list(word)
    for idx in range((len(word))):
        result[idx] = l[idx]
    return result

def visualize_matches(x):
    global game_grid
    df = pd.DataFrame('', index=x.index, columns=x.columns)
    for row in range(len(x.index)):
        for col in range(len(x.columns)):
            color = 'gray'
            if game_grid.iloc[row, col] == word_to_guess[col]:
                color = 'green'
            elif game_grid.iloc[row, col] in word_to_guess:
                color = 'yellow'
            df.iloc[row, col] = 'background-color: %s' % color
    return df

def guess(guessed_word):
    global game_grid
    game_grid = game_grid.append(string_to_dic(guessed_word), ignore_index=True)
     

def index(request):
    global game_grid
    a_word = request.POST.get('a_word', "XXXXX")
    if len(a_word) == desired_length:
        guessed_word = a_word.lower()
        guess(guessed_word)
    template = loader.get_template('wordle01/index.html')
    context = {
        'view_grid': game_grid.style.apply(visualize_matches, axis=None).to_html(),
    }
    return HttpResponse(template.render(context, request))
