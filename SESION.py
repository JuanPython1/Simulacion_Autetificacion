class Seccion_login:

    def __init__(self):
        self.user_list = {"juan": "juan123", "Pamela": "nashe123"}

    def buscarUsuario(self, nombre_usuario):
        if nombre_usuario in self.user_list:
            return nombre_usuario
        return None

    def buscarContraseña(self, contraseña):
        if contraseña in self.user_list.values():
            return contraseña
        return None

    def L_facebook(self, usuario, contraseña):
        self.user_entrada = usuario
        self.pass_entrada = contraseña

        self.e_user = self.buscarUsuario(self.user_entrada)
        self.e_pass = self.buscarContraseña(self.pass_entrada)

        if self.user_entrada == self.e_user and self.pass_entrada == self.e_pass:
            return "Este usuario y contraseña es correcto"
        else:
            return "Usuario y/o contraseña incorrecto"



        
