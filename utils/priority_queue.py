from heapq import heappop, heappush
import itertools


class PriorityQueue:
    def __init__(self) -> None:
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of item to entries
        self.REMOVED = "<removed-task>"  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def is_in_queue(self, item):
        """Check if item is in queue"""
        return item in self.entry_finder

    def add_with_priority(self, item, priority):
        """Add new item with priority"""
        if item in self.entry_finder:
            raise ValueError("Item already in queue!")
        count = next(self.counter)
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heappush(self.pq, entry)

    def remove_item(self, item):
        """Mark existing item as REMOVED."""
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def change_priority(self, item, priority):
        """Change priority of existing item"""
        if item not in self.entry_finder:
            raise ValueError("Item not in queue!")

        self.remove_item(item)
        self.add_with_priority(item, priority)

    def pop(self):
        """Return item with lowest priority"""
        while self.pq:
            _, _, item = heappop(self.pq)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item

        return None
