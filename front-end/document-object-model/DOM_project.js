// Grabbing all the td tags
// REMEMBER that querySelectorAll() returns an array with all the elements given as an argument
// the variable squares, is going to return: squares = [td, td, ..., td]
var squares = document.querySelectorAll("td");

// This function uses the "this" keyword, it is a called a handler function by the way.
// We can replace this function by adding an #id to all the <td> tags and repeat this function
// for eacha #id... eww
function changeMarker(){
    if (this.textContent === ''){
        this.textContent = 'X';
    } else if (this.textContent === 'X'){
        this.textContent = 'O';
    } else {
        this.textContent = '';
    }
}

// Iterating through all the td tags (remember... squares = [td, td, ..., td])
// NOTE that changeMarker is being passed as an event handler, not as a function itself
for(let i=0; i < squares.length; i++){
    squares[i].addEventListener('click', changeMarker)
}

// Adding functionality to the button
// first we grab it
let restart = document.querySelector('#b');

// Creating a function to delete all the squares
restart.addEventListener('click', () => {
    for(let j=0; j<squares.length; j++){
        squares[j].textContent = '';
    }
})
