class BinarySearch(list):
    """docstring for BinarySearch"""

    def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(b, ((a * b) + b)), b)
        self.length = a

    def search(self, item):
        start = 0
        stop = self.length - 1
        result = {'count': 0, 'index': None}
        while start <= stop:
            midpoint = (start + stop) // 2
            # Increment count for each iteration
            result['count'] = result.get('count') + 1
            if self[midpoint] == item:
                # Set value of index as midpoint
                result['index'] = midpoint
                break
            else:
                if item < self[midpoint]:
                    stop = midpoint - 1
                else:
                    start = midpoint + 1
        return result
