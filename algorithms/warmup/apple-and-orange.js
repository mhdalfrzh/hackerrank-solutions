/*
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.
Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?
For example, Sam's house is between s = 7 and t = 10. The apple tree is located at a = 4 and the orange at b = 12. There are m = 3 apples and n = 3 oranges. Apples are thrown apples = [2, 3, -4] units distance from a, and oranges = [3, -2, -4] units distance. Adding each apple distance to the position of the tree, they land at [4+2, 4+3, 4+(-4)] = [6, 7, 0]. Oranges land at [12+3, 12+(-2), 12+(-4)] = [15, 10, 8]. One apple and two oranges land in the inclusive range 7-10 so we print
1
2

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.

Sample Input
7 11
5 15
3 2
-2 2 1
5 -6

Sample Output 0
1
1
*/

function countApplesAndOranges(s, t, a, b, apples, oranges) {
  let totalApple = 0,
    totalOrange = 0;
  for (let i = 0; i < apples.length; i++) {
    apples[i] = apples[i] + a;
    if (apples[i] >= s && apples[i] <= t) {
      totalApple++;
    }
  }
  for (let i = 0; i < oranges.length; i++) {
    oranges[i] = oranges[i] + b;
    if (oranges[i] >= s && oranges[i] <= t) {
      totalOrange++;
    }
  }

  console.log(totalApple);
  console.log(totalOrange);
}
