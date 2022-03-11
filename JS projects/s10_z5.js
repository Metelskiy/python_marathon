function checkAdult(age=0){
    let sendMessage=function(){console.log("Error"),console.log("Access denied - you are too young!")}
    let hasntSet = function(){console.log("Please, enter your age")}
    let negative = function(){console.log("Please, enter positive number")}
    let nonNumeric = function(){console.log("Please, enter number")}
    let notInt = function(){console.log("Please, enter Integer number")}
    if(age==0){
        throw hasntSet()}
    else if(age<0){
        negative()
    }
    else if(typeof(age)!=="number"){
        nonNumeric()
    }
    else if(Number.isInteger(age)==false){
        notInt()
    }
    console.log("Age verification complete")

}
let a=224

checkAdult()