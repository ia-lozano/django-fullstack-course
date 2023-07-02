// There are three types of for loops in JS:
// For - loops through a number of times
// For/In - loops through a JS object
// For/of - used with arrays



// Printing only even numbers
for (i=1; i <= 10; i++){
    if (i%2 == 0){
        console.log(i)
    }
}

// We can also iterate through strings
let word = 'Dichlorodifluoromethane'

for (let i=0; i < word.length; i++){
    console.log(word[i])
}
console.log(word + ' is ' + word.length + ' characters long.')