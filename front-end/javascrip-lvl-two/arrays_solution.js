// initializing roster
let roster = [];

// CREATING FUNCTIONS FOR THE TASKS

// Add student
let addNew = () => {
    var newName = prompt('What name would you like to add?')
    roster.push(newName)
}

// Remove student
let remove = () => {
    var rmName = prompt('What name would you like to remove?')
    var index = roster.indexOf(rmName)
    roster.splice(index, 1) // (index to remove, how many elements from there)
}

// Display roster
let display = () => {
    console.log(roster)
}

// STARTING THE APP LOGIC

let start = prompt('Would you like to start the roster web app? y/n')
let request = '';

if(start === 'y'){
    while(request !== 'quit'){
        request = prompt('Please select an action: add, remove, display, or quit.')
        if(request === 'add'){
            addNew()
        } else if(request === 'display'){
            display()
        } else if(request === 'remove'){
            remove()
        } else {
            alert('Closing roster web app...')
            request = 'quit'
        }
    }
}
alert('Thanks for using the web app, please refresh to start over')
