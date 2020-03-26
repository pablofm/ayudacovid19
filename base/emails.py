from django.template import loader
from django.core.mail import send_mail
from django.conf import settings


def enviar_correo_pidiendo_ayuda(datos):
    '''
    Datos proporcionados:
    Diccionario con las claves:
        'colaborador':  nombre del colaborador
        'email': email del colaborador
        'nombre':  Nombre de la persona que solicita ayuda
        'mensaje':  Mensaje de la persona que solicita ayuda
        'enlace': Enlace para validar el acceso
    '''
    asunto = "Alguien te necesita"
    plain_message = """
        Hola {0},
        Nos ponemos en contacto contigo porque alguien ha solicitado tu ayuda. Los datos de la petición son los siguientes:
            - Nombre: {1}
            - Mensaje: {2}
        Si quieres atender a esta petición y proporcionarle tus datos de contacto (también te proporcionaremos los datos de la persona solicitante) entra en el siguiente enlace.
        (si no funciona, copia y pega en tu navegador):
        {3}
        Si no quieres atenderla ignora este mensaje
        Un saludo y que tengas un buen día.
        #QUEDATEENCASA
    """.format(datos["colaborador"], datos["nombre"], datos["mensaje"], datos["enlace"])
    html_message = loader.render_to_string('base/emails/peticion_ayuda.html', datos)
    send_mail(asunto, plain_message, settings.EMAIL_HOST_USER, (datos["email"],), fail_silently=False, html_message=html_message)


def enviar_correo_ofreciendo_ayuda(datos):
    '''
    Datos proporcionados:
    Diccionario con las claves:
        'peticion':  nombre de la persona necesitada
        'email': email de la persona necesitada
        'nombre':  Nombre de la persona que ofrece ayuda
        'mensaje':  Mensaje de la persona que ofrece ayuda
        'enlace': Enlace para validar el acceso
    '''

    asunto = "Alguien quiere ayudarte"
    plain_message = """
        Hola {0},
        Nos ponemos en contacto contigo porque alguien quiere ayudarte. Los datos de la petición son los siguientes:
            - Nombre: {1}
            - Mensaje: {2}
        Si quieres aceptar esta oferta y proporcionarle tus datos de contacto (también te proporcionaremos los datos de la persona que quiere ayudarte) entra en el siguiente enlace (si no funciona, copia y pega en tu navegador):
        (si no funciona, copia y pega en tu navegador)
        {3}
        Si no quieres atenderla ignora este mensaje
        Un saludo y que tengas un buen día.
        #QUEDATEENCASA
    """.format(datos["peticion"], datos["nombre"], datos["mensaje"], datos["enlace"])
    html_message = loader.render_to_string('base/emails/ofrecimiento_ayuda.html', datos)
    send_mail(asunto, plain_message, settings.EMAIL_HOST_USER, (datos["email"],), fail_silently=False, html_message=html_message)


def enviar_correo_acceso_datos(datos):
    '''
    Datos proporcionados:
    Diccionario con las claves:
        'nombre_para':  nombre de la receptora del correo
        'email_para': email de la receptora del correo
        'nombre_contacto':  Nombre del contacto
        'telefono_contacto':  Teléfono del contacto
        'email_contacto':  Email del contacto
        'mensaje_contacto':  Mensaje del contacto
    '''
    asunto = "Han aceptado tu solicitud de contacto"
    plain_message = """
        Hola {0},
        La persona con la que esperabas contactar ha aceptado que podamos compartir sus datos y os pongáis en contacto. Sus datos son:
            - Nombre: {1}
            - Teléfono: {2}
            - Email: {3}
            - Mensaje: {4}
       Un saludo y que tengas un buen día.
        #QUEDATEENCASA
    """.format(
        datos["nombre_para"], datos["nombre_contacto"], datos["telefono_contacto"], datos["email_contacto"], datos["mensaje_contacto"])
    html_message = loader.render_to_string('base/emails/acceso_datos.html', datos)
    send_mail(asunto, plain_message, settings.EMAIL_HOST_USER, (datos["email_para"],), fail_silently=False, html_message=html_message)