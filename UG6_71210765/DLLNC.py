class NodeMahasiswa:
    def __init__(self,nama,ipk,n=None,p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p
    
    def getNama(self):
        return self._element

    def getIpk(self):
        return self._ipk

    def setNama(self,nama):
        self._element = nama
    
    def setIpk(self,ipk):
        self._ipk = ipk

class DoubleLList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size
    
    def addElementTail(self,nama,ipk):
        baru = NodeMahasiswa(nama,ipk)
        if self.isEmpty() == True:
            self._head = baru
            self._tail = baru
            self._head._next = None
            self._head._prev = None
            self._tail._next = None
            self._tail._prev = None
        else:
            self._tail._next = baru
            baru._prev = self._tail
            self._tail = baru
            self._tail._next = None
        self._size = self._size + 1
        print('data masuk ke tail')
    
    def deleteLast(self):
        if self.isEmpty() == False:
            d = None
            bantu = self._head
            if self._head._next != None:
                hapus = self._tail
                self._tail = self._tail._prev
                d = hapus._element
                hapus._next = None
                del hapus
            else:
                d = self._tail._element
                self._head = None
                self._tail = None
            self._size = self._size - 1
            print('# Data',d,'terhapus #')

    def printAllDescending(self):
        print('===== Print Descending =====')
        if self.isEmpty()==False:
            bantu = self._head
            while bantu!=self._tail._next:
                print('=========================')
                print('Nama :',bantu._element)
                print('IPK  :',bantu._ipk)
                bantu = bantu._next
            print()
        else:
            print("Kosong")

    def rataIpk(self):
        print('===== Rata-rata IPK =====')
        bantu = self._head
        total = 0
        bantu != None
        total += bantu.getIpk()
        bantu = bantu._next
        rumus = round(total/self._size,2)
        print('Rata - rata :',rumus)
            


DLLNC = DoubleLList()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Harris',3.6)
DLLNC.printAllDescending()
DLLNC.deleteLast()
DLLNC.printAllDescending()

DLLNC.rataIpk()
