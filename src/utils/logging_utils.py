import time

def log_step(message):
    """Utility function to log steps with timestamps"""
    print(f"\n[{time.strftime('%H:%M:%S')}] {message}")