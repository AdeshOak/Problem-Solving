/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    // Create an object to store the indices of the elements
    const numToIndex = {};

    // Iterate through the array of numbers
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;

        // Check if the complement is already in the object
        if (complement in numToIndex) {
            // If found, return the indices of the complement and the current number
            return [numToIndex[complement], i];
        }

        // If not found, add the current number and its index to the object
        numToIndex[num] = i;
    }

    // If no solution is found, return an empty array (although the problem guarantees a solution)
    return [];
};