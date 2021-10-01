// Use the generateCoinChange function below to receive a dollar (decimal) amount with change. 
// Covert that value to the number of quarters, dimes, nickels, and pennies it would have.
// It should count the number or quarters first then work it's way down from there
// This can return a string or an object or whatever you'd like

// Example: generateCoinChange(.67) woud return 2 quarters, 1 dime, 1 nickel, 2 pennies
// Example: generateCoinChange(0.77) would return 3 quarters, 2 pennies
// Example: generateCoinChange(2.85) would return 11 quarters, 1 dime
// Example: generateCoinChange(4.57) would return 18 quarters, 1 nickel, 2 pennies


//unfinished code below - we were getting there!

function generateCoinChange(input) {
    var quarter = 0.25;
    var dime = 0.10;
    var nickel = 0.05;
    var penny = 0.01;
    var tempResult = "";

    if (input / quarter > 0) {
        console.log(Math.floor(input / quarter)); 
    }

    if (input % quarter != 0) {
        console.log(input % quarter);
    }

    if ((input % quarter) / dime > 0) {
        console.log(Math.floor((input % quarter) / dime))
    }

    if ((input % quarter) / dime != 0) {
        console.log((input % quarter) % dime);
    }
}

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57))