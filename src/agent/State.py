class State:
    def __init__(self, h_cost, g_cost, username, password, parent):
        self.h_cost = h_cost
        self.g_cost = g_cost # tracked by number of mutations done
        self.username = username
        self.password = password
        self.parent = parent

        self.total_cost = 0
        self.total_cost += self.h_cost
        self.total_cost += self.g_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost