/*
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Sample Input
07:05:45PM

Sample Output
19:05:45
*/

function timeConversion(s) {
  const ampm = s.slice(-2);
  let [hours, minutes, seconds] = s.slice(0, -2).split(":");

  if (ampm === "AM" && hours === "12") {
    hours = "00";
  } else if (ampm === "PM" && hours !== "12") {
    hours = String(Number(hours) + 12);
  }

  return `${hours}:${minutes}:${seconds}`;
}

console.log(timeConversion("07:05:45PM"));
console.log(timeConversion("12:00:00AM"));
