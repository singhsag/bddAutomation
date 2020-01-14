

class CucumberBasket:
    def __init__(self, initial_count=0, max_count=10):
        if initial_count < 0:
            raise ValueError("Initial cucumber basket must not be negative")
        if max_count < 0:
            raise ValueError("Initial cucumber basket must not be negative")
        self._count = initial_count
        self._max_count = max_count

    @property
    def count(self):
        return self._count

    @property
    def full(self):
        return self._max_count

    @property
    def empty(self):
        return self._count == 0

    @property
    def maxCount(self):
        return self._max_count

    def add(self, count=1):
        new_count = self._count + count
        if new_count > self._max_count:
            raise ValueError("Attempt to add too many cucumbers")
        self._count = new_count

    def remove(self, count=1):
        new_count = self._count - count
        if new_count < 0:
            raise ValueError("Attempt to remove too many cucumbers")
        self._count = new_count


# cb = CucumberBasket()
# cb.add(0)
# print(cb.count)
# print(cb.empty)
