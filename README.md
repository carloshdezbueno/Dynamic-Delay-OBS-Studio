# Dynamic-Delay-OBS-Studio

Dynamic delay system for OBS Studio mainly aimed for streamers who want to change between 0 seconds delay and an among of delay to play competitive games without being stream sniped. 


# WIP


## How to deploy

Here you will find the steps to get a functional project for testing, free use or improvement.


### How to setup python enviroment

1. Install last version of <a href='https://www.python.org/downloads/'>Python 3</a>
2. Install setuptools `pip3 install setuptools`
3. Install requeriments with `python3 setup.py install`

At this point, you will have all the required modules installed.

### How to setup OBS Studio

1. Install <a href='https://obsproject.com/es/download'>OBS Studio</a>.
2. Install <a href='https://github.com/Palakis/obs-websocket/releases'>OBS websocket</a>.
3. Open OBS Studio and create two profiles. Make reference to which one is for recording and which one is for streaming.
4. Create two shortcut of OBS Studio in your desktop.
5. Enter properties of each shortcut and configure like this:<br>
    5.1. Add in the source field of one shortcut `"C:\Program Files\obs-studio\bin\64bit\obs64.exe" --multi --profile "recordingOBS"`. <br>
    5.2. Add in the source field of the other shortcut`"C:\Program Files\obs-studio\bin\64bit\obs64.exe" --multi --profile "streamingOBS"`.
        (Change the name next to --profile with the name of each profiles created in step 3)
6. Open both shortcut. You will have two instances of OBS Studio running with different profiles. Maybe you will have an error caused by OBS Websockets, it doesnt matter.
7. Go to `Tolls->WebSocket Server settings` in both obs and change the server port of each to the desired ones. Notice that you can't have the same port in both OBS Studio.
8. Create all the scenes you need for your stream and add two more scenes. One is for adding Delay and the other one for removing the delay.
<!--

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.
-->

