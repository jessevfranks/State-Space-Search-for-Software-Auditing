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


def generate_report(informed_state, uninformed_state, informed_time, uninformed_time):
    """
    Generates the final report comparing both algorithms.
    """
    primary_result = informed_state if informed_state else uninformed_state

    if primary_result is None:
        print("Status: VULNERABILITY NOT FOUND (Both algorithms failed/timed out)")
        return

    winning_path = reconstruct_path(primary_result)
    final_payload = winning_path[-1]

    print("Status: VULNERABILITY DISCOVERED")
    print(f"Target URL: http://localhost:5000/login")
    print(f"Goal State: HTML contains 'Welcome, admin!'")
    print("-" * 60)
    print("Winning Exploit Path:")
    print(f"  Username Input: {final_payload['user']}")
    print(f"  Password Input: {final_payload['pass']}")

    print("-" * 60)
    print(f"{'PERFORMANCE COMPARISON':^60}")
    print("-" * 60)
    print(f"{'Metric':<25} | {'Informed (A*)':<15} | {'Uninformed (BFS)':<15}")
    print("-" * 60)

    print(f"{'Time Elapsed (s)':<25} | {informed_time:<15.4f} | {uninformed_time:<15.4f}")

    inf_cost = informed_state.g_cost if informed_state else "N/A"
    uninf_cost = uninformed_state.g_cost if uninformed_state else "N/A"
    print(f"{'Path Cost (g)':<25} | {str(inf_cost):<15} | {str(uninf_cost):<15}")

    inf_len = len(reconstruct_path(informed_state)) - 1 if informed_state else "N/A"
    uninf_len = len(reconstruct_path(uninformed_state)) - 1 if uninformed_state else "N/A"
    print(f"{'Path Length (steps)':<25} | {str(inf_len):<15} | {str(uninf_len):<15}")
    print("=" * 60)


from auditor import *

if __name__ == "__main__":
    start_username = "admin"
    start_password = "password"

    # Run the audit
    start_t_informed = time.time()
    final_informed_state = run_informed_audit(start_username, start_password)
    end_t_informed = time.time()
    informed_duration = end_t_informed - start_t_informed

    start_t_uninformed = time.time()
    final_uninformed_state = run_uninformed_audit(start_username, start_password) # not in report, here as a comparison
    end_t_uninformed = time.time()
    uninformed_duration = end_t_uninformed - start_t_uninformed

    generate_report(final_informed_state, final_uninformed_state, informed_duration, uninformed_duration)