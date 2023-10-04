x=0;
merk = []
kode = []
daftarKosmetik = []
daftarHarga =[]
jawab = 'Y'
import math
def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1
    return -1
def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    middle = len(unsorted) // 2
    l_list = unsorted[:middle]
    r_list = unsorted[middle:]
    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)
    return list(merge(l_list, r_list))
def merge(l_half,r_half):
    s = []
    while len(l_half) != 0 and len(r_half)!=0:
        if l_half[0] < r_half[0]:
            s.append(l_half[0])
            l_half.remove(l_half[0])
        else:
            s.append(r_half[0])
            r_half.remove(r_half[0])
    if len(l_half) == 0:
       s = s + r_half
    else:
       s = s + l_half
    return s
def linierSearch(daftarKosmetik,cari):
    ketemu = False
    posisi = 0
    while posisi<len(daftarKosmetik) and ketemu :
        if daftarKosmetik[posisi] == cari:
            kertemu = True
        posisi = posisi+1
    print("Barang yang dicari ada di index = %i" %posisi)
    
print ("====================== Linda Kosmetik ===========================")
print ("| Kode = CT                                                     |")
print ("|   SHADE  |  EMINA CREAMY TINT  |   WARNA  |    HARGA          |")        
print ("|    A01   |    Brick Town       |   Light  |    Rp. 38.000     |")
print ("|    B02   |    Peach Crush      |  Natural |    Rp. 40.000     |")
print ("|    C03   |    Sunbeam          |   warm   |    Rp. 45.000     |")
print ("-----------------------------------------------------------------")
print ("| Kode = CS                                                     |")
print ("|   SHADE  |   EMINA CUSHION     |   WARNA  |    HARGA          |")
print ("|    A001  |      Light          |   Light  |    Rp. 80.000     |")
print ("|    B002  |     Natural         |  Natural |    Rp. 90.000     |")
print ("|    C003  |     Caramel         |   Warm   |    Rp. 85.000     |")
print ("=================================================================")

banyak=int(input("Masukkan Banyak Pembelian  : "))
for i in range (1,banyak+1,1):
    kode=input("Masukkan Kode ke-%i <CT/CS> : " %i)
    if(kode =="CT" or kode == "ct"):
        merk  = "EMINA CREAMY TINT"
        shade1 = input("Masukkan Shade yang anda inginkan (A01/B02/C03) = ")
        if(shade1 =="A01" or shade1=="a01"):
            merkTint="Brick Town"
            warna = "Light"
            harga = "Rp. 38.000"
            daftarKosmetik.append(merkTint)
            daftarHarga.append(harga)
            x=x+1
        elif(shade1 =="B02" or shade1 =="b02"):
            merkTint="Peach Crush"
            warna = "Natural"
            harga = "Rp. 40.000"
            daftarKosmetik.append(merkTint)
            daftarHarga.append(harga)
            x=x+1
        elif(shade1 =="C03" or shade1 =="c03"):
            merkTint="Sumbeam"
            warna = "Warm"
            harga = "Rp. 45.000"
            daftarKosmetik.append(merkTint)
            daftarHarga.append(harga)
            x=x+1
        else:
            print("Barang Tidak Ditemukan")
            x=x+1
    elif(kode =="CS" or kode == "cs"):
        merk = "EMINA CUSHION"
        shade2 = input("Masukkan Shade yang anda inginkan (A001/B002/C003) = ")
        if(shade2 =="A001" or shade2 =="a001"):
            merkCush="Light"
            warna = "Light"
            harga = "Rp. 80.000"
            daftarKosmetik.append(merkCush)
            daftarHarga.append(harga)
            x=x+1
        elif(shade2=="B002" or shade2 =="b002"):
            merkCush="Natural"
            warna = "Natural"
            harga = "Rp. 90.000"
            daftarKosmetik.append(merkCush)
            daftarHarga.append(harga)
            x=x+1
        elif(shade2 =="C003" or shade2 =="C003"):
            merkCush="Caramel"
            warna = "Warm"
            harga = "Rp. 85.000"
            daftarKosmetik.append(merkCush)
            daftarHarga.append(harga)
            x=x+1
        else:
            print("Barang Tidak Ditemukan")
    else :
        merk = "Error"
        merkTint =  "Error"
        merkCush = "Error"
        warna = "Error"
        harga = 0
        
print("Barang yang Masuk Kedalam Keranjang = %s " %daftarKosmetik)
print("Harga Barang = %s " %daftarHarga)
print()
urut =input("Ingin mengurutkan harga? (Y/T) = ")
if urut == 'Y' or urut== 'y' :
    print(merge_sort(daftarHarga))
print()
jawab = input("Ingin mencari kosmetik yang ada dikeranjang?(Y/T) = ")
cari    =input("Masukkan Nama Kosmetik yang ingin dicari = ")
if (jawab == 'Y' or jawab == 'y') :
    ketemuBarang = FibonacciSearch(daftarKosmetik,cari)
    print("Kosmetik yang anda cari berada di index ke-%i " %ketemuBarang)
else :
    print("Tidak ada kosmetik yang dicari")

def tampil () :
    print("***************************************")
    print("No\tShade\tMerk\tHarga")
    for i in range(0,banyak,1):
        print(i+1, end="\t")
        for j in range(0,3,1) :
            print(daftarHarga[i][j], end="\t")
        print()
tampil()

   
            
