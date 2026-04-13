from datetime import datetime

def log(action, status):
    return {
        'action': action,
        'status': status,
        'timestamp': datetime.utcnow().isoformat()
    }
