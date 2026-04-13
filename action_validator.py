def validate_action(action, state):
    if action is None:
        return False, 'No valid action'
    if state.get('requires_human'):
        return False, 'Human escalation required'
    return True, 'Action validated'
