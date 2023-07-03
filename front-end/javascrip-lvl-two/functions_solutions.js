// PROBLEM 1: SLEEPING IN
//
// Write a function called sleepIn that takes in two boolean parameters: weekday
// and vacation.
//
// The parameter weekday is true if it is a weekday, and the parameter vacation is
// true if we are on vacation. We sleep in if it is not a weekday or
// we're on vacation. Return true if we sleep in. So some example input and output:
let sleepIn = (weekday, vacation) => !weekday || vacation;
console.log(sleepIn(false, false))

// PROBLEM 2: MONKEY TROUBLE
//
// We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if
// each is smiling. We are in trouble if they are both smiling or if neither of
// them is smiling. Return true if we are in trouble.
let monkeyTrouble = (aSmile, bSmile) => (aSmile && bSmile) || (!aSmile && !bSmile);
console.log(monkeyTrouble(false, false))

// PROBLEM 3: STRING TIMES
//
// Given a string and a non-negative int n, return a larger
// string that is n copies of the original string.
let stringTimes = (str, n) => {
    returnStr = '';
    var i = 0;
    while (i<n){
        returnStr += str
        i++
    }
    return returnStr
}
console.log(stringTimes('Hi', 2))

// PROBLEM 4: LUCKY SUM

// Given 3 numerical values, a b c, return their sum. However, if one of the values is
// 13 then it does not count towards the sum and values to its right do not count.
// So for example, if b is 13, then both b and c do not count.
let luckySum = (a, b, c) => {
    if(a == 13){
        return 0
    } else if(b == 13){
        return a
    } else if(c == 13){
        return a+b
    } else {
        return a+b+c
    }
}
console.log(luckySum(1, 1, 2))

// PROBLEM 5:
//
// You are driving a little too fast, and a police officer stops you. Write code to
// compute the result, encoded as an int value: 0=no ticket, 1=small ticket,
// 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
// and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
// Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
let caughtSpeeding = (speed, birthday) => {
    if(birthday){
        speed -= 5
    }
    if(speed <= 60){
        return 0
    }
    if(speed > 60 && speed <=80){
        return 1
    }
    return 2
}
console.log(caughtSpeeding(85, false))

// BONUS: MAKE BRICKS
//
// We want to make a row of bricks that is goal inches long. We have a number of
// small bricks (1 inch each) and big bricks (5 inches each). Return true if it
// is possible to make the goal by choosing from the given bricks. This is a
// little harder than it looks and can be done without any loops in a single line!
let makeBricks = (small, big, goal) => goal%5 >= 0 && goal%5 - small <= 0 && small + 5*big >=goal;
console.log(makeBricks(3, 2, 9))

let ternaryMakeBricks = (small, big, goal) => goal%5 - small <= 0 && small +5*big >= goal ? true:false;
console.log(ternaryMakeBricks(3,2,10))

