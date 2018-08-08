
//Valicación de campos

function validarLetras(event) {
    var input = document.getElementsByClassName('letras').value;
	var key = event.key;
	var keyCode = event.keyCode;
	var expresion = /^[A-Za-záéíóúÁÉÍÓÚñÑ\s\.\',']+$/;

	if(!expresion.test(input+key)){
	  alert("Este campo permite solo permite letras.");
	  event.preventDefault();
	}
}

function validarLetrasNumerosBiografia(event){
    var biografia = document.getElementById('biografia').value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    
    if(expresion.test(biografia+key) == true && 
      expresion2.test(biografia+key) == true && 
      biografia.length < 256){
        console.log("correcto");
    } else {
      alert("- El primer caracter deber ser una letra." +
      "\n- Este campo permite solo permite letras y números.");
      event.preventDefault();
    }
  }

  function validarLetrasNumerosFrase(event){
    var frase_personal = document.getElementById('frases_personal').value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    
    if(expresion.test(frase_personal+key) == true && 
      expresion2.test(frase_personal+key) == true && 
      frase_personal.length < 200){
        console.log("correcto");
    } else {
      alert("- El primer caracter deber ser una letra." +
      "\n- Este campo permite solo permite letras y números.");
      event.preventDefault();
    }
  }

function validarFormatoArchivo() {
	var extensionArchivo = /(.pdf)$/i;
	var curriculum = document.getElementById('curriculum');
	var archivo = curriculum.value;
	if(!extensionArchivo.test(archivo)){
	    console.log(archivo);
	    alert("El formato del currículum debe ser PDF.");
	    document.getElementById('curriculum').value = "";        
	}
}

function validarFormatoImagen(){
	var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
	var imagen = document.getElementById('img_perfil');
	var archivo = imagen.value;
	if(!extensionImagenes.test(archivo)){
	    console.log(archivo);
	    alert("El formato de la imagen no es válido.");
	    document.getElementById('img_perfil').value = "";        
	}
}

function resetForm(){
    document.getElementById("nuevoProfesor-form").reset();
}
