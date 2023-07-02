// Comparison operators
// These operators usually return a boolean

// Greater than, Less than
console.log(3 > 2);
console.log(3 < 2);
console.log('--------------');

// Greater than or equal to, Less than or equal to
console.log(5 >= 2);
console.log(5 <= 2);
console.log('--------------');

//Equality, inequality
console.log(2 == 2);
console.log('2' == 2);
console.log(8 != 2);
console.log('--------------');

//Strict equality, inequality (both elements must be of the same type)
console.log(5 === '5');
console.log(1 !== '1');
console.log('--------------');

//null, undefined, and NaN might behave not as spected
console.log(null == undefined);
console.log(NaN == NaN);
console.log(NaN === NaN);
console.log('--------------');


//Logical operators
// They're AND(&&) or OR(||)
// False && True = False
// True && True == True
// True || False == True
// True || True == True

console.log(1 === '1' && 2 > 1);
console.log(2 == 5 || '5' === '5');