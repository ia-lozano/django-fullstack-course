// The DOM allow you to use JS to manipulate what the user sees in the front end,
// it connects JS to HTML and CSS.

// We can actually see the DOM of any website. To do so, go to your browser and open 
// the dev tools or inspect any element, then:

// 1. Type "document" and you'll get the html of the website
// 2. Type the command console.dir(document)
// 3. You get the DOM of the site

// For more info please refer to HTML DOM Documents

// To see the following commands, go to your browser and open the console in the 
// html file linked to this script
console.log('Printing the website URL:')
console.log(document.URL)

console.log('Getting all the elements with the #pickme Id')
console.log(document.getElementById('pickme'))

console.log('Getting ul elements by .class name')
console.log(document.getElementsByClassName('myul'))

console.log('Getting all the li elements by tag')
console.log(document.getElementsByTagName('li'))

// about the querySelector() methods, you have to pass the argument with its CSS selector tag
console.log('Using the querySelector methods')
console.log(document.querySelector('#pickme'))
console.log(document.querySelectorAll('.myul'))


// Now.. How to grab an element and actually make changes??????
// Fear not, first we write a function, to do somenthing, this time is a random color picker
// it generates random hex codes
function getRandomColor(){
    var letters = '0123456789ABCDEF'
    var color = '#'
    for (var i=0; i<6; i++){
        color += letters[Math.floor(Math.random()*16)];
    }
    return color
}

// Using the Random Color generator to change the h1 tag color
function changeHeaderColor(){
    var header = document.getElementById('header');
    var colorInput = getRandomColor()
    header.style.color = colorInput;
}

// setting an interval of time (miliseconds), where the function changeHeaderColor() is going to be called
setInterval('changeHeaderColor()', 500);
