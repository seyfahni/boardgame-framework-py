from collections.abc import Callable


class MovePolicy:

    def is_valid(self, changes: dict, state) -> bool:
        pass


class InvertedMovePolicy(MovePolicy):

    def __init__(self, move_policy: MovePolicy):
        self.move_policy = move_policy

    def is_valid(self, changes: dict, state) -> bool:
        return not self.move_policy.is_valid(changes, state)


class AndMovePolicy(MovePolicy):

    def __init__(self, *move_policies: MovePolicy):
        self.move_policies = move_policies

    def is_valid(self, changes: dict, state) -> bool:
        for move_policy in self.move_policies:
            if not move_policy.is_valid(changes, state):
                return False
        return True


class OrMovePolicy(MovePolicy):

    def __init__(self, *move_policies: MovePolicy):
        self.move_policies = move_policies

    def is_valid(self, changes: dict, state) -> bool:
        for move_policy in self.move_policies:
            if move_policy.is_valid(changes, state):
                return True
        return False


class ChangeCountMovePolicy(MovePolicy):

    def __init__(self, change_count_check: Callable[[int], bool]):
        self.change_count_check = change_count_check

    def is_valid(self, changes: dict, state) -> bool:
        return self.change_count_check(len(changes))
