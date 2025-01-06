# Top ‘K’ Elements

The Top ‘K’ Elements pattern finds the top k largest or smallest elements in an array or stream of data using heaps or sorting.

## Sample Problem:
Find the k-th largest element in an unsorted array.

### Example:

- Input: nums = [3, 2, 1, 5, 6, 4], k = 2
- Output: 5

### Explanation:
1. Use a min-heap of size k to keep track of the k largest elements.
2. Iterate through the array, adding elements to the heap.
3. If the heap size exceeds k, remove the smallest element from the heap.
4. The root of the heap will be the k-th largest element.

## LeetCode Problems:
1. Kth Largest Element in an Array (LeetCode #215)
2. Top K Frequent Elements (LeetCode #347)
3. Find K Pairs with Smallest Sums (LeetCode #373)

