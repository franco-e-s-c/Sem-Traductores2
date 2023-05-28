let startTime = new Date();
var A = 0
var B = 0
var C = 0
var D = 0
var I = 1
var cont = 0

let tiempoI
let seleccionesI
let mezcladoA = []
let mezcladoB = []
let mezcladoC = []
let mezcladoD = []
let bancoini
let bancoini2
let selecciones = 0
let seleccion
let ganancia
let perdida
let total


function onloadJuego(){
    window.Bridge.cargarJuego();
}

window.Bridge.cargarC((event, configuracion) => {
    mezcladoA = configuracion[8]
    mezcladoB = configuracion[9]
    mezcladoC = configuracion[10]
    mezcladoD = configuracion[11]
    seleccionesI = 100
    bancoini = 2000
    bancoini2 = bancoini
    document.getElementById("puntos").innerHTML = bancoini
})

function moverC(element, newId){
    element.classList.add("mover" + newId);
    element.classList.add("grandeC");
    const elements = document.body.getElementsByTagName('*')
    for (var i = 0; i<elements.length; i++){
        elements[i].classList.add('blur')
        if (elements[i].id == element.id){
            elements[i].classList.remove('blur')
        }
    }
    var carta = element.getElementsByTagName('*')
    for (var c = 0; c<carta.length; c++){
        carta[c].classList.remove('blur')
    }
    document.getElementById("fondo-d").classList.remove('blur')
    document.getElementById("score").classList.remove('blur')
    puntos = document.getElementById("score").getElementsByTagName('*');
    for (var p = 0; p<puntos.length; p++){
        puntos[p].classList.remove('blur')
    }

    setTimeout(()=>{
        animacion(element,newId);}, 800)
}

async function animacion(element,newId){
    countTo()
    element.classList.add("animation")
    setTimeout(() => {
        element.classList.add("sacar"+newId);
        setTimeout(() => {  
            vovler(element,newId);
            element.classList.add("none");}, 800);}, 2000)   
}

function vovler(element,newId){
    document.getElementById("oscurecer").classList.remove("oscurecer")
    document.getElementById("oscurecer").classList.add("aclarar")
    const elements = document.body.getElementsByTagName('*')
    const borrar = document.getElementById("fondo-d")
    borrar.innerHTML=""
    borrar.style.cssText = ""
    for (var i = 0; i<elements.length; i++){
        elements[i].classList.remove('blur')
    }
    window.Bridge.enviarIte(seleccion, ganancia, perdida, bancoini2);
    borrar.innerHTML = `<div class="flip-card" id="A">
    </div>
    <div class="flip-card" id="B">
    </div>
    <div class="flip-card" id="C">
    </div>
    <div class="flip-card" id="D">
    </div>`
}


function terminar(I){
        if(I==seleccionesI){
            setTimeout(() => {
                document.getElementById("over").classList.add("oscurecer")
            },3600) 
        }
    
}

function crear(element){
    terminar(I)
    document.getElementById("oscurecer").classList.remove("aclarar")
    document.getElementById("oscurecer").classList.add("oscurecer")
    fondo = document.getElementById("fondo-d")
    fondo.style.cssText = "z-index: 999; pointer-events: all;"
    id = element.id
    newId = id.replace('m','')
    I++
    if(id == "Am"){
        seleccion = 'A'
        ganancia = mezcladoA[A][0]
        perdida = mezcladoA[A][1]
        mazo="A" 
        A++
    }
    else if(id == "Bm"){
        seleccion = 'B'
        ganancia = mezcladoB[B][0]
        perdida = mezcladoB[B][1]
        mazo="B"
        B++ 
    }
    else if(id == "Cm"){
        seleccion = 'C'
        ganancia = mezcladoC[C][0]
        perdida = mezcladoC[C][1]
        mazo="C" 
        C++
    }
    else if(id == "Dm"){
        seleccion = 'D'
        ganancia = mezcladoD[D][0]
        perdida = mezcladoD[D][1]
        mazo="D"
        D++ 
    }
    codigo = `
        <div class="carta">
        <div class="carta-lomo">
            <img src="src/doodad.jpg" alt="" class="dorso">
        </div>
        <div class="carta-info">
        <ul>
            <li>
                <p class="carta-texto">Ganas: </p>
            </li>
            <li>
                <p class="carta-texto" id="win">+${ganancia}</p>
            </li>
            <li>    
                <p class="carta-texto">Pierdes: </p>
            </li>
            <li>
                <p class="carta-texto" id="loss">${perdida}</p>
            </li>
        </ul>
        </div>
        `
    document.getElementById(mazo).innerHTML=codigo;
    document.getElementById(mazo).innerHTML=codigo;
    newElement = document.getElementById(mazo)
    moverC(newElement, newId);
}

function countTo(){
    let from = parseInt(document.getElementById("puntos").innerHTML);
    let win = parseInt(document.getElementById("win").innerHTML)
    let loss = parseInt(document.getElementById("loss").innerHTML)
    total = ganancia+perdida
    bancoini2 = bancoini2+total
    let to = from+total
    let interval = 30;
    let step = total
    if (Math.abs(from-to) >=100){
        interval = 15
    }
    if (Math.abs(from-to) >=200){
        interval = 10
    }
    if (Math.abs(from-to) >=300){
        interval = 1
    }
    console.log("step", step)

    if(from == to){
        document.querySelector("#puntos").textContent = from;
        total = document.querySelector("#puntos").innerHTML
        console.log("ADSD", total)
        return;
    }

    let counter = setInterval(function(){
        from += step;
        document.querySelector("#puntos").textContent = from;
        total = document.querySelector("#puntos").innerHTML
        console.log("ADSD", total)

        if(from == to){
            clearInterval(counter);
        }
    }, interval);
}
