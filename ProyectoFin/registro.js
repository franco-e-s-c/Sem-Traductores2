(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          else{
            guardarPar()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

async function guardarPar(){
    nombre = document.getElementById('nombre').value
    edad = document.getElementById('edad').value
    datos = [nombre, edad]
    await window.Bridge.guardarParticipante(datos)
    window.location.href = 'juego.html'
}