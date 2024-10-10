function isBalanced(str, openBrackets = '({[', openBracArrTracker = []) {
   if (str.length === 0) { // Base case if string is empty
    return openBracArrTracker.length === 0; //balanced only if no unclosed brackets
   }
   
   const firstChar = str[0];

   // if first character is an opening bracket, add to []tracker and check rest of string.
   if (openBrackets.includes(firstChar)) {
    return isBalanced(str.slice(1), openBrackets, [...openBracArrTracker, firstChar]); 
   }

   // if first character is a closing bracket, check if it matches last opening bracket
   if (')}]'.includes(firstChar)) {
    const lastOpenBracket = openBracArrTracker[openBracArrTracker.length - 1];
    if ((firstChar === ')' && lastOpenBracket === '(') ||
        (firstChar === '}' && lastOpenBracket === '{') ||
        (firstChar === ']' && lastOpenBracket === '[')) {
            // if it matches, remove last opening bracket and continue
            return isBalanced(str.slice(1), openBrackets, openBracArrTracker.slice(0, -1));
        } else {
            return false; // if it does not match, string is imbalanced
        }   
    }

    return isBalanced(str.slice(1), openBrackets, openBracArrTracker);
}


console.log(isBalanced("hello"));        // true (no brackets)
console.log(isBalanced("(hi) [there]")); // true
console.log(isBalanced("(hi [there])")); // true
console.log(isBalanced("(((hi)))"));     // true
console.log(isBalanced("(hello"));       // false (unmatched '(')
console.log(isBalanced("(nope]"));       // false (mismatched brackets)
console.log(isBalanced("((ok) [nope)]")); // false (wrong order)