/*
Sample Input
6

Sample Output
     #
    ##
   ###
  ####
 #####
######
*/

function staircase(n) {
  for (let i = 1; i <= n; i++) {
    let line = "";

    for (let j = 1; j <= n; j++) {
      if (j <= n - i) {
        line += " ";
      } else {
        line += "#";
      }
    }

    console.log(line);
  }
}

staircase(6);
