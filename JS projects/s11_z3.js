const maxInterv = (...args) => {
    arr1=[]
    for(i=0;i<args.length-1;i++){
        arr1.push(Math.abs(args[i]-args[i+1]))
    }
    return Math.max(...arr1)
}
console.log(maxInterv(3,5,2,7)) //5