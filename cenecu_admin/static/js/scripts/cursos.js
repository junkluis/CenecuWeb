
//Validación de campos
function validarLetrasNumerosNombre(event){
    var input = document.getElementById('nombreCurso').value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    
    if(expresion.test(input+key) == true && 
      expresion2.test(input+key) == true && 
      input.length < 256){
        console.log("correcto");
    } else {
      alert("- El primer caracter deber ser una letra." +
      "\n- Este campo permite solo permite letras y números.");
      event.preventDefault();
    }
  }

  function validarLetrasNumerosDescripcion(event){
    var input = document.getElementById('descripcion').value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    
    if(expresion.test(input+key) == true && 
      expresion2.test(input+key) == true && 
      input.length < 256){
        console.log("correcto");
    } else {
      alert("- El primer caracter deber ser una letra." +
      "\n- Este campo permite solo permite letras y números.");
      event.preventDefault();
    }
  }

function validarFormatoArchivo() {
    var extensionArchivo = /(.pdf)$/i;
    var pensum = document.getElementById('pensum');
    var filePensum = pensum.value;
    if(!extensionArchivo.test(filePensum)){
        console.log(filePensum);
        alert("El formato del pensum debe ser PDF.");
        document.getElementById('pensum').value = "";            
    }
}

function validarFormatoImagen(){
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById('imagen');
    var fileImagen = imagen.value;
    if(!extensionImagenes.test(fileImagen)){
        console.log(fileImagen);
        alert("El formato de la imagen no es válido.");
        document.getElementById('imagen').value = "";            
    }

}

/*$( document ).ready(function() {
    let checks = $(".chk");
    console.log(checks);
    {% for dias in horario_curso %}
        $(".chk").each(function(index, element){
            console.log($(elemtn));
        });
        
    {% endfor %}
});*/

function validarCosto(event){
  var input = document.getElementsById('costo').value;
  var key = event.key;            // Obtengo la tecla que presiono
  var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
  expresion = /^[0-9]+[0-9\.]+$/;

  if(!expresion.test(input+key)){
    alert("Este campo solo permite numeros");
    event.preventDefault();
  }
}

function resetForm(){
    document.getElementById("nuevoCurso-form").reset();
}
