//If statement
// We're going to simulate some sort of temperature control
// If the temperature is equal to or less than 60 (arbitrary units)
// the temperature is going to be not considered as hot
// otherwise, the temperature is going to be hot.

let hot = false;
let T = 61;

if(T > 60) {
    hot = true;
}

if(hot) {
    console.log('OMG! this is hot!!!')
} else {
    console.log('hmm... cold...')
}

// Now we're going to simulate a kind of exterior temperature monitor

let extTemp = 35;

if (extTemp > 35) {
    console.log('Hot outside');
} else if (extTemp <= 35 && extTemp >= 30) {
    console.log('Not so hot outside')
} else if (extTemp < 30 && extTemp >= 25) {
    console.log('Temperature is perfect')
} else if (extTemp < 25 && extTemp >= 20) {
    console.log('Kinda cold...')
} else {
    console.log('Cold outside')
}