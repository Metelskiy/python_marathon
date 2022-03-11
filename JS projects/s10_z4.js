function factorial(n) {
    var result = 1;
    while(n){
        result *= n--;
    }
    return result;
}

function processArray(arr, factorial) {
    const arr2=[]
    for(i=0;i<arr.length;i++){
        arr2.push(factorial(arr[i]))
    }
    return arr2
}
let a=4
console.log(factorial(a))
console.log(processArray([1, 2, 3, 4, 5], factorial))
