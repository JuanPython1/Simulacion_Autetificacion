
class Seccion_login:
  
  def __init__(self):
    self.user_list= ["juan","juan123"]

  def L_facebook (self,usuario,password):
    self.e_user=self.user_list[0]
    self.e_password=self.user_list[1]
    self.user_entrada=usuario
    self.pass_entrada=password
    if self.user_entrada == self.e_user:
        if self.pass_entrada == self.e_password:
            return "Este usuario y contraceña es correcto"
    else:
        return "Usuario y/o contraceña incorrecto"




