// Problem #1
// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While loop
console.log ('Problem 1:');
console.log(' ');

let i = 0;
while (i < 5){
    console.log('Hello');
    ++i;
}
console.log('###############################################')
// For loop
for (let j=0; j < 5; j++){
    console.log('Hello');
}

console.log(' ');
console.log ('Problem 2:');
console.log(' ');

// Use Loops to console.log() (print out) all the even numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// While Loop
let a = 1;
while(a < 25){
    if(a%2 == 0){
        console.log(a);
    }
    a++;
}

console.log('###############################################');

// For loop
for(let b=1;b < 25; b++){
    if(b%2 == 0){
        console.log(b);
    }
}