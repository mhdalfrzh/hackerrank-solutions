/*
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zeros. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Sample Input
6
-4 3 -9 0 4 1

Sample Output
0.500000
0.333333
0.166667
*/

function plusMinus(arr) {
  let positive = 0;
  let negative = 0;
  let zero = 0;
  const total = arr.length;

  for (let num of arr) {
    if (num > 0) {
      positive++;
    } else if (num < 0) {
      negative++;
    } else {
      zero++;
    }
  }

  console.log((positive / total).toFixed(6));
  console.log((negative / total).toFixed(6));
  console.log((zero / total).toFixed(6));
}

plusMinus([-4, 3, -9, 0, 4, 1]);
