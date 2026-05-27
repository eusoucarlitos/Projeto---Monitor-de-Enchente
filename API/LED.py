class Atuador:
  
  def __init__(self, nome, pino):
    self._nome = nome
    self._pino = pino
    self._estado = False

  def get_estado(self):
    return self._estado

  def ligar(self):
    self._estado = True
    print(f{self._nome} ligado)
    return self._estado

  def desligar(self):
    self._estado = False
    print(f{self._nome} desligado)
    return self._estado
    
  def alternar(self):
      if self._estado:
        return self.desligar()
      else:
        return self.ligar()

 class LED(Atuador):

  def __init__(self, pino, cor=vermelho):
    super().__init__(fLED {cor}, pino)
    self._cor = cor
