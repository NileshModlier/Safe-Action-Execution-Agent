from agents.action_planner import plan_action
from agents.action_validator import validate_action
from agents.action_executor import execute_action
from agents.audit_logger import log

state = {'requires_human': False}
intent = 'refund_request'
action = plan_action(intent)
valid, reason = validate_action(action, state)
if valid:
    result = execute_action(action)
    audit = log(action, 'SUCCESS')
    print(result)
    print(audit)
else:
    print('Blocked:', reason)
