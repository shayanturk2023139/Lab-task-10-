class UniqueIterator:

        def _init_(self, iterable):
        self.iterable = iterable
        self.visited = set()
        self.index = 0

    def _iter_(self):
        return self

    def _next_(self):
        while self.index < len(self.iterable):
            element = self.iterable[self.index]
            self.index += 1
            if element not in self.visited:
                self.visited.add(element)
                return element
        raise StopIteration


# Example usage:
if _name_ == "_main_":
    # Test the iterator with a list containing duplicates
    my_list = [1, 2, 2, 3, 4, 4, 5]

    unique_iterator = UniqueIterator(my_list)

    print("Original list:", my_list)
    print("Unique elements:", list(unique_iterator))
