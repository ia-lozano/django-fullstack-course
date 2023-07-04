// Grabbing the <p> tag of  the html
var p = document.querySelector(`p`);
console.log(p)

// Changing the content of the <p> tag
// p.textContent = 'content changed'

// use var.innerHTML to pass html tags
// p.innerHTML = "<b>I'm bold</b>"

// let's grab the first item with the #special id
var special = document.querySelector('#special');
console.log(special)

// Grabbing the first anchor tag of the html document
var specialA = document.querySelector('a');
console.log(specialA)

// Then we change the attribute of the anchor tag, it takes you to facebook.com
// let's change it
//specialA.setAttribute('href', 'https://www.amazon.com.mx/') // setAttribute(attr name, attr value)
