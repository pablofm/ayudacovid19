function get_ubicacion(ubicacion){
    return [ubicacion.coordinates[1],ubicacion.coordinates[0]];
}

function generar_popup_colaborador(nombre, horario, servicios, identificador){
    var popup = "<b>$NOMBRE$</b></br>Horario: $HORARIO$<br/>Tipo de ayuda: $SERVICIOS$ <br/>Identificador: $IDENTIFICADOR$";
    popup = popup.replace("$NOMBRE$", nombre);
    popup = popup.replace("$HORARIO$", horario);
    popup = popup.replace("$SERVICIOS$", servicios);
    popup = popup.replace("$IDENTIFICADOR$", "C-"+identificador);
    return popup;
}

function generar_popup_peticion(nombre, peticion, identificador){
    var popup = "<b>$NOMBRE$</b></br>"+"<br/>Petición: $PETICION$<br/>Identificador: $IDENTIFICADOR$";
    popup = popup.replace("$NOMBRE$", nombre);
    popup = popup.replace("$PETICION$", peticion);
    popup = popup.replace("$IDENTIFICADOR$", "P-"+identificador);
    return popup;
}

function get_colaboradores(url_colaboradores, url_contacto){
    var colaboradores = L.layerGroup();
    $.ajax({
        dataType: 'json',
        url: url_colaboradores,
        success: function(data) {
            for (index in data.features){
                var datos = data.features[index].properties;
                var marker = L.marker(get_ubicacion(data.features[index].geometry), { title: datos.nombre, icon: greenIcon }).addTo(colaboradores);
                var popup = generar_popup_colaborador(datos.nombre, datos.horario, datos.servicios, datos.identificador);
                var popup = popup.concat("<br/><a href='"+url_contacto.replace("0", datos.identificador)+"'>Contactar</a>");
                marker.bindPopup(popup);
            }
        },
        error: function (xhr, status, error) {
            alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText);
        }
    });
    return colaboradores;
}

function get_peticiones(url_peticiones, url_contacto){
    var peticiones = L.layerGroup();
    $.ajax({
        dataType: 'json',
        url: url_peticiones,
        success: function(data) {
            for (index in data.features){
                var datos = data.features[index].properties;
                var marker = L.marker(get_ubicacion(data.features[index].geometry), { title: datos.nombre, icon: redIcon }).addTo(peticiones);
                var popup = generar_popup_peticion(datos.nombre, datos.peticion, datos.identificador);
                var popup = popup.concat("<br/><a href='"+url_contacto.replace("0", datos.identificador)+"'>Contactar</a>");
                marker.bindPopup(popup);
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
