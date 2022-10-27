//BARRA DE NAVEGACIÓN: enlaces y datos.
//guardar los datos en arrays:
var titulos=new Array();
var enlaces=new Array();
//Datos de los submenús
titulos[0]=new Array
();
enlaces[0]=new Array("#","#","#","#","#");

titulos[1]=new Array
(
    "Región Andina",
    "Región Caribe",
    "Región Pacífica",
    "Región Orinoquí",
    "Región Amazonía"
);
enlaces[1]=new Array("#","#","#","#","#");

//arrays para guardar elementos de la lista y submenús:
var menu=new Array()
var submenu=new Array()

window.onload = function() {
//BARRA DE NAVEGACIÓN: Crear desplegables:
for (i=0;i<titulos.length;i++) {
     //localizar elementos principales
     menu[i]=document.getElementById("seccion_ini"+i);
     //crear elemento menu desplegable
     menu[i].innerHTML+="<div id='subseccion"+i+"'></div>"
     //localizar elemento menu desplegable
     submenu[i]=document.getElementById('subseccion'+i);
     //escribir menu desplegable
     for (j=0;j<titulos[i].length;j++) {
         submenu[i].innerHTML += "<p><a href='"+enlaces[i][j]+"'>"+titulos[i][j]+"</a></p>";
         }
     //estilo de los submenús
     menu[i].style.position="relative";
     }	
//eventos para ver - ocultar menu
for (i=0;i<titulos.length;i++) {
    menu[i].onmouseover = ver;
    menu[i].onmouseout = ocultar;
    } 
}
//función para ver los menús desplegables.
function ver() {
         muestra=this.getElementsByTagName("div")[0];
         muestra.style.display="block"
         }
//funcion para ocultar los menús desplegables.
function ocultar() {
         oculta=this.getElementsByTagName("div")[0];
         oculta.style.display="none"
         }
/*--------------------------------------------------------------------------------------------------*/
/*
//BARRA DE NAVEGACIÓN: enlaces y datos.
//guardar los datos en arrays:
var titulos_andi=new Array();
var enlaces_andi=new Array();
//Datos de los submenús
titulos_andi[0]=new Array(
          "Subsección uno uno",
          "Subsección uno dos",
          "Subsección uno tres",
          "Subsección uno cuatro");
enlaces_andi[0]=new Array("#","#","#","#");

titulos_andi[1]=new Array(
          "Subsección dos uno",
          "Subsección dos dos",
          "Subsección dos tres",
          "Subsección dos cuatro",
          "Subsección dos cinco");
enlaces_andi[1]=new Array("#","#","#","#","#");

titulos_andi[2]=new Array(
          "Subsección tres uno",
          "Subsección tres dos",
          "Subsección tres tres",
          "Subsección tres cuatro",
          "Subsección tres cinco");
enlaces_andi[2]=new Array("#","#","#","#","#");	

titulos_andi[3]=new Array(
          "Subsección cuatro uno",
          "Subsección cuatro dos",
          "Subsección cuatro tres");
enlaces_andi[3]=new Array("#","#","#");
	
//arrays para guardar elementos de la lista y submenús:
var menu_andi=new Array()
var submenu_andi=new Array()

window.onload = function() {
//BARRA DE NAVEGACIÓN: Crear desplegables:
for (i=0;i<titulos_andi.length;i++) {
     //localizar elementos principales
     menu_andi[i]=document.getElementById("seccion_andi"+i);
     //crear elemento menu desplegable
     menu_andi[i].innerHTML+="<div id='subseccion_andi"+i+"'></div>"
     //localizar elemento menu desplegable
     submenu_andi[i]=document.getElementById('subseccion_andi'+i);
     //escribir menu desplegable
     for (j=0;j<titulos_andi[i].length;j++) {
         submenu_andi[i].innerHTML += "<p><a href='"+enlaces_andi[i][j]+"'>"+titulos_andi[i][j]+"</a></p>";
         }
     //estilo de los submenús
     menu_andi[i].style.position="relative";
     }	
//eventos para ver - ocultar menu
for (i=0;i<titulos_andi.length;i++) {
    menu_andi[i].onmouseover = ver_andi;
    menu_andi[i].onmouseout = ocultar_andi;
    } 
}
//función para ver los menús desplegables.
function ver_andi() {
         muestra_andi=this.getElementsByTagName("div_andi")[0];
         muestra_andi.style.display="block"
         }
//funcion para ocultar los menús desplegables.
function ocultar_andi() {
         oculta_andi=this.getElementsByTagName("div_andi")[0];
         oculta_andi.style.display="none"
         }
*/