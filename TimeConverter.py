# def timeConverter(detik):
#     detik = int(input("Masukkan detik: "))
#     return detik
# def ubah_jam(d):
#     j = int(detik)//3600
#     return j

# def ubah_menit(d):
#     m = (int(j%3600))//60
#     return m

# def ubah_second(d):
#     s = (int(m))%60
#     return s

# def tampilkan_semua(jam,menit,second):
#     print("tampilkan jam : ", jam)
#     print("tampilkan menit : ", menit)
#     print("tampilkan second : ", detik)
# detik=3600
# print(timeConverter)

###Maaf mas, Ujian ini saya menyerah aja###

detik=int(input("Ketik nilai detik ="))
D=detik
H=D//86400
D=D%86400
J=D//3600
D=D%3600
M=D//60
D=D%60
print(detik,"detik = ",J," jam + ",M," menit + ",D," detik")