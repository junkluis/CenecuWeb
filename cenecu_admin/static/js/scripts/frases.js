
//Validación de campos

function validarLetrasNumeros(event){
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

function validarFormatoImagen(){
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById('img_frase');
    var archivo = imagen.value;
    if(!extensionImagenes.test(archivo)){
        console.log(archivo);
        alert("El formato de la imagen no es válido.");
        document.getElementById('img_frase').value = "";        
    }
}

function resetForm(){
    document.getElementById("nuevaFrase-form").reset();
} 
