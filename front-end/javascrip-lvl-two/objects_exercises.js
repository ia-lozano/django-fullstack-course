// PROBLEM 1
// Given the object:
var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    nameLength: function(){return this.name.length},
    lastName: function(){
        let nameArr = this.name.split(' ');
        let lName = nameArr[1]
        return lName
    }
  }

// Add a method called nameLength that prints out the
// length of the employees name to the console.
console.log(employee.nameLength())

// PROBLEM 2
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert

// I didn't want to make an .html file for this, so i will just console.log() this part
// just change console.log() by alert() and link this script to an .html file
for(k in employee){
    console.log(employee[k])
}

// PROBLEM 3
// Add a method called lastName that prints
// out the employee's last name to the console.

// Okay, for this we need to split() the name string
// (see the object employee above)
console.log(employee.lastName())