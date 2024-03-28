document.getElementById("rollButton").onclick = function(){
    let lottoNums = new Set();
    const size = 6;

    while(lottoNums.size < size){
         num = Math.floor(Math.random() * 10) + 1;
            lottoNums.add(num);
    }
    
    const numArr = Array.from(lottoNums);
    for(let i = 0; i < size; i++){
        document.getElementById(`num${i+1}`).innerHTML = numArr[i];
    }

}