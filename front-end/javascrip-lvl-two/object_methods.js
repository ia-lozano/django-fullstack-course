// We can put functions inside of an object and call them later as methods
// NOTE and PLEASE: AVOID ARROW FUNCTIONS
let simpleObj = {
    prop: 'property',
    simpleMethod: function() {return'simpleMethod was called'},
    anotherMethod: function() {return 'prop stands for ' + this.prop}
}

// If we print the object to the console, it will not show the function
console.log(simpleObj)

// Of we call the object and its method with dot notation, the console will report the actual function
console.log(simpleObj.simpleMethod)

// To call the method we have to use ()
console.log(simpleObj.simpleMethod())

// A method can use a property of the object, for that we use the keyword "this" 
// (see the anotherMethod in the object)
console.log(simpleObj.anotherMethod())

