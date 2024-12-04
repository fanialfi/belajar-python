# casting => merubah dari 1 tipe data ke tipe data lain

# data integer
print("=====INTEGER=====")
data_int = 10
data_float = float(data_int);
data_string = str(data_int);
data_boolean = bool(data_int);  # akan false jika nilai int 0
print("nilai : ",data_int,"\n\ttipe data : ",type(data_int))
print("nilai : ",data_float,"\n\ttipe data : ",type(data_float))
print("nilai : ",data_string,"\n\ttipe data : ",type(data_string))
print("nilai : ",data_boolean,"\n\ttipe data : ",type(data_boolean))

# data float
print("=====FLOAT=====")
data_float = 0.9
data_int = int(data_float); # akan dibulatiakn ke bawah
data_string = str(data_float);
data_boolean = bool(data_float);  # akan false jika nilai float 0
print("nilai : ",data_float,"\n\ttipe data : ",type(data_float))
print("nilai : ",data_int,"\n\ttipe data : ",type(data_int))
print("nilai : ",data_string,"\n\ttipe data : ",type(data_string))
print("nilai : ",data_boolean,"\n\ttipe data : ",type(data_boolean))

# data string
print("=====STRING=====")
data_string = "100"
data_boolean = bool(data_string);  # akan false jika isi stringnya kosong
data_float = float(data_string); # jika data srting didalamnya bukan berupa string number / float, maka akan terjadi error
data_int = int(data_string); # jika data string didalamnya bukan berupa string number (exampel = "fani") maka akan terjadi errorf
print("nilai : ",data_string,"\n\ttipe data : ",type(data_string))
print("nilai : ",data_boolean,"\n\ttipe data : ",type(data_boolean))
print("nilai : ",data_float,"\n\ttipe data : ",type(data_float))
print("nilai : ",data_int,"\n\ttipe data : ",type(data_int))

# data boolean
print("=====BOOLEAN=====")
data_boolean = False
data_float = float(data_boolean)
data_int = int(data_boolean);
data_string = str(data_boolean);
print("nilai : ",data_boolean,"\n\ttipe data : ",type(data_boolean))
print("nilai : ",data_float,"\n\ttipe data : ",type(data_float))
print("nilai : ",data_int,"\n\ttipe data : ",type(data_int))
print("nilai : ",data_string,"\n\ttipe data : ",type(data_string))