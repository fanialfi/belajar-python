# tipe data = angka satuan (integer)

data_integer = 99999999999999999999
print("data : ",data_integer)
print("- bertipe : ",type(data_integer))

# tipe data = angka dengan koma (float)
data_float = 1.2
print("data : ",data_float)
print("- bertipe : ",type(data_float))

# tipe data = string (kumpulan karakter)
data_string = "ucup10"
print("data : ",data_string)
print("- bertipe : ",type(data_string))

# tipe data = biner true/false (boolean)
data_biner = True
print("data : ",data_biner)
print("- bertipe : ",type(data_biner))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6);
print("data : ",data_complex)
print("- bertipe : ",type(data_complex))

# tipe data dari bahasa C
# harus import dulu dari package / library
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ",data_c_double)
print("- bertipe : ",type(data_c_double))