# Define the initial state of the problem
initial_state = (3, 3, 1)

# Define the goal state of the problem
goal_state = (0, 0, 0)

# Define the set of rules for the production system
rules = [
    # Rule 1: Move 2 missionaries
    (lambda state: state[0] >= 2, lambda state: (state[0] - 2, state[1], 0)),
    
    # Rule 2: Move 2 cannibals
    (lambda state: state[1] >= 2, lambda state: (state[0], state[1] - 2, 0)),
    
    # Rule 3: Move 1 missionary and 1 cannibal
    (lambda state: state[0] >= 1 and state[1] >= 1, lambda state: (state[0] - 1, state[1] - 1, 0)),
    
    # Rule 4: Move 1 missionary
    (lambda state: state[0] >= 1, lambda state: (state[0] - 1, state[1], 0)),
    
    # Rule 5: Move 1 cannibal
    (lambda state: state[1] >= 1, lambda state: (state[0], state[1] - 1, 0)),
    
    # Rule 6: Move 2 missionaries back
    (lambda state: state[0] <= 1 and state[1] <= 2 and state[2] == 0, lambda state: (state[0] + 2, state[1], 1)),
    
    # Rule 7: Move 2 cannibals back
    (lambda state: state[0] <= 2 and state[1] <= 1 and state[2] == 0, lambda state: (state[0], state[1] + 2, 1)),
    
    # Rule 8: Move 1 missionary and 1 cannibal back
    (lambda state: state[0] <= 2 and state[1] <= 2 and state[2] == 0, lambda state: (state[0] + 1, state[1] + 1, 1)),
    
    # Rule 9: Move 1 missionary back
    (lambda state: state[0] <= 2 and state[2] == 0, lambda state: (state[0] + 1, state[1], 1)),
    
    # Rule 10: Move 1 cannibal back
    (lambda state: state[1] <= 2 and state[2] == 0, lambda state: (state[0], state[1] + 1, 1))
]

# Define the production system function
def production_system(state, rules):
    for rule in rules:
        if rule[0](state):
            new_state = rule[1](state)
            return new_state
    return None

# Solve the problem using the production system approach
current_state = initial_state
path = [current_state]

while current_state != goal_state:
    new_state = production_system(current_state, rules)
    if new_state is None:
        break
    path.append(new_state)
    current_state = new_state

# Print the solution path
for state in path:
    print(state)
