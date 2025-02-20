class SortableArray:
    def __init__(self, array: list) -> None:
        self.array = array
    def part(self, left: int, right: int) -> int:
        pivot_index = right
        pivot = self.array[pivot_index]
        right -= 1
        while True:
            while self.array[left] < pivot and left < len(self.array):
                left += 1

            while self.array[right] > pivot and right >= 0:
                right -= 1

            if left >= right:
                break
            else:
                self.array[left], self.array[right] = self.array[left], self.array[right]
                left += 1

        self.array[left], self.array[pivot_index] = self.array[pivot_index], self.array[left]
        return left


    def quicksort(self, left: int, right: int) -> None:
        if right - left <= 0:
            return

        pivot_index = self.part(left, right)
        self.quicksort(left, pivot_index - 1)
        self.quicksort(pivot_index + 1, right)



if __name__ == "__main__":
    array = [5, 4, 3, 2, 6, 1, 7, 8, 9]
    test_arr = SortableArray(array)
    test_arr.quicksort(0, len(array) - 1)
    print(test_arr.array)
# test