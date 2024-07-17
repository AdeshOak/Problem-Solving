# Intuition
My first thought on how to solve this problem was to use a simple nested loop to check all pairs of numbers and see if they sum up to the target. However, this would be inefficient with a time complexity of ***O(n^2)***. To optimize, I thought of using a hash map (or an object in JavaScript) to store the indices of the numbers we've seen so far. This way, we can check in constant time if the complement (target - current number) exists.

# Approach
1. **Create an Object:** I used an object numToIndex to store each number in the array as the key and its index as the value.
2. **Iterate Through the Array:** For each number, I calculated its complement (i.e., target - num).
3. **Check for Complement:** If the complement exists in the object numToIndex, it means we have found the two numbers that add up to the target, and I returned their indices.
4. **Store the Index:** If the complement does not exist, I stored the current number and its index in the object.

This approach ensures that we only pass through the array once, making it efficient.

# Complexity
- Time complexity:
The time complexity of this approach is ***O(n)***, where n is the number of elements in the nums array. This is because we only iterate through the array once, and each lookup or insertion in the object is ***O(1)*** on average.

- Space complexity:
The space complexity is also ***O(n)*** since we store up to n elements in the object.