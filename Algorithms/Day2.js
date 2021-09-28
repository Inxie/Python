// Use the parensValid(str) function below to receive a string with any number of parenthesis in it
// Return true if the parenthesis are valid and false if they are not
// We are looking to see if the opening and closing parenthesis match up correctly or not

// Example 1:"y(3(p)p(3)r)s" returns true
// Example 2: "n(0(p)3" returns false
// Example 3: "n)0(t(o)k" returns false
// Example 4: "((()))" returns true
// Example 5: "()())(" returns false
// Example 6: "hello!" returns true (there are no parenthesis to be invalid)

// HINTS: You can loop through a string!
// Consider using a counter or an array or object to track your parenthesis
// Start out simple like "())" or "(())", work through it mentally, and then work out from there
// Every single opening parenthesis has a closing one as well
// A closing parenthesis should never appear before an opening parenthesis
// We can ignore everything in the string except the parenthesis

// our incorrect/incomplete logic below

function parensValid(str) {
    var open_paren_count = 0;
    var close_paren_count = 0;
    for (i=0; i<str.length; i++) {
        if (str[i] == "(") {
            open_paren_count++;
        }
        if (str[i] == ")") {
            close_paren_count++;
        }
    }
    for (j=0; j<str.length; j++) {
        if (str[i] == "(" && i < j) {
            return false;
        }
    }
    
    if (open_paren_count == close_paren_count) {
        return true;
    }
    else {
        return false;
    }
}

console.log(parensValid("y(3(p)p(3)r)s"));
console.log(parensValid("n(0(p)3"));
console.log(parensValid("n)0(t(o)k"));
console.log(parensValid("((()))"));
console.log(parensValid("())("));
console.log(parensValid("hello!"));


// a different group's completed logic below

function parensValid(str) {
    // your code here
    var count = 0
    for(var i = 0; i < str.length; i++){
        if(str[i] == "("){
            count = count + 1
        }
        else if(str[i] == ")"){
            count = count - 1
        }
        if(count == -1){
            return false
        }
    }
    if(count == 0){
        return true
    }
    else if(count >= 1){
        return false
    }
}

console.log(parensValid("y(3(p)p(3)r)s"));
console.log(parensValid("n(0(p)3"));
console.log(parensValid("n)0(t(o)k"));
console.log(parensValid("((()))"));
console.log(parensValid("()())("));
console.log(parensValid("hello!"));


// Use the bracesValid function below to receive a string with any number of parenthesis, 
//    square brackets, and curly brackets in it
// Return true if the parenthesis, square brackets, and curly brackets line up and return false if they don't 

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true

// HINTS: Same hints as the parensValid function, except now we have to check for three kinds of characters

// didn't get to this; unfinished

function bracesValid(str) {
    // your code here
}

console.log(bracesValid("({[({})]})"))
console.log(bracesValid("d(i{a}l[t]o)n{e!"))
console.log(bracesValid("{{[a]}}(){bcd}{()}"))