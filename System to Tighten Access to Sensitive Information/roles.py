from collections import OrderedDict

class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, role):
        if role in self.cache:
            self.cache.move_to_end(role)
            return self.cache[role]
        return None

    def set(self, role, message):
        if role in self.cache:
            self.cache.move_to_end(role)
            self.cache[role] = message
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[role] = message

    def _complexity(self):
        return {
            'get': 'O(1)',
            'set': 'O(1)',
            'space': 'O(N)'
        }
