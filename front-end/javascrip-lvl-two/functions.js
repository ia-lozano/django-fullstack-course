// Functions are the main building blocks of almost any programming languaje
// Let's start with the most basic function:
function HelloWorld(){
    console.log('Hello World!');
}

HelloWorld();

// A function with a paprameters:
function Hello(name){
    console.log('Hello ' + name);
}

Hello('Mr. Krabs');

// We can also use default parameters:
function addNumbers(a, b=5){
    console.log(a + b);
}

addNumbers(5); // Be aware of the position of the paremeter with a default value

// The return Key word, is used to return a value instead of just printing it to the console
function product(brand, item){
    return brand + item;
}

productInfo = product('Intel ', 'processor'); // this line will not print nothing by itself
console.log(productInfo);

// Arrow functions simmplify your code:
// 1. Remove the word "function"
// 2. Remove the body braces
// 3. Remove the parameter parentheses (if there's only one argument)
// 4. Asign the arrow function to a variable

let arrowFunct = a => a + 100;

console.log(arrowFunct(1));

// Function scope
// A variable defined inside of a funcion can only be called inside that function 
// (because it's a local variable)

function timesFive(number) {
    // local scope to the function
    var result = number*5;
    return result;
}

console.log(timesFive(5));
// console.log(result); // This line is going to throw a ReferenceError

// What about global scoppe???
var v = 'Gobal variable';
var stuff = 'Global stuff';

function fun(stuff){
    console.log(v)
    return stuff = 'Reassigned stuff inside func'
    console.log(stuff)
}

// Variable "stuff" is going to be changed only into the function scope
console.log(fun(stuff))
// If we print "stuff" outside the function it is going to have its global value
console.log(stuff)

