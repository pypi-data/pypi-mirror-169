from threading import Thread


def threaded(func):
    """Decorator to run a function in a separate thread."""
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread
    return wrapper
