function validarIngresos() {
    var nombre = document.forms["nuevoCurso-form"]["nombreCurso"].value;
    var descrip = document.forms["nuevoCurso-form"]["descripcion"].value;
    var pensum = document.forms["nuevoCurso-form"]["pensum"].value;
    var duracion = document.forms["nuevoCurso-form"]["duracion"].value;
    var horarios = document.forms["nuevoCurso-form"]["horarios"].value;
    var costo = document.forms["nuevoCurso-form"]["costo"].value;
    var imagen = document.forms["nuevoCurso-form"]["imagen"].value;
    var estado = document.forms["nuevoCurso-form"]["estado"].value;
    if (nombre && descrip && pensum && duracion && costo && imagen && estado == "") {
        alert("Ingrese todos los campos");
        return false;
    }
    else {
    	return true;
    }


}
