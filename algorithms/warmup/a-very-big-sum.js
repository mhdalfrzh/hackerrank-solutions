/*
In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large.

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015
*/

function aVeryBigSum(ar) {
  let sum = 0;
  for (let num of ar) {
    sum += num;
  }

  return sum;
}

console.log(
  aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
);
