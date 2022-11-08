import hashlib
from hashlib import md5
from hashlib import sha256

class hash_password():
    
    def __init__(self):
        self.respuesta  = {}
    
    def generate_hash_sha(self, message):
        '''
        Convierte un parametro a bytes, posteriormente genera el hash del mismo
        empleando el algoritmo de cifrado SHA256
        
        @parametros:
            message         -> Paramentro a convertir
            message_hash_md -> Parametro que almacena el hash generado
            respuesta       -> Diccionario con la respuesta de la instancía 
        '''
        try:
            message = bytes(message,'utf-8')
            self.message_hash_md = sha256(message).hexdigest()
            self.respuesta['hash'] = self.message_hash_md
        except Exception as e:
            print("Ocurrio un error al generar el hash: ", e)
            self.respuesta['error'] = e
        finally:
            return self.respuesta
                    
if __name__ == "__main__":
    password = hash_password()    
    print("Encriptación usando sha256: ")
    respuesta = password.generate_hash_sha("prueba")
    print(respuesta)

    