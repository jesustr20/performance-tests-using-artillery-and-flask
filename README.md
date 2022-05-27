# performance-tests-using-artillery-and-flask
creando dos endpoing con Flask [GET, POST], se crearon pruebas de testing usando Artillery con yaml.

Instalar Flask, dejo la guia de instalacion y configuracion de flask: https://flask.palletsprojects.com/en/2.1.x/installation/,
crear un entorno virtual: python -m venv nombre_entorno
activar el entorno virtual: nombre_entorno/scripts/activate.bat
Instalar el arhivo requirements.txt es otra opcion ya que tiene los paquetes a instalar: pip install -r requirements.txt

iniciamos Flask con "flask run"

tendremos 2 EndPoint: GET y POST

Endpoint/main.py

POST: /api/v1/post, method['POST']

GET: /api/v1/get, method['GET']

Ambos EndPoint reciben como param el "id", el fin de estas apis son para ser probadas con https://www.artillery.io/ usando y poniendo a prueba
los principios y opciones que tiene artillery para tester en QA, Pruebas de carga a gran escala antes de los lanzamientos de producción 
de nuevos servicios, o para preparar las aplicaciones y la infraestructura para el tráfico pesado, 
como el tráfico del Black Friday/Cyber Monday

Usando Artillery para testear los EndPoint:

Instalación estable
Se recomienda la versión estable de Artillery para la mayoría de los usuarios.

npm install

Instalar artillería a través de npm:

npm install -g artillery@latest

Esto instalará Artillery globalmente en su computadora.

Precaución
Si está instalando Artillery en un contenedor de Docker (o una imagen de Docker, por ejemplo, a través RUN npm install -g artilleryde), 
asegúrese de que la instalación no se ejecute como rootusuario.

Artillery también se puede instalar como una dependencia de desarrollo de un proyecto de Node.js con:

npm install -D artillery@latest

Precaución
No recomendamos instalar Artillery como una dependencia dentro de las bases de código de la aplicación. 
Este método de instalación solo se recomienda para bases de código que solo contienen pruebas.

Windows 
De forma predeterminada, PowerShell establece una política de ejecución en los clientes de escritorio de 
Windows que impide la ejecución de scripts. Si usa Windows PowerShell, es posible que vea el siguiente mensaje de error 
al intentar ejecutar Artillery:

artillery: File C:\Users\Artillery\AppData\Roaming\npm\artillery.ps1
cannot be loaded because running scripts is disabled on this system.

Para permitir que su sistema Windows use Artillery, deberá cambiar la política de ejecución de PowerShell aRemoteSigned. 
Abra PowerShell como administrador y use Set-ExecutionPolicypara cambiar la política de ejecución a RemoteSigned:

PS C:\Windows\system32> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y


Comprobando su 
Si solía npminstalar Artillery globalmente, ejecute:

artillery dino

Si instaló Artillery localmente para un proyecto, ejecute el siguiente comando desde la carpeta raíz de ese proyecto:

$(npm bin)/artillery dino

Debería ver un dinosaurio ASCII impreso en la terminal. Algo como esto:

Dinosaurio de artillería

![image](https://user-images.githubusercontent.com/13369296/170794233-636dc7de-a354-4159-bf2c-bf955e33e6ee.png)

usando el archivo Yaml "test.yaml", configuraremos una serie de pasos que se encuntra en la guia de artillery:  
https://www.artillery.io/docs/guides/getting-started/writing-your-first-test

La cual quedaria de esta manera.

![image](https://user-images.githubusercontent.com/13369296/170795124-405847d5-4a60-4ed5-8f2e-b5319dd0a2fb.png)
    
Podremos correr el archivo "test.yaml" con el siguiente comando:

artillery run test.yml

o tambien los siguientes comandos el cual generara un JSON y una vista amigable en html:

Generara un JSON:
artillery run -e develop test.yaml --output result.json

Generara una vista con datos y medidas en html:
artillery report --output result.html result.json
