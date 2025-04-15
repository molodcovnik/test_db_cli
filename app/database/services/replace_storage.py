from functools import wraps


def use_current_transaction(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.transaction_stack:
            original_storage = self.storage
            self.storage = self.transaction_stack[-1]
            try:
                return func(self, *args, **kwargs)
            finally:
                self.storage = original_storage
        else:
            return func(self, *args, **kwargs)
    return wrapper
