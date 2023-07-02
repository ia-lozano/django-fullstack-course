/* 
For this project you will be building a generic website that will seem to ask mundane questions to normal users, but you secretly are looking for a spy! Anyone visiting your website will be asked a series of questions, only the Spy will be able to give specific answers you expect. If all questions are answered correctly, you will post a secret message in console for the Spy to read!

Here are the four conditions you will check for the spy:

The Spy has the same first letter of her First Name and Last Name
The Spy is between the Age of 20 and 30 (exclusive of 20 and 30)
The Spy is at least 170 centimeters tall.
The Spy has a pet name that ends with the letter "y".
*/

/* This was my solution, which actually worked , but theres a cooler way to do it...

let fname = prompt('Enter your name: ', 'John');
let lname = prompt('Enter your last name: ', 'Doe');
let age = prompt('What is your age again? ', 23);
let height = prompt('How tall are you (in cm) ', 0);
let  pet = prompt('What is the name of your pet? ', 'tina-chan');
alert('Okay... Thank you.')

if (fname[0] === lname[0] && 20 < age < 30 && height >= 170 && pet.charAt(pet.length -1) === 'y'){
    console.log('Welcome comrade, you have passed the spy test.')
} else{
    console.log('Uhhh.... nothing to see here, he he he.')
} 
*/

// Prompts for the user
var firstName = prompt('First Name Please: ');
var lastName = prompt('Last Name Please: ');
var age = prompt('How old are you? ');
var height = prompt('What is your height? ');
var petName = prompt('What is your pet name? ');
alert('Thank you so much for the info!!');

// Four conditions
var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;

// Name condition
if(firstName[0] === lastName[0]){
    nameCond = true;
} else{nameCond = false}

// Age condition
if(age > 20 && age < 30){
    ageCond = true;
} else{ageCond = false}

// Height condition
if(height >= 170){
    heightCond = true;
} else{heightCond = false}

// Pet name condition
if(petName[petName.length -1] === 'y'){
    petCond = true;
} else{petCond = false}

// Console log message
if(nameCond && ageCond && heightCond && petCond){
    console.log('Welcome comrade!')
} else{console.log('Nothing to see here...')}