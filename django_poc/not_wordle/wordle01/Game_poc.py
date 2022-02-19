import pandas as pd


class Game:
    word_length = 5
    word_to_guess = list('WURST'.lower())

    def __init__(self):
        self.get_random_game()
        self.current_round = 0

    def get_random_game(self):
        self.game_grid = pd.DataFrame()

    def visualize_matches(self, x):
        df = pd.DataFrame('', index=x.index, columns=x.columns)
        for row in range(len(x.index)):
            for col in range(len(x.columns)):
                color = 'gray'
                if self.game_grid.iloc[row, col] == self.word_to_guess[col]:
                    color = 'green'
                elif self.game_grid.iloc[row, col] in self.word_to_guess:
                    color = 'yellow'
                df.iloc[row, col] = 'background-color: %s' % color
        return df

    def display(self):
        display(self.game_grid.style.apply(
            self.visualize_matches, axis=None))

    def string_to_dic(self, word):
        result = {}
        l = list(word)
        for idx in range((len(word))):
            result[idx] = l[idx]
        return result

    def guess(self):
        self.game_grid = self.game_grid.append(
            self.string_to_dic(self.guessed_word), ignore_index=True)
        return self

    def read_a_world_from_user(self):
        desired_length = len(self.word_to_guess)
        while True:
            a_word = input(f'Guess a word with {desired_length} letters.')
            if len(a_word) == desired_length:
                break
        self.guessed_word = a_word.lower()
        return self
