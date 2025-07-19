/*
Given an array of integers, find the sum of its elements.

Sample Input
6
1 2 3 4 10 11

Sample Output
31
*/

function simpleArraySum(ar) {
  let sum = 0;
  for (let num of ar) {
    sum += num;
  }

  return sum;
}

console.log(simpleArraySum([1, 2, 3, 4, 10, 11]));
