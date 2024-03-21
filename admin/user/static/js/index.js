

let x;
let y;
let z;
let o;
let i;
let p;

document.getElementById("rollButton").onclick = function(){

     x = Math.floor(Math.random() * 49) + 1;
     y = Math.floor(Math.random() * 49) + 1;
     z = Math.floor(Math.random() * 49) + 1;
     o = Math.floor(Math.random() * 49) + 1;
     i = Math.floor(Math.random() * 49) + 1;
     p = Math.floor(Math.random() * 49) + 1;


     document.getElementById("xlable").innerHTML = x
     document.getElementById("ylable").innerHTML = y
     document.getElementById("zlable").innerHTML = z
     document.getElementById("olable").innerHTML = o
     document.getElementById("ilable").innerHTML = i
     document.getElementById("plable").innerHTML = p
     
}