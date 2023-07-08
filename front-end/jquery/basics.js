// Let's change some styles by using jQuery
// First we define a variable to grab the h1 (or any other element)
let headerOne = $('h1');
console.log(headerOne)

// Then we create a javascript object containing styles
let newCSS = {
    'color': 'white',
    'background': 'gray',
    'border': '20px solid black'
}

// Then we call the .css method from jQuery
// NOTE that we could also pass in the form .css('background', 'gray', ...)
headerOne.css(newCSS)


// Let's grab multiple elements
var listItems = $('li');
console.log(listItems)

// Here we change the color of all the li item to blue
listItems.css('color', 'blue')

// And then, we select the first and the last item and change only that specific item
listItems.eq(0).css('color', 'orange')
listItems.eq(-1).css('color', 'green')

// To modify an element, use .text()
$('h1').text('BRAND NEW TEXT')

// And if you want to pass a html tag, use .html()
$('p').html('<b>this text was changed to bold</b>')

// Now let's play with the inputs
$('input').eq(1).attr('type', 'checkbox')
$('input').eq(0).val('New Value')

// About the CSS styles we added in the html file, we can add them to an element
$('h2').addClass('turnRed')
// We can also remove it
// $('h2').removeClass('turnRed')

// We can toggle a class to add and remove class
$('h3').toggleClass('turnBlue')
// Then we use toggle again to remove the class
// $('h3').toggleClass('turnBlue')