from fastapi import FastAPI
import urllib.request
import urllib.error

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hola Mundo desde K8s y ArgoCD! Wii"}
    
    #base_message = "Hola Mundo desde K8s y ArgoCD! Wii"
    #url = "http://localhost:8088/hello"
    #url = "http://192.168.31.219:8088/hello"
    #
    #try:
    #    # Realizamos la llamada GET
    #    with urllib.request.urlopen(url, timeout=5) as response:
    #        external_data = response.read().decode('utf-8')
    #        result_message = f"{base_message} | Respuesta API: {external_data}"
    #except urllib.error.URLError as e:
    #    # Capturamos errores de conexión o HTTP (404, 500, etc.)
    #    result_message = f"{base_message} | Error en llamada: {str(e)}"
    #except Exception as e:
    #    # Capturamos cualquier otro error inesperado
    #    result_message = f"{base_message} | Error inesperado: {str(e)}"
    
    #return {"message": result_message}

@app.get("/health")
async def health_check():
    return {"status": "ok"}