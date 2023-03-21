{/* <script>
    data = "{{image}}"
    
    var image = document.getElementById("img-txt");
    image.src = "";
    image.src = "data:image/png;base64," + data;

    function cargarfoto(){
        file = document.getElementById("imgs");
        imagen = document.getElementById("img-txt");
        txt64 = document.getElementById("img-text");

        if (file.files.length > 0){
            var fr = new FileReader();
            fr.onload = function()
            {
                imagen.src = ""
                imagen.src = fr.result;
                txt64.value = "";
                txt64.value = imagen.src.replace(/^data:image\/(png|jpg|jpeg);base64,/,"");
            }
            fr.readAsDataURL(archivoF.files[0]);
        }

    }
    
</script> */}

function ver() {
    var file = document.getElementById("imgs").files[0];
    var reader = new FileReader();
    if (file) {
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            document.getElementById("img-txt").src = reader.result;
        }
    }
}