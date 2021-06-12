print("Selamat datang di kalkulator kelulusan")
utul=float(input("Silahkan masukkan nilai ujian tulis anda :"))
uprak=float(input("Silahkan masukkan nilai ujian praktek anda :"))

if utul >= 70 and uprak >= 70:
    print("Selamat, anda lulus!")
elif utul >= 70 and uprak < 70:
    print("Anda harus mengulangi ujian praktek.") 
elif utul < 70 and uprak >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")