// Adding an event to the h1 elements
// For more info please refer to jQuery Events

$('h1').click(() => {console.log('h1 clicked!')})

$('li').click(() => {console.log('Any li clicked!')})

// To change an attribute or property, use the this keyword. 
// NOTE that you shouldn't use an arrow function with the this keyword
$('h2').click(function(){
    $(this).text('text was changed')})

// We can perform actions with a KEY PRESS too
$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue')
})

// it is possible to console log an event object, for example
// Here we're going to console.log an event for a keypress, then we're going to
// search info in the 'which' property in the console, 'which' displays the ASCII value
// of the key being pressed
$('input').eq(0).keypress(function(){
    console.log(event);
    if(event.which === 13) {
        $('h3').toggleClass('turnBlue')
    }
})

// On your own:
// Write code to change the h2 element turn red and then white again 
// every time you double click on it:
$('h2').on('dblclick', function(){
    console.log('h2 was double clicked !');
    $(this).toggleClass('turnRed');
})

// This even makes the first paragraph in the html change when you pass the mouse
// over it
$('p').eq(0).on('mouseenter', function(){
    console.log('cursor where over the paragraph!');
    $(this).toggleClass('turnBlue')
})


// You can put animations in your website
// This event makes everything fade when you push the button
$('input').eq(1).on('click', function(){
    $('.container').fadeOut(3000);
})