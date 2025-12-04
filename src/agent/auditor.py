from collections import deque

from helpers import *
import heapq
from State import *
import time

def run_informed_audit(start_username, start_password):
    """
    Implementation of the A* algorithm
    """
    # heap to hold States needing to be explored
    open_states = []

    # set to hold explored tuples of (username, password)
    explored = set()

    first_state = State(
        heuristic_cost(start_username, start_password),
        0,
        start_username,
        start_password,
        None,
    )
    heapq.heappush(open_states, first_state)
    explored.add((start_username, start_password))
    states_found = 1

    while open_states:
        curr_state = heapq.heappop(open_states)
        print(f"""Exploring state with:
              username: {curr_state.username}
              password: {curr_state.password}
              cost: {curr_state.total_cost}""")

        if curr_state.h_cost == 0:
            print(f"Achieved goal state with username: {curr_state.username} and password: {curr_state.password}")
            print(f"Found {states_found} states")
            print(f"Path cost {curr_state.g_cost}")
            return curr_state

        mutations = generate_mutations(curr_state)

        for new_username, new_password in mutations:
            if (new_username, new_password) in explored:
                continue

            explored.add((new_username, new_password))

            h_cost = heuristic_cost(new_username, new_password)
            g_cost = curr_state.g_cost + 1

            new_state = State(
                h_cost,
                g_cost,
                new_username,
                new_password,
                curr_state,
            )
            heapq.heappush(open_states, new_state)
            states_found += 1

    print("Could not reach goal state")
    print(f"Found {states_found} states")
    return None

def run_uninformed_audit(start_username, start_password):
    """
    BFS implementations
    """
    start_time = time.time()
    time_limit_seconds = 5 * 60 # 5 minutes

    # queue to hold States needing to be explored
    open_states = deque()

    # set to hold explored tuples of (username, password)
    explored = set()

    first_state = State(
        fake_heuristic(start_username, start_password),
        0,
        start_username,
        start_password,
        None,
    )
    states_found = 1
    open_states.append(first_state)
    explored.add((start_username, start_password))

    while open_states:
        # Check if time limit has been exceeded
        if time.time() - start_time > time_limit_seconds:
            print(f"Time limit of {time_limit_seconds} seconds reached. Stopping audit.")
            print(f"Found {states_found} states")
            return None

        curr_state = open_states.popleft()
        print(f"""Exploring state with:
                  username: {curr_state.username}
                  password: {curr_state.password}
                  cost: {curr_state.total_cost}""")

        if curr_state.h_cost == 0:
            print(f"Achieved goal state with username: {curr_state.username} and password: {curr_state.password}")
            print(f"Found {states_found} states")
            print(f"Path cost {curr_state.g_cost}")
            return curr_state

        mutations = generate_mutations(curr_state)

        for new_username, new_password in mutations:
            if (new_username, new_password) in explored:
                continue

            explored.add((new_username, new_password))

            new_state = State(
                fake_heuristic(new_username, new_password),
                curr_state.g_cost+1,
                new_username,
                new_password,
                curr_state,
            )
            open_states.append(new_state)
            states_found += 1

    print("Could not reach goal state")
    print(f"Found {states_found} states")
    return None