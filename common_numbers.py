###

# takes two sorted arrays of integers as input and returns an array containing 
# numbers common to both arrays without duplicates.




# Solution with below Efficient: 
# Linear time (O(n + m)) due to the sorted nature of arrays.
# Space-efficient: O(1) additional space used for pointers and result list.
# No extra space for sets: Just pointers and result list.
# No duplicates: Controlled via last_added tracking.
# Encapsulated logic: Easy to reuse and extend as part of a class.

# Program that finds common elements in two sorted arrays without duplicates



class CommonElementsFinder:
    def __init__(self, array1, array2):
        """
        Initialize with two sorted integer arrays.
        """
        self.array1 = array1
        self.array2 = array2

    def find_common(self):
        """
        Finds common elements without duplicates using a two-pointer approach.
        Returns a list of common integers.
        """
        result = []
        i, j = 0, 0
        last_added = None

        while i < len(self.array1) and j < len(self.array2):
            a, b = self.array1[i], self.array2[j]

            if a == b:
                if a != last_added:  # Avoid duplicates
                    result.append(a)
                    last_added = a
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1

        return result


# Example usage:
if __name__ == "__main__":
    arr1 = [1, 2, 2, 3, 4, 5, 6]
    arr2 = [2, 2, 4, 6, 6, 7]

    finder = CommonElementsFinder(arr1, arr2)
    print("Common elements:", finder.find_common())
