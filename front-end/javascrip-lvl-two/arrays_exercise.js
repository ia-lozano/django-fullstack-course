// initializing the class roster and the roster itself with an empty array
let init = prompt('Would you like to start the Roster Manager App? (y/n) ');
let roster = [];

// starting the app if the user typed 'y'
if(init == 'y'){
    // Infinite Loop, which prompts the user until they enter 'quit'
    while(true){
        let action = prompt('What would you like to do? (add, remove, display or quit)')
        // Adding a new student at the last position of the roster array
        if(action == 'add'){
            let newName = prompt('Enter new student name: ', 'John Doe');
            roster.push(newName)
        } 
        // Removing a student from the roster
        else if(action == 'remove'){
            // 1. Storing the name entered by the user in the variable "removed"
            let removed = prompt('Enter the name to remove: ');
            // 2. Obtaining the index by its value
            let index = roster.indexOf(removed)
            // 3. Removing the selected index (splice function takes 2 arguments:
            //    (first position to remove, last position to remove))
            // In this case we just want to remove the selected index
            roster.splice(index, index);
        } 
        // Displaying the roster with an alert and printing it to the console
        else if(action == 'display'){
            alert(roster)
            console.log(roster)
        } 
        // Stoping the infinite loop with the break statement
        else if(action == 'quit'){
            break;
        } 
        // If the user enters an invalid command, the app does nothing and the loop starts again
        else(alert('Invalid command!'))
    }
} 
// If the user quits, they must refresh the page to start the app again
else(alert('Please refresh the page to start over.'))