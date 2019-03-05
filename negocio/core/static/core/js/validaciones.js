////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////Productos/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_nombre(){
	var nombre = document.getElementById("id_nombre");
    var regex_nombre = /^\w{1,20}(\s\w{1,20})*$/;
	var span_nombre = document.getElementById("id_nombre-invalid");
	nombre.classList.remove("is-valid");
	nombre.classList.remove("is-invalid");
	if(nombre.value.trim().length != 0){
		if(nombre.value.match(regex_nombre)){
			nombre.classList.add("is-valid");
			return true;
		}else{
			span_nombre.innerHTML="Ingrese un nombre valido, sin espacios al principio/final";
			nombre.classList.add("is-invalid");
			nombre.focus();
			return false;
		}
	}else{
		span_nombre.innerHTML="Por favor rellene el campo vacio";
		nombre.classList.add("is-invalid");
		nombre.focus();
		return false;
	}
}

function validar_categoria(){
	var categoria = document.getElementById("id_categoria");
	var span_categoria = document.getElementById("id_categoria-invalid");
	categoria.classList.remove("is-valid");
	categoria.classList.remove("is-invalid");
	if(!categoria.value ==""){
			categoria.classList.add("is-valid");
			return true;
	}else{
		span_categoria.innerHTML="Seleccione una categoria";
		categoria.classList.add("is-invalid");
		categoria.focus();
		return false;
	}
}

function validar_unidad_medida(){
	var unidad_medida = document.getElementById("id_unidad_medida");
	var span_unidad_medida = document.getElementById("id_unidad_medida-invalid");
	unidad_medida.classList.remove("is-valid");
	unidad_medida.classList.remove("is-invalid");
	if(!unidad_medida.value ==""){
			unidad_medida.classList.add("is-valid");
			return true;
	}else{
		span_unidad_medida.innerHTML="Seleccione una opcion";
		unidad_medida.classList.add("is-invalid");
		unidad_medida.focus();
		return false;
	}
}

function validar_precio_compra(){
	var precio_compra = document.getElementById("id_precio_compra");
	var span_precio_compra = document.getElementById("id_precio_compra-invalid");
	precio_compra.classList.remove("is-valid");
	precio_compra.classList.remove("is-invalid");
	    if (precio_compra.value.trim().length != 0 && precio_compra.value >= 0){
            precio_compra.classList.add("is-valid");
            return true;
        }else{
            span_precio_compra.innerHTML="Rellene el campo correctamente";
            precio_compra.classList.add("is-invalid");
            precio_compra.focus();
            return false;
        }
}

function validar_precio_venta(){
	var precio_venta = document.getElementById("id_precio_venta");
	var span_precio_venta = document.getElementById("id_precio_venta-invalid");
	precio_venta.classList.remove("is-valid");
	precio_venta.classList.remove("is-invalid");
	    if (precio_venta.value.trim().length != 0 && precio_venta.value >= 0){
            precio_venta.classList.add("is-valid");
            return true;
        }else{
            span_precio_venta.innerHTML="Rellene el campo correctamente";
            precio_venta.classList.add("is-invalid");
            precio_venta.focus();
            return false;
        }
}

function validar_email(){
	var email = document.getElementById("email");
	var regex_email = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/;
	var span_email = document.getElementById("email-invalid");
	email.classList.remove("is-valid");
	email.classList.remove("is-invalid");
	if(!email.value ==""){
		if(email.value.match(regex_email)){
			email.classList.add("is-valid");
			return true;
		}else{
			span_email.innerHTML="Por favor ingrese un email valido";
			email.classList.add("is-invalid");
			return false;
		}
	}else{
		span_email.innerHTML="Por favor rellene el campo en blanco.";
		email.classList.add("is-invalid");
		return false;
	}
}


function validar_condiciones(){
	var condiciones = document.getElementById("condiciones");
	condiciones.classList.remove("is-valid");
	condiciones.classList.remove("is-invalid");
	if(condiciones.checked){
		condiciones.classList.add("is-valid");
			return true;
	}else{
		condiciones.classList.add("is-invalid");
			return false;
	}
}

function validar(){

	if(validar_nombre() && validar_categoria() && validar_precio_compra() && validar_precio_venta() && validar_unidad_medida()){
		return true ;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////BUSCAR/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_buscar(){
	var buscar = document.getElementById("buscar_producto");
	var span_buscar = document.getElementById("buscar_producto-invalid");
	buscar.classList.remove("is-valid");
	buscar.classList.remove("is-invalid");
	if(buscar.value.trim().length != 0){
        buscar.classList.add("is-valid");
        return true;
	}else{
		span_buscar.innerHTML="Por favor rellene el campo";
		buscar.classList.add("is-invalid");
		buscar.focus();
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////LDC///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_local(){
	var local = document.getElementById("id_local");
	var span_local = document.getElementById("id_local-invalid");
	local.classList.remove("is-valid");
	local.classList.remove("is-invalid");
	if(!local.value ==""){
			local.classList.add("is-valid");
			return true;
	}else{
		span_local.innerHTML="Seleccione un local";
		local.classList.add("is-invalid");
		local.focus();
		return false;
	}
}


function validar_ldc(){

	if(validar_nombre() && validar_local()){
		return true;
	}else{
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////PRODUCTOS A COMPRAR///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_producto(){
	var producto = document.getElementById("id_cod_productos");
	var span_producto = document.getElementById("id_cod_productos-invalid");
	producto.classList.remove("is-valid");
	producto.classList.remove("is-invalid");
	if(!producto.value ==""){
			producto.classList.add("is-valid");
			return true;
	}else{
		span_producto.innerHTML="Seleccione un Producto";
		producto.classList.add("is-invalid");
		producto.focus();
		return false;
	}
}

function validar_cantidad(){
	var cantidad = document.getElementById("id_cantidad");
	var span_cantidad = document.getElementById("id_cantidad-invalid");
	cantidad.classList.remove("is-valid");
	cantidad.classList.remove("is-invalid");
	    if (cantidad.value.trim().length != 0 && cantidad.value >= 0){
            cantidad.classList.add("is-valid");
            return true;
        }else{
            span_cantidad.innerHTML="Rellene el campo correctamente";
            cantidad.classList.add("is-invalid");
            cantidad.focus();
            return false;
        }
}

function validar_productos_comprar(){

	if(validar_producto() && validar_cantidad()){
		return true;
	}else{
		return false;
	}
}