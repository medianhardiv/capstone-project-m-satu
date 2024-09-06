class MakhlukHidup :
    def __init__(self, name, age, alive) :
        self.nama = name
        self.umur = age
        self.masihHidup = alive
    
    def bernafas(self) :
        print('{} sedang bernafas'.format(self.nama))

class Manusia(MakhlukHidup) :
    def __init__(self, name, age, alive, job) :
        super().__init__(name, age, alive)
        self.pekerjaan = job

class Hewan(MakhlukHidup) :
    def __init__(self, name, age, alive, canFly) :
        super().__init__(name, age, alive)
        self.dapatTerbang = canFly

class Tumbuhan(MakhlukHidup) :
    def __init__(self, name, age, alive, rootType) :
        super().__init__(name, age, alive)
        self.jenisAkar = rootType
    
    def bernafas(self):
        print('{} bernafas menggunakan pori-pori stomata'.format(self.nama))

manusia1 = Manusia('Budi', 21, True, 'Teacher')
tumbuhan1 = Tumbuhan('Pohon Pisang', 1, True, 'Akar Serabut')

print(manusia1.__dict__)
print(tumbuhan1.__dict__)
manusia1.bernafas()
tumbuhan1.bernafas()