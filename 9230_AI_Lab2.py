# Define the initial state of the problem
initial_state = {
    'jug1': 0,
    'jug2': 0,
    'goal': 4
}

# Define the rules for the production system
rules = [
    {
        'condition': lambda state: state['jug1'] < 3,
        'action': lambda state: {'jug1': 3, 'jug2': state['jug2']}
    },
    {
        'condition': lambda state: state['jug2'] < 4,
        'action': lambda state: {'jug1': state['jug1'], 'jug2': 4}
    },
    {
        'condition': lambda state: state['jug1'] > 0,
        'action': lambda state: {'jug1': 0, 'jug2': state['jug2']}
    },
    {
        'condition': lambda state: state['jug2'] > 0,
        'action': lambda state: {'jug1': state['jug1'], 'jug2': 0}
    },
    {
        'condition': lambda state: state['jug1'] > 0 and state['jug2'] < 4,
        'action': lambda state: {
            'jug1': max(0, state['jug1'] - (4 - state['jug2'])),
            'jug2': min(4, state['jug2'] + state['jug1'])
        }
    },
    {
        'condition': lambda state: state['jug2'] > 0 and state['jug1'] < 3,
        'action': lambda state: {
            'jug1': min(3, state['jug1'] + state['jug2']),
            'jug2': max(0, state['jug2'] - (3 - state['jug1']))
        }
    }
]

# Define the production system function
def production_system(initial_state, rules):
    state = initial_state
    while state['jug1'] != state['goal'] and state['jug2'] != state['goal']:
        applied_rule = False
        for rule in rules:
            if rule['condition'](state):
                state.update(rule['action'](state))
                applied_rule = True
                break
        if not applied_rule:
            raise Exception('No applicable rule found')
    return state

# Test the production system
print(production_system(initial_state, rules))
