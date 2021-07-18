/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
// map
var twoSum = function (numbers, target) {
    let map = new Map();
    for (let i = 0; i < numbers.length; i++) {
        map.set(numbers[i], i + 1);
    }

    for (let i = 0; i < numbers.length; i++) {
        let diff = target - numbers[i];
        if (map.has(diff) && map.get(diff) !== i + 1) {
            return [i + 1, map.get(diff)]
        }
    }
};



/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
// Two pointers
var twoSum = function (numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        if (numbers[left] + numbers[right] > target) {
            right--;
        }

        if (numbers[left] + numbers[right] < target) {
            left++;
        }

        if (numbers[left] + numbers[right] === target) {
            break;
        }
    }

    return [left + 1, right + 1];
};