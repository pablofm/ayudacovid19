function get_ubicacion(ubicacion){
    return [ubicacion.coordinates[1],ubicacion.coordinates[0]];
}
function get_colaboradores(url){
    var colaboradores = L.layerGroup();
    $.ajax({
        dataType: 'json',
        url: url,
        success: function(data) {
            for (index in data.features){
                var datos = data.features[index].properties;
                var marker = L.marker(get_ubicacion(data.features[index].geometry), { title: datos.nombre, icon: greenIcon }).addTo(colaboradores);
                marker.bindPopup("<b>"+datos.nombre+"</b></br>Teléfono:"+datos.telefono+"<br/>Email: "+datos.email+"<br/>Horario: "+datos.horario+"<br/>Tipo de ayuda: "+datos.servicios+"<br/>Identificador: "+datos.identificador);
            }
        },
        error: function (xhr, status, error) {
            alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText);
        }
    });
    return colaboradores;
}

function get_peticiones(url){
    var peticiones = L.layerGroup();
    $.ajax({
        dataType: 'json',
        url: url,
        success: function(data) {
            for (index in data.features){
                var datos = data.features[index].properties;
                var marker = L.marker(get_ubicacion(data.features[index].geometry), { title: datos.nombre, icon: redIcon }).addTo(peticiones);
                marker.bindPopup("<b>"+datos.nombre+"</b></br>Teléfono:"+datos.telefono+"<br/>Email: "+datos.email+"<br/>Petición: "+datos.peticion+"<br/>Identificador: "+datos.identificador);
            }
        },
        error: function (xhr, status, error) {
            alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText);
        }
    });
    return peticiones;
}


function resize(){
    $("body").css("padding-top", $('nav').outerHeight());
    $('#mapa').css("height", $(window).height()-$('nav').outerHeight());    
}

$(window).on("resize", resize);
