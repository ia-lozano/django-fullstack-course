// Listening for an event looks like this:
// myvar.addEventListener(event, func);
// for more info please refer to JavaScript event listeners


// defining variables
let headOne = document.querySelector('#one');
let headTwo = document.querySelector('#two');
let headThree = document.querySelector('#three');

// Writing listeners


headOne.addEventListener('mouseover', () => {
    headOne.textContent = 'Mouse Currently Over';
    headOne.style.color = 'red'
})
headOne.addEventListener('mouseout', () => {
    headOne.textContent = 'HOVER OVER ME';
    headOne.style.color = 'black'
})

headTwo.addEventListener('click', () => {
    headTwo.textContent = 'Clicked on!';
    headTwo.style.color = 'aqua'
})

headThree.addEventListener('dblclick', () =>{
    headThree.textContent = 'Double Clicked!';
    headThree.style.color = 'green'
})