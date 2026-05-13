class Results:
    def __init__(self, victories:int, draws:int, losses:int):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def get_number_of_wins(self) -> str:
        return f'Футбольных побед: {self.victories}'

    def get_number_of_draws(self) -> str:
        return f'Футбольных ничьих: {self.draws}'

    def get_number_of_losses(self) -> str:
        return f'Футбольных поражений: {self.losses}'

    def get_total_points(self) -> str:
        total = self.victories * 3 + self.draws
        return f'Общее количество очков: {total}'

class Hockey(Results):
    def get_number_of_wins(self) -> str:
        return f'Хоккейных побед: {self.victories}'

    def get_number_of_draws(self) -> str:
        return f'Хоккейных ничьих: {self.draws}'

    def get_number_of_losses(self) -> str:
        return f'Хоккейных поражений: {self.losses}'

    def get_total_points(self) -> str:
        total = self.victories * 2 + self.draws
        return f'Общее количество очков: {total}'

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in [football_team, hockey_team]:
    print(f'{team.get_number_of_wins()}'
          f'\n{team.get_number_of_draws()}'
          f'\n{team.get_number_of_losses()}'
          f'\n{team.get_total_points()}')