function get_ubicacion(ubicacion){
    return [ubicacion.coordinates[1],ubicacion.coordinates[0]];
}

String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function generar_popup_colaborador(nombre, horario, mensaje, identificador){
    var popup = "<b>$NOMBRE$</b></br>Horario: $HORARIO$<br/>Tipo de ayuda: $MENSAJE$ <br/>Identificador: $IDENTIFICADOR$";
    popup = popup.replace("$NOMBRE$", nombre);
    popup = popup.replace("$HORARIO$", horario);
    popup = popup.replace("$MENSAJE$", mensaje);
    popup = popup.replace("$IDENTIFICADOR$", "C-"+identificador);
    return popup;
}

function generar_popup_peticion(nombre, mensaje, identificador){
    var popup = "<b>$NOMBRE$</b></br>"+"<br/>Petición: $MENSAJE$<br/>Identificador: $IDENTIFICADOR$";
    popup = popup.replace("$NOMBRE$", nombre);
    popup = popup.replace("$MENSAJE$", mensaje);
    popup = popup.replace("$IDENTIFICADOR$", "P-"+identificador);
    return popup;
}

function generar_popup_comercio(nombre, telefono, mensaje){
    var popup = "<b>$NOMBRE$</b></br>"+"<br/>Teléfono: $TELEFONO$<br/>Detalles: $MENSAJE$";
    popup = popup.replace("$NOMBRE$", nombre);
    popup = popup.replace("$TELEFONO$", telefono);
    popup = popup.replace("$MENSAJE$", mensaje);
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
                var popup = generar_popup_colaborador(datos.nombre, datos.horario, datos.mensaje, datos.identificador);
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
                var popup = generar_popup_peticion(datos.nombre, datos.mensaje, datos.identificador);
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

function get_comercios(url_peticiones){
    var peticiones = L.layerGroup();
    $.ajax({
        dataType: 'json',
        url: url_peticiones,
        success: function(data) {
            for (index in data.features){
                var datos = data.features[index].properties;
                var marker = L.marker(get_ubicacion(data.features[index].geometry), { title: datos.nombre, icon: blueIcon }).addTo(peticiones);
                var popup = generar_popup_comercio(datos.nombre, datos.telefono, datos.mensaje);
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

function get_current_location() {
    return new Promise((resolve) => {
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(
                ({ coords: { latitude, longitude } }) => {
                    resolve({ latitude, longitude });
                },
                // Como es una feature opcional, nos dan igual los errores
                () => resolve(undefined),
                {
                    enableHighAccuracy: true,
                }
            );
        } else {
            resolve(undefined);
        }
    });
}

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function map_go_to_current_location(map) {
    const location = await get_current_location();

    if (location) {
        // Reseteamos las coordinadas. Si no lo hacemos, Leaflet
        // a veces nos lleva a la ubicación incorrecta
        map.setView([0, 0]);

        await wait(100);

        map.setView([location.latitude, location.longitude]);
        map.setZoom(12);

        return location;
    }
}

var theMarker;

function map_mark(map, icon, lat, lon) {
    if (theMarker != undefined) {
        map.removeLayer(theMarker);
    };

    theMarker = L.marker([lat,lon], {icon}).addTo(map);
}

async function map_mark_current_location(map, icon) {
    const location = await map_go_to_current_location(map);
    
    if (location) {
        map_mark(map, icon, location.latitude, location.longitude)
    }
}

$(window).on("resize", resize);
