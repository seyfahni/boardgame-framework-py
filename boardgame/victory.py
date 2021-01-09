from boardgame import game


class VictoryCondition:

    def get_result(self, changes: dict, state) -> game.Result:
        pass


class PriorityVictoryCondition(VictoryCondition):

    def __init__(self, *victory_conditions: VictoryCondition):
        self.victory_conditions = victory_conditions

    def get_result(self, changes: dict, state) -> game.Result:
        for condition in self.victory_conditions:
            result = condition.get_result(changes, state)
            if result.get_victory_state() != game.VICTORY_UNDECIDED:
                return result
        return game.Result()
