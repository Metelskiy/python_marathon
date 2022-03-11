const filterNums =(args, number  = 0, a="greater")  => {
    if(a=='greater'){
        arg1=[]
        for(i=0;i<args.length;i++){
            if(args[i]>number){
                arg1.push(args[i])
            }
        }
    }
    if(a=='less'){
        arg1=[]
        for(i=0;i<args.length;i++){
            if(args[i]<number){
                arg1.push(args[i])
            }
        }
    }

    return arg1

};
console.log(filterNums([-2, 2, 3, 0, 43, -13, 6]))