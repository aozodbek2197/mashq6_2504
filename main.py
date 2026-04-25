from typing import List

class MergeSorter:
    def sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result: List[int] = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


if __name__ == "__main__":
    sorter = MergeSorter()
    print(sorter.sort([5, 2, 9, 1, 5, 6]))
