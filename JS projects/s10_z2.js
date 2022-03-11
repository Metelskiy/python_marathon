function combineArray(arr1, arr2) {
    for (i=0;i<arr2.length;i++){
        if(typeof(arr2[i])!=="number"){
            arr2.splice(i,1)
            i--
        }
    }
    for (i=0;i<arr1.length; i++){
        if(typeof(arr1[i])!=="number"){
            arr1.splice(i,1)
            i--
        }
    }
    const arr3=arr1.concat(arr2)
    return arr3
}

const a = ["User01", "User02", "User03", "User04"]
const b = ["Data1", 33, "Data2", 44]
console.log(combineArray(a,b))
console.log("-----------------------------------------------------")
const c = ['1', '2', '3', '4' ]
const d = ['first', 'second', 'third']
console.log(combineArray(c,d))