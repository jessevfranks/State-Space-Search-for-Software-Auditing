class State:
    def __init__(self, h_cost, g_cost, username, password, parent, path):
        self.h_cost = h_cost
        self.g_cost = g_cost
        self.username = username
        self.password = password
        self.parent = parent
        self.path = path

        self.total_cost = 0
        self.total_cost += self.h_cost
        self.total_cost += self.g_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost