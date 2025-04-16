class TransactionStorage:
    def __init__(self):
        self.transaction_stack = list()

    def _get_transaction_stack(self):
        return self.transaction_stack

    def begin(self, base_storage):
        if self.transaction_stack:
            self.transaction_stack.append(self.transaction_stack[-1].copy())
        else:
            self.transaction_stack.append(base_storage)

    def commit(self):
        if not self.transaction_stack:
            print("Транзакция еще не началась...")
            return

        last = self.transaction_stack.pop()

        if self.transaction_stack:
            self.transaction_stack[-1].update(last)
        else:
            self.storage.update(last)

    def rollback(self):
        if not self.transaction_stack:
            print("Транзакция еще не началась...")
            return
        self.transaction_stack.pop()
