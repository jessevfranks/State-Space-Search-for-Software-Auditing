def reconstruct_path(goal_state):
    """
    Walks backward from the goal state to the start state
    to reconstruct the winning path.
    """
    path = []
    current = goal_state
    while current is not None:
        # Add the step to the beginning of the list
        path.insert(0, {
            "user": current.username,
            "pass": current.password
        })
        current = current.parent
    return path


def generate_report(goal_state, total_states_explored, start_time):
    """
    Generates the final report.
    """
    if goal_state is None:
        print("===================================================")
        print("Automated Audit Report")
        print("===================================================")
        print("Status: VULNERABILITY NOT FOUND")
        print(f"Total States Explored: {total_states_explored}")

        return

    # Reconstruct the path
    winning_path = reconstruct_path(goal_state)
    final_payload = winning_path[-1]  # The last step is the winning one

    print("\n" + "=" * 51)
    print("Automated Audit Report")
    print("=" * 51)
    print("Status: VULNERABILITY DISCOVERED")
    print(f"Target URL: http://localhost:5000/login")  # You'll need to pass config in
    print(f"Goal State: HTML contains 'Welcome, admin!'")

    print("Winning Exploit Path")
    print(f"  Username Input: {final_payload['user']}")
    print(f"  Password Input: {final_payload['pass']}")

    print("\nSearch Statistics")
    print(f"  Total States Explored: {total_states_explored}")
    print(f"  Cost of Exploit g(n): {goal_state.g_cost}")
    print(f"  Path Length (steps): {len(winning_path) - 1}")
    print(f"  Time Elapsed: {(time.time() - start_time):.2f} seconds")


# --- Example of how to run it all ---
import time
from auditor import *


if __name__ == "__main__":
    start_time = time.time()
    start_username = "admin"
    start_password = "password"

    # Run the audit
    final_informed_state = run_informed_audit(start_username, start_password)
    #final_uninformed_state = run_uninformed_audit(start_username, start_password)

    # You'd get total_states_explored from len(closed_set),
    # which you'd need to return from run_audit
    generate_report(final_informed_state, total_states_explored=999, start_time=start_time)