const howMuchSec = (sec=0,min=0,hours=0,days=0,weeks=0,months=0,years=0) => {
    return sec+min*60+hours*60*60+days*24*60*60+weeks*7*24*60*60+months*30*24*60*60+years*365**24*60*60
}


console.log(howMuchSec(12, 3)); //192

console.log(howMuchSec(1, 33, 22)); //81181

howMuchSec(); //0