def plan_action(intent):
    actions = {
        'refund_request': 'issue_refund',
        'cancel_subscription': 'cancel_subscription',
        'update_address': 'update_address'
    }
    return actions.get(intent, None)
