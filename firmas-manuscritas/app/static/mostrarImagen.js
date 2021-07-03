function mostrarFirmaOriginal() {
    var archivo = document.getElementById("firmaOriginal").files[0];
    var reader = new FileReader();
    if (firmaOriginal) {
        reader.readAsDataURL(archivo);
        reader.onloadend = function() {
            document.getElementById("firmaA").src = reader.result;
            document.getElementById("firmaB").src = reader.result;
        }
        activarBotonAnalizar()
        document.getElementById("firmaOriginal").disabled.true;
    }
}

function activarBotonAnalizar() {
    document.getElementById("btnAnalizar").disabled = false;
}

function parrafoTexto() {
    document.getElementById("parrafoAnalizar").innerText = "Preparado para analizar firma...";
}