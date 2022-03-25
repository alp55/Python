



from tokenize import Double


yarıcap=input("yarıçap degeri giriniz ") # input ile yarıcap degeri girilir
yarıcap=float(yarıcap)                   # girilen yarıcap degeri float türünde tanımlanır
alan=3.14*(yarıcap^2)                    # dairenin alanı hesaplanır
cevre=(2*3.14)*yarıcap                   # dairenin cevresi hesaplanır
print("dairenin alanı",alan)             # alan degişkeni ile degişkenin alanı ekrana yazdırılır
print("dairenin cevresi",cevre)          # cevre degişkeni ile dairenin cevresi ekrana yazdırılır
