// Arrays allow us to store various types of data and access them as
// needed. Arrays might prevent us from using an unnecesary number of variables

let countries = ['USA', 'China', 'Germany']
// accessing to an element of the countries array
console.log(countries[1])

// arrays are mutable
countries[1] = 'Spain'
console.log(countries[1])

// for instance, strings are immutable
country = countries[0]
console.log(country)

// here we print the last element of the string "country"
console.log(country[2])
// then we try to modify the last element
country[2] = 'B'
// and we see that in didn't do anythin, because strings are immutable
console.log(country)

// An array can also store mixed data
let mixed = [true, 20, 'text', country]
console.log(mixed)

// Here are some methods for arrays
console.log(mixed.length)

// Removing and adding elements
let lasOne = mixed.pop() // removing last element
console.log(lasOne)
console.log(mixed)

let newOne = mixed.push('newOne') // adding an element at the end of the array
console.log(newOne)
console.log(mixed)

let firstOne = mixed.shift() // removing the first element
console.log(firstOne)
console.log(mixed)

let newFirstOne = mixed.unshift('new1stOne') // adding an element to the beggining of the array
console.log(newFirstOne)
console.log(mixed)

// It is possible to nest multiple arrays to make a matrix
let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
console.log(matrix + ' Matrix length: ' + matrix.length)

// Array iteration
arr = ['a', 'b', 'c', 'd']
// with a normal for loop:
for(let i=0; i < arr.length; i++){
    console.log(arr[i])
}

// with an array specific for loop:
// NOTE the "in" keyword used to iterate through an array (i is an arbitrary name)
for(i in arr){
    console.log(arr[i])
}

// You can iterate with the .forEach method 
['alpha', 'beta', 'gama'].forEach(i => console.log(i)) // note that we can use a variable or an array itself

// another example of .forEach
let topics = ['JavaScript', 'C++', 'Python', 'SQL'];
let addAwesome = topic => console.log(topic + ' is awesome!');
topics.forEach(addAwesome)

// we can store the modified strings into another array by using the .map function
let topics2 = ['JavaScript', 'C++', 'Python', 'SQL'];
let addAwesome2 = topic => topic + ' is awesome!';
let modifiedTopics = topics.map(addAwesome2);
console.log(modifiedTopics);