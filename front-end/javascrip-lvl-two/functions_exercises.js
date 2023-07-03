// PROBLEM 1: SLEEPING IN
//
// Write a function called sleepIn that takes in two boolean parameters: weekday
// and vacation.
//
// The parameter weekday is true if it is a weekday, and the parameter vacation is
// true if we are on vacation. We sleep in if it is not a weekday or
// we're on vacation. Return true if we sleep in. So some example input and output:
//
// sleepIn(false, false) → true
// sleepIn(true, false) → false
// sleepIn(false, true) → true
function sleepIn(weekday, vacation){
    if(weekday == false){  
        console.log(true)
    } else if(vacation == true){
        console.log(true) 
    } else {
        console.log(false)
    }
}
console.log('PROBLEM 1: SLEEPING IN results:')
sleepIn(false, false)
sleepIn(true, false)
sleepIn(false, true)

// PROBLEM 2: MONKEY TROUBLE
//
// We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if
// each is smiling. We are in trouble if they are both smiling or if neither of
// them is smiling. Return true if we are in trouble.
//
// Example Input and Output
//
// monkeyTrouble(true, true) → true
// monkeyTrouble(false, false) → true
// monkeyTrouble(true, false) → false
function monkeyTrouble(aSmile, bSmile){
    if(aSmile === bSmile){
        console.log(true)
    } else {
        console.log(aSmile && bSmile)
    }
}
console.log(' ')
console.log('PROBLEM 2: MONKEY TROUBLE: solutions')
monkeyTrouble(true, true)
monkeyTrouble(false, false)
monkeyTrouble(true, false)
monkeyTrouble(false,true)

// PROBLEM 3: STRING TIMES
//
// Given a string and a non-negative int n, return a larger
// string that is n copies of the original string.
//
// Example input and output:
//
// stringTimes("Hi", 2) → "HiHi"
// stringTimes("Hi", 3) → "HiHiHi"
// stringTimes("Hi", 1) → "Hi"
function stringTimes(str, n){
    let longString = ''
    for(let i=0; i<n; i++){
       longString += str
    }
    console.log(longString)
}
console.log(' ')
console.log('PROBLEM 3: STRING TIMES: solutions')
stringTimes('Hi', 2)
stringTimes('Hi', 3)
stringTimes('Hi', 1)

// PROBLEM 4: LUCKY SUM

// Given 3 numerical values, a b c, return their sum. However, if one of the values is
// 13 then it does not count towards the sum and values to its right do not count.
// So for example, if b is 13, then both b and c do not count.
//
// Hint (Explore using multiple return statements inside a single function!)
//
// Example input and output
//
// luckySum(1, 2, 3) → 6
// luckySum(1, 2, 13) → 3
// luckySum(1, 13, 3) → 1
function luckyNum(a, b, c){
    let luckySum = 0;
    const luckyList = [a, b, c];
    for(i of luckyList){
        if (i === 13){
            break;
        }
        luckySum += i
    }
    console.log(luckySum)
}

console.log(' ')
console.log('PROBLEM 4: LUCKY SUM: solutions')
luckyNum(1, 2, 3)
luckyNum(1, 2, 13)
luckyNum(1, 13, 3)

// PROBLEM 5:
//
// You are driving a little too fast, and a police officer stops you. Write code to
// compute the result, encoded as an int value: 0=no ticket, 1=small ticket,
// 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
// and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
// Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
//
// Here are some example inputs and outputs:
//
// caught_speeding(60, false) → 0
// caught_speeding(65, false) → 1
// caught_speeding(65, true) → 0
function cuaghtSpeeding(speed, birthday){
    if(birthday){
        speed -= 5
}   
    if(speed <= 60){
    console.log(0)
}   else if(speed > 60 && speed <= 80){
    console.log(1)
}   else if(speed > 81) { // This could also be just an else statement
    console.log(2)
}
}

console.log(' ')
console.log('PROBLEM 5: Caught Speeding')
cuaghtSpeeding(60, false)
cuaghtSpeeding(65, false)
cuaghtSpeeding(65, true)
cuaghtSpeeding(85, false)

// BONUS: MAKE BRICKS
//
// We want to make a row of bricks that is goal inches long. We have a number of
// small bricks (1 inch each) and big bricks (5 inches each). Return true if it
// is possible to make the goal by choosing from the given bricks. This is a
// little harder than it looks and can be done without any loops in a single line!
//
// If you can't figue this one out, don't worry, that's why its a bonus!
//
// makeBricks(3, 1, 8) → true
// makeBricks(3, 1, 9) → false
// makeBricks(3, 2, 10) → true
function makeBricks(smallBricks, bigBricks, goal){
    if(smallBricks >= goal){
        console.log(true)
    } else if(goal%5 == 0 && bigBricks >= goal/5){
        console.log(true)
    } else if(smallBricks >= goal - bigBricks*5) {
        console.log(true)
    } else {
        console.log(false)
    }
}

console.log(' ')
console.log('BONUS: Make Bricks results')
makeBricks(3, 1, 8)
makeBricks(3, 1, 9)
makeBricks(3, 2, 10)
