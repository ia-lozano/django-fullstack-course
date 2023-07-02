// Just a normal while loop:
// x starts in 0, and each time it iterates through x, the while statement adds 1 to x
// the loop continues until x reaches 5.

let x = 0;


while (x < 5){
    console.log('X is currently ' + x);
    console.log('X is still less than 5, adding +1 to X...');
    console.log('-----------')
    x++;
}

console.log('Done X is already equal to 5')
// This is just a separation
console.log('*********************************************************')
console.log('   ')

// It is possible to interrupt a while statement with the keyword 'break', lets see...
let y = 0;
let counter = 0;

while (y < 10){
    console.log('Y is currently ' + y);
    console.log('Y is still currently less than 10, adding +1 to Y....');
    console.log('-----------');
    y++;

    if (y == 7) {
        console.log('Almost there........');
        console.log('-----------');
        y--;
        counter++;
    }

    if(counter > 3) {
        console.log('Wait... something went wrong... finishing the loop with the break statement...')
        break;
    }
}
console.log('*********************************************************');
console.log('   ');

// Showing only even numbers
let num = 1;

console.log('Printing only even numbers from 0 to 16:')
while (num <= 16) {
    if (num%2 == 0) {
        console.log(num);
    }
    ++num;
}