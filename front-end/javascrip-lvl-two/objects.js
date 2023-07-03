// The typical JS object looks like a Python dictionary
// object = {key1: value1, ..., key_n: value_n}
// You access values through the corresponding key.
// Unlike arrays, JS objects do not retain any ordering

// Let's create a car Object

let carInfo = {
    make: 'Toyota',
    year: 1990,
    model: 'Camry'
};

console.log(carInfo)

// Accessing only a value
// NOTE that we're using a string, but the original key is not a string, this is by convention
console.log(carInfo['make'])

// Like arrays, you can store anything into the object
let newObject = {
    a: 'string',
    b: [1, 2, 3],
    c: {inside: ['a', 'b']}
};

// We can access a specific element of the array with the 'b' value by nesting the call
console.log(newObject['b'][1])

// For a nested object the nested call works this way:
// Call the value by it's key, then call the key of that object value, and finally call the position
console.log(newObject['c']['inside'][1])

// Taking back the carInfo Object...
// It is posible to change or perform operations on the values
carInfo['year'] = 2006
carInfo['year'] += 1
console.log(carInfo['year'])

// To iterate through an object use the for/in loop
for(key in carInfo){
    console.log(key)
}

// By default, for/in loop grabs the keys, we can use the key to grab de actual value
for(key in carInfo){
    console.log(carInfo[key])
}