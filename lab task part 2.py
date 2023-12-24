 class ChunkIterator:
    def _init_(self, iterable, chunk_size):
        self.iterable = iterable
        self.chunk_size = chunk_size
        self.index = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.index < len(self.iterable):
            chunk = self.iterable[self.index:self.index + self.chunk_size]
            self.index += self.chunk_size
            return chunk
        raise StopIteration


# Example usage:
if _name_ == "_main_":
    # Test the iterator with a list of numbers and a chunk size of 3
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    chunk_iterator = ChunkIterator(numbers_list, 3)

    print("Original list:", numbers_list)
    print("Chunks of size 3:", list(chunk_iterator))
