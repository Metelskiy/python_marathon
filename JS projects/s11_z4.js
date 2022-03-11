const sumOfLen = (...args) => {
    res=0
    for(i=0;i<args.length;i++){
        res+=args[i].length
    }
    return res
}

console.log(sumOfLen('hello', 'hi')); //7
console.log(sumOfLen('hi')); //2
console.log(sumOfLen()); //0
console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16