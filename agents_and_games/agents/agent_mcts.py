import copy
import random
from math import sqrt, log


class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self) -> bool:
        return len(self.children) == len(self.state.get_valid_moves())

    def best_child(self, exploration_weight: float = 1.4) -> "Node":  # Forward reference
        return max(
            self.children,
            key=lambda child: (child.wins / child.visits) +
                              exploration_weight * sqrt(log(self.visits) / child.visits)
        )


class AgentMCTS:

    def __init__(
            self,
            game_constructor,
            players,
            max_depth: int = 999,
            iterations: int = 1000
        ) -> None:
        self.game_constructor = game_constructor
        self.players = players
        self.max_depth = max_depth
        self.iterations = iterations

    def search(self, root: Node) -> Node:
        for _ in range(self.iterations):
            node = self._select(node=root)
            # TODO-print:
            # node.state.display_board()
            # print(f"{node.state.player = }")
            reward = self._simulate(state=node.state)
            # TODO-print:
            # print(f"{reward = }")
            self._backpropagate(node=node, reward=reward)
        # TODO-print:
        # for node in root.children:
        #     node.state.display_board()
        #     print(f"{node.wins = }")
        #     print(f"{node.visits = }")
        return root.best_child(exploration_weight=0.0)

    def get_changed_position(self, list_1, list_2) -> tuple[int, int]:
        pos_y = [index for index, (element_1, element_2) in enumerate(zip(list_1, list_2)) if element_1 != element_2][0]
        pos_x = [index for index, (element_1, element_2) in enumerate(zip(list_1[pos_y], list_2[pos_y])) if element_1 != element_2][0]
        return (pos_y, pos_x)

    def get_move(self, game, silent=False) -> tuple[int, int]:
        best_move = None
        if game.is_game_over():
            return best_move
        root = Node(game)
        board_best_move = self.search(root=root).state
        best_move = self.get_changed_position(
            list_1=game.board,
            list_2=board_best_move.board,
        )
        return best_move

    def _select(self, node: Node) -> Node:
        while not node.state.is_game_over():
            # TODO-print:
            # n_empty = len([x for row in node.state.board for x in row if x == " "])
            # if n_empty < 40:
            #     print(f"{n_empty = }")
            if not node.is_fully_expanded():
                return self._expand(node=node)
            node = node.best_child()
        return node

    def _expand(self, node: Node) -> Node:
        moves = node.state.get_valid_moves()
        for move in moves:
            state_new = self._get_next_state(state=node.state, move=move)
            if not any(child.state.board == state_new.board for child in node.children):
                node_child = Node(state=state_new, parent=node)
                node.children.append(node_child)
                return node_child
        raise ValueError("All moves have been visited.")

    def _simulate(self, state: Node) -> float:
        state_cloned = self._clone_state(state=state)
        player_rewarded = self.players.P1.value if state_cloned.player == self.players.P2.value else self.players.P2.value  # player who made the last step to get the current state

        # TODO-print:
        # print(f"{state_cloned.player = }")
        # print(f"{player_rewarded = }")
        reward = 0 # game ends with a draw
        depth = 0
        while not state_cloned.is_game_over() and depth < self.max_depth:
            move = random.choice(state_cloned.get_valid_moves())
            state_cloned.make_move(move=move)
            depth += 1
        # TODO-print:
        # current_state.display_board()
        if state_cloned.is_winner(player=player_rewarded):
            reward = 1
        if state_cloned.is_winner(player=state_cloned.player):
            reward = -1
        return reward

    def _backpropagate(self, node: Node, reward: float, discount_factor: float = 0.9) -> None:
        discount = 1.0
        while node is not None:
            node.visits += 1
            node.wins += reward * discount  # Apply discount factor to reward
            discount *= discount_factor  # Reduce discount factor for next step
            reward = -reward  # Alternate reward for opponent
            node = node.parent

    def _get_next_state(self, state: Node, move: int) -> Node:
        state_new = self._clone_state(state=state)
        state_new.make_move(move=move)
        return state_new

    def _clone_state(self, state: Node) -> Node:
        state_new = self.game_constructor()
        state_new.board = copy.deepcopy(state.board)
        state_new.player = state.player
        return state_new
