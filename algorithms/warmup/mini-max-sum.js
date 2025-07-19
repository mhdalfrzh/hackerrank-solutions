/*
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.

Sample Input
1 2 3 4 5

Sample Output
10 14
*/

function miniMaxSum(arr) {
  arr.sort((a, b) => a - b);

  let minSum = 0;
  let maxSum = 0;

  for (let i = 0; i < arr.length - 1; i++) {
    minSum += arr[i];
    maxSum += arr[arr.length - 1 - i];
  }

  console.log(minSum, maxSum);
}

miniMaxSum([1, 2, 3, 4, 5]);
