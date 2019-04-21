class GameState:

    def __init__(self):
        pass

    def process_action(self, action):
        raise NotImplementedError

    def get_valid_actions(self):
        raise NotImplementedError

    def is_over(self):
        raise NotImplementedError

    def get_winner(self):
        raise NotImplementedError

    def display_game(self):
        raise NotImplementedError
