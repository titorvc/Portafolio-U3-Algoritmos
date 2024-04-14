console.log ("Hola, por favor ingresa la hora en formato de 24 horas y los minutos")
var hora = prompt ("Ingresa la hora");
document.write (hora);
var minutos = prompt ("Ingresa los minutos");
document.write (minutos);
if (hora > 18 ) {
    console.log ("Good day! The hour is: ", hora, ":",+ minutos);
}
else {
    console.log ("La hora es: ", hora, ":" + minutos);
}