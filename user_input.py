# mengambil input dari user
data = input("masukkan data : ")
# tipe data yang diambil dari user, dari console akan selalu bertipe string
print("data : ", data, "\n\ttype data : ", type(data))

# jika ingin menbambil input dari user berupa integer
data_int = int(input("masukkan data : "))
print("data : ", data_int, "\n\tType data : ", type(data_int))

# jika ingin mengambil input dari user berupa boolean
data_bool = bool(int(input("masukkan 1/0 : ")))
print("data : ", data_bool, "\n\tType data : ", type(data_bool))

data_int_dua = None
print("data : ", data_int_dua, "\n\tType : ", type(data_int_dua))

while True:
    try:
        data_int_dua = int(input("masukkan angka : "))
        break
    except ValueError:
        print("data yang dimasukkan harus angka")

print("data : ", data_int_dua, "\n\tType : ", type(data_int_dua))
