
class ReverseIterator:
    def _init_(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def _iter_(self):
        return self

    def _next_(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        raise StopIteration


# Example usage:
if _name_ == "_main_":
    # Test the iterator with a list of strings
    string_list = ["apple", "banana", "cherry", "date"]

    reverse_iterator = ReverseIterator(string_list)

    print("Original list:", string_list)
    print("Reversed order:", list(reverse_iterator))