const { app, BrowserWindow, ipcMain, Menu, ipcMainEvent } = require('electron')
const path = require('path')
const { Pool } = require('pg');
const shuffleSeed = require('shuffle-seed');
const {PythonShell} = require('python-shell')
let id_participante
let id_juego
mazoAG = [100,100,100,100,100,100,100,100,100,100]
mazoAP = [0,0,0,0,0,-250,-250,-250,-250,-250]
mazoBG = [100,100,100,100,100,100,100,100,100,100]
mazoBP = [0,0,0,0,0,0,0,0,0,-1250]
mazoCG = [50,50,50,50,50,50,50,50,50,50]
mazoCP = [0,0,0,0,0,-50,-50,-50,-50,-50]
mazoDG = [50,50,50,50,50,50,50,50,50,50]
mazoDP = [0,0,0,0,0,0,0,0,0,-250]
aprendi = []
selecciones = 100
bancoini = 2000
nombre = 'prueba'
mezcladoA = shuffle(mazoAG,mazoAP, nombre, selecciones)
mezcladoB = shuffle(mazoBG,mazoBP, nombre, selecciones)
mezcladoC = shuffle(mazoCG,mazoCP, nombre, selecciones)
mezcladoD = shuffle(mazoDG,mazoDP, nombre, selecciones)
configuracion = [mazoAG, mazoAP,mazoBG, mazoBP,mazoCG, mazoCP,mazoDG, mazoDP,mezcladoA,mezcladoB,mezcladoC,mezcladoD,selecciones,bancoini] 

function createWindow () {
    mainWindow = new BrowserWindow({
    width: 1920,
    height: 1080,
    minWidth: 1280,
    minHeight: 720,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      devTools: true,
    }
  })
  mainWindow.loadFile('registro.html')
  mainWindow.menuBarVisible = false
  mainWindow.maximize()
  mainWindow.setAspectRatio(16/9)
  mainWindow.fullScreen = false
  
}

app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
function shuffle(mazoG, mazoP, nombre, dato){
  const merge = (first, second, third) => {
      for(let i=0; i<second.length; i++) {
        let pares = [];
        pares.push(first[i]);
        pares.push(second[i]);
        third.push(pares);
      }
      return third;
    }
  let obj = [];
  resultadoPares = merge(mazoG, mazoP, obj)
  //console.log(obj);
  const repeat = (arr, n) => [].concat(...Array(n).fill(arr));
  n = dato/10
  copia = repeat(resultadoPares, n)
  var resp = shuffleSeed.shuffle(copia,nombre);
  return resp
}

const credenciales = {
  user: "postgres",
  host: "localhost",
  database: "proyectoIATraductores",
  password: "admin"
}

const pool = new Pool(credenciales);

ipcMain.on("guardarParticipante", async(event, datos) =>{
  await guardarParticipanteDB(datos)
})

async function guardarParticipanteDB(datos){
  let query = await pool.query('INSERT INTO participante (nombre, edad, etiqueta) VALUES ($1, $2, $3)', [datos[0], datos[1], 'Pendiente'])
  query = await pool.query('SELECT id_participante FROM participante WHERE nombre = $1 AND edad = $2', [datos[0], datos[1]]) 
  res = query.rows[0]
  id_participante = res.id_participante 
  query = await pool.query('INSERT INTO juego (id_participante, fecha) VALUES ($1, NOW())', [id_participante])
  query = await pool.query('SELECT id_juego FROM juego WHERE id_participante = $1', [id_participante]) 
  res = query.rows[0]
  id_juego = res.id_juego 
}

async function getIte(id_exp){
  const query = await pool.query('SELECT iteracion FROM resultado  WHERE id_juego = $1 ORDER BY iteracion DESC LIMIT 1', [id_juego])
  if (query.rows.length == 0){
    ite = 1
  }
  else{
    ite = query.rows[0].iteracion +1
  }
  return ite
}

ipcMain.on('cargarJuego', async(event)=>[
  mainWindow.webContents.send("cargarC", configuracion)
])

ipcMain.on('enviarIte', async(event, seleccion, ganancia, perdida, total) =>{
  await enviarIteDB(seleccion, ganancia, perdida, total)
})

async function enviarIteDB(seleccion, ganancia, perdida, total){
  await getIte(id_juego).then(result => ite = result)
  if (seleccion == 'A'){
    seleccion = 1
  }
  else if (seleccion == 'B'){
    seleccion = 2
  }
  else if (seleccion == 'C'){
    seleccion = 3
  }
  else if (seleccion == 'D'){
    seleccion = 4
  }
  const query = await pool.query('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion, ganancia, perdida, total) VALUES ($1, $2, $3, $4, $5, $6, $7)', [id_juego, id_participante, ite, seleccion, ganancia, perdida, total])
  if (ite == 100){
    sacarIteDB2()
  }
}


async function sacarIteDB(){
  const query = await pool.query(`SELECT to_json(row(
    MAX(t.seleccion)      FILTER (WHERE t.rn = 1),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 2),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 3),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 4),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 5),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 6),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 7),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 8),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 9),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 10),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 11),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 12),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 13),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 14),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 15),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 16),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 17),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 18),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 19),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 20),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 21),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 22),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 23),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 24),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 25),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 26),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 27),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 28),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 29),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 30),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 31),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 32),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 33),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 34),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 35),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 36),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 37),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 38),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 39),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 40),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 41),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 42),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 43),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 44),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 45),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 46),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 47),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 48),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 49),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 50),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 51),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 52),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 53),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 54),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 55),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 56),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 57),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 58),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 59),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 60),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 61),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 62),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 63),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 64),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 65),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 66),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 67),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 68),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 69),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 70),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 71),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 72),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 73),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 74),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 75),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 76),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 77),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 78),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 79),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 80),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 81),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 82),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 83),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 84),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 85),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 86),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 87),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 88),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 89),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 90),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 91),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 92),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 93),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 94),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 95),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 96),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 97),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 98),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 99),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 100),
    t.id_participante,
    MAX(participante.etiqueta) FILTER(WHERE participante.id_participante = t.id_participante))
  ) FROM (
      SELECT *,
        ROW_NUMBER() OVER (PARTITION BY t.id_participante ORDER BY t.iteracion) AS rn
      FROM resultado t
  ) t, participante
  GROUP BY
    t.id_participante;`)

    aprendi.push([query.rows[0].to_json])
    aprendi.push([query.rows[1].to_json])
    aprendi.push([query.rows[2].to_json])
    aprendi.push([query.rows[3].to_json])
    aprendi.push([query.rows[4].to_json])
    aprendi.push([query.rows[5].to_json])
    aprendi.push([query.rows[6].to_json])
    aprendi.push([query.rows[7].to_json])
    aprendi.push([query.rows[8].to_json])
    aprendi = JSON.stringify(aprendi)
    let options = {
      mode: 'text',
      args: [aprendi, "HOLA"]
    }
    PythonShell.run('ia.py', options).then(messages=>{
      console.log(messages)
    },reason =>{
      console.log(reason)
    })
}

async function sacarIteDB2(){
  const query = await pool.query(`SELECT to_json(row(
    MAX(t.seleccion)      FILTER (WHERE t.rn = 1),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 2),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 3),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 4),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 5),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 6),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 7),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 8),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 9),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 10),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 11),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 12),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 13),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 14),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 15),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 16),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 17),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 18),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 19),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 20),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 21),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 22),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 23),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 24),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 25),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 26),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 27),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 28),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 29),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 30),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 31),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 32),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 33),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 34),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 35),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 36),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 37),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 38),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 39),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 40),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 41),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 42),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 43),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 44),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 45),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 46),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 47),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 48),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 49),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 50),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 51),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 52),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 53),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 54),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 55),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 56),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 57),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 58),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 59),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 60),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 61),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 62),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 63),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 64),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 65),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 66),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 67),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 68),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 69),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 70),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 71),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 72),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 73),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 74),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 75),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 76),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 77),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 78),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 79),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 80),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 81),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 82),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 83),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 84),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 85),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 86),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 87),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 88),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 89),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 90),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 91),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 92),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 93),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 94),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 95),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 96),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 97),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 98),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 99),
    MAX(t.seleccion)      FILTER (WHERE t.rn = 100),
    t.id_participante,
    MAX(participante.etiqueta) FILTER(WHERE participante.id_participante = t.id_participante))
  ) FROM (
      SELECT *,
        ROW_NUMBER() OVER (PARTITION BY t.id_participante ORDER BY t.iteracion) AS rn
      FROM resultado t
  ) t, participante
  WHERE t.id_participante = $1
  GROUP BY
    t.id_participante;`, [id_participante])
    console.log(query.rows[0].to_json)
    aprendi.push([query.rows[0].to_json])
    json = query.rows[0].to_json
    aprendi = JSON.stringify(aprendi)
    let options = {
      mode: 'text',
      args: [aprendi, "HOLA"]
    }
    PythonShell.run('ia.py', options).then(messages=>{
      console.log(messages)
      mainWindow.webContents.send("result", messages[0])
      const query2 = pool.query('UPDATE participante SET etiqueta = $1 WHERE id_participante = $2', [messages[0], id_participante])
      },reason =>{
      console.log(reason)
    })
}

