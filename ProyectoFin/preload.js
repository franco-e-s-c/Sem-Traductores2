const { contextBridge, ipcMain, ipcRenderer } = require('electron')

function enviarIte(seleccion, ganancia, perdida, total){
  ipcRenderer.send("enviarIte", seleccion, ganancia, perdida, total);
}

function cargarJuego(){
  ipcRenderer.send("cargarJuego")
}

function guardarParticipante(configuracion){
  resp = ipcRenderer.send("guardarParticipante", configuracion)
}

function guardarExp(){
  ipcRenderer.send("guardarExp")
}


let indexBridge = {
  enviarIte: enviarIte,
  cargarJuego: cargarJuego,
  cargarC: (callback) => ipcRenderer.on("cargarC", (callback)),
  guardarParticipante: guardarParticipante,
  guardarExp: guardarExp,
  result: (callback) => ipcRenderer.on("result", (callback))
}

contextBridge.exposeInMainWorld("Bridge", indexBridge);

window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) element.innerText = text
  }

  for (const type of ['chrome', 'node', 'electron']) {
    replaceText(`${type}-version`, process.versions[type])
  }
})

