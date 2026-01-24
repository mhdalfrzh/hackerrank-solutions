/*
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
- The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
- int x1, int v1: starting position and jump distance for kangaroo 1
- int x2, int v2: starting position and jump distance for kangaroo 2

Sample Input
0 3 4 2

Sample Output
YES

Sample Input
0 2 5 3

Sample Output
NO
*/

function kangaroo(x1, v1, x2, v2) {
  if (v1 <= v2) {
    return "NO";
  } else {
    if ((x2 - x1) % (v1 - v2) === 0) {
      return "YES";
    } else {
      return "NO";
    }
  }
}

console.log(kangaroo(0, 3, 4, 2));

/*
ASAL RUMUS
Dua kanguru:
Kanguru 1 mulai di x1, lompat v1 tiap lompatan
Kanguru 2 mulai di x2, lompat v2 tiap lompatan

Setelah n lompatan:
Posisi kanguru 1:
x1 + n·v1

Posisi kanguru 2:
x2 + n·v2

Mereka ketemu kalau posisinya sama:
x1 + n·v1 = x2 + n·v2
n·v2 - n·v1 = x1 - x2
n = (x2 - x1) / (v1 - v2)

Supaya n itu bilangan bulat, maka:
(x2 - x1) habis dibagi (v1 - v2)
*/
