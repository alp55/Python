liste={"alperen":507456989,"mehmet":493543635,"kerem":3523543634,"faruk":"numarası yok"}

print(type(list)) #liste degişkenin veri tipini belirtik

print("\n",liste["faruk"]) #faruk anahtarının karşılıgını yansıtık

liste["naber"]=1243254231 #dict içine yeni kayıt ekledik

print("\n",liste) #liste degişkenin üzerindeki tüm kayıtları listeler 

print("\n",liste["naber"]) #yeni ekledigimiz kayıtın anahtar verisini yazdırdık 

del liste["naber"] #naber kayıtını sildim

print("\n",liste) #liste degişkenin üzerindeki tüm kayıtları listeler 

liste.clear() #tüm kayıtları silmek için clear kulanılır

print("\n",liste) #liste degişkenin üzerindeki tüm kayıtları listeler ama kayıt olmadıgı içi boş gösterir
