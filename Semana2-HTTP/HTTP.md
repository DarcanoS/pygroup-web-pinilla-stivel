# Mensajes HTTP

Los mensajes HTTP, son los medios por los cuales se intercambian datos entre servidores y clientes. Hay dos tipos de mensajes: _peticiones_, enviadas por el cliente al servidor, para pedir el inicio de una acción; y _respuestas_, que son la respuesta del servidor.

Las peticiones y respuestas HTTP, comparten una estructura similar, compuesta de:

1. Una línea de inicio ('start-line' en inglés) describiendo la petición a ser implementada, o su estado, sea de éxito o fracaso. Esta línea de comienzo, es siempre una única línea. 
1. Un grupo opcional de cabeceras HTTP, indicando la petición o describiendo el cuerpo ('body' en inglés) que se incluye en el mensaje. 
1. Una línea vacía ('empty-line' en inglés) indicando toda la meta-información ha sido enviada.
1. Un campo de cuerpo de mensaje opcional ('body' en inglés) que lleva los datos asociados con la petición (como contenido de un formulario HTML), o los archivos o documentos asociados a una respuesta (como una página HTML, o un archivo de audio, vídeo ... ) . La presencia del cuerpo y su tamaño es indicada en la línea de inicio y las cabeceras HTTP.

## Peticiones
### Start-line
La primera linea de la petición en HTTP se compone por:
`<verbo> <recurso> <versión>`

### Verbo
`GET` Solicita una representación de un recurso específico.

`HEAD` Pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.

`POST` Se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

`PUT` Reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

`DELETE` Borra un recurso en específico.

`CONNECT` Establece un túnel hacia el servidor identificado por el recurso.

`OPTIONS` Es utilizado para describir las opciones de comunicación para el recurso de destino.

## Respuestas
### Start-line
La primer linea de la respuesta en HTTP se conforma de:
`<versión> <codigo de estado> <texto de estado>`

### Código de estado
Este código le indica al cliente como interpretar la respuesta.
Los cuales se dividen de la siguiente manera:
`1XX` Información
`2XX` Éxito
`3XX` Redirección
`4XX` Error del Cliente
`5XX` Error del servidor
