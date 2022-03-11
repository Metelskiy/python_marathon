function a(hum){
    const humlen = hum.length;
    for(let i=0;i<humlen;i++){
        if(hum[i].position==='astrounaut'){
            break
        }
    }

console.log('Astrounaut if in ${i} index')
return i;
}
console.log(a())