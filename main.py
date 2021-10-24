#Membuat Class
class Kulkas :
  brand=None
  dimensi=None
  volume=None
  watt=None
  TempratureIs = [4]
  weight=None
  on=False

  def __init__(self, brand, dimensi, volume, watt, TempratureIs, weight):
      self.brand = brand
      self.dimensi = dimensi 
      self.volume = volume
      self.watt = watt
      self.TempratureIs = TempratureIs
      self.weight = weight

  def turnOn(self):
      self.on = True

  def turnOff(self):
      self.on = False

  def scanTemprature(self):
      newTempratureIs = []
      for i in range(0, 7):
          newTempratureIs.append(i)
      self.temprature = newTempratureIs

  def printData(self):
      print("------------------------------")
      print(f'Brand : {self.brand}')
      print(f'dimensi : {self.dimensi}')
      print(f'volume : {self.volume}')
      print(f'Watt : {self.watt}')
      print(f'weight : {self.weight}')
      print(f'On  : {"Nyala" if self.on else "Mati"}')
      print(f'On  : {"Pendingin Nyala" if self.on else "Pendingin Mati" }')
      print("------------------------------\n")

#kulkasKamar

class KulkasGEA(Kulkas):
    def __init__(self, brand, dimensi, volume, watt, TempratureIs, weight):
        super(KulkasGEA, self).__init__(brand, dimensi,volume, watt, TempratureIs, weight)
        self.wave = 'KulkasGEA'



class KulkasPolytron(Kulkas):
    def __init__(self, brand, dimensi, volume, watt, TempratureIs, weight):
        super(KulkasPolytron, self).__init__(brand, dimensi, volume, watt, TempratureIs, weight)
        self.wave = 'KulkasPolytron'


kulkasKamar = KulkasGEA('GEA', '44x47x57', '46', '82', '4', '13,2')
kulkasKamar.turnOn()
kulkasKamar.scanTemprature()
kulkasKamar.printData()

kulkasKamar.turnOff()
kulkasKamar.printData()

#kulkasDapur

kulkasDapur = KulkasPolytron('Polytron', '48x52x160', '210', '110', '4', '43')
kulkasDapur.turnOn()
kulkasDapur.scanTemprature()
kulkasDapur.printData()

kulkasDapur.turnOff()
kulkasDapur.printData()