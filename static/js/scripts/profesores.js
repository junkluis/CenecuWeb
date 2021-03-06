
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
      expresion2.test(biografia+key) == true){
        console.log("correcto");
    }else if(biografia.length > 255) {}  
    else {
      alert("- El primer caracter deber ser una letra." +
      "\n- Este campo permite solo permite letras y números.");
      event.preventDefault();
    }
  }

function validarLinkedin(event) {
  linkedin_url =  document.getElementById('url_linkedin').value;

  if(/(ftp|http|https):\/\/?(?:(www|ec)\.)?linkedin.com(\w+:{0,1}\w*@)?(\S+)(:([0-9])+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/.test(linkedin_url)){
    console.log("URL LinkedIn correcta");
  } else {
    alert("Este campo solo permite un URL de usuario de LinkedIn.");
  }
}

function validarLetrasNumerosFrase(event){
    var frase_personal = document.getElementById('frases_personal').value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    
    if(expresion.test(frase_personal+key) == true && 
      expresion2.test(frase_personal+key) == true){
        console.log("correcto");
    }else if(frase_personal.length > 200){}      
    else {
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

$(document).ready(function() {
  $('table#profesorTable').DataTable({
    "ordering": false,
  });
});

$('.delete').on("click", function (e) {
  e.preventDefault();
  var choice = confirm($(this).attr('data-confirm'));

  if (choice) {
      window.location.href = $(this).attr('href');
  }
});