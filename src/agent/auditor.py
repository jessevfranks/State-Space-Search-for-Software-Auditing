from helpers import *
import heapq
import State

def run_audit(start_username, start_password):
    """
    Implementation of the A* algorithm
    """
    # heap to hold States needing to be explored
    open = []

    # set to hold explored tuples of (username, password)
    explored = set()

    first_state = State(
        heuristic_cost(start_username, start_password),
        path_cost(start_username, start_password),
        start_username,
        start_password,
        None,
        [],
    )
    heapq.heappush(open, first_state)
    explored.add((start_username, start_password))

    while open:
        curr_state = open.pop()

        if curr_state.h_cost == 0:
            print(f"Achieved goal state with username: {curr_state.username} and password: {curr_state.password}")
            return curr_state

        mutations = generate_mutations(curr_state)

        for new_username, new_password in mutations:
            if (new_username, new_password) in explored:
                continue

            explored.add((new_username, new_password))

            h_cost = heuristic_cost(new_username, new_password)
            g_cost = path_cost(new_username, new_password)

            new_state = State(
                h_cost,
                g_cost,
                new_username,
                new_password,
                curr_state,
                curr_state.path.append(new_username),
            )
            heapq.heappush(open, new_state)

    print("Could not reach goal state")
    return None