#belajar casting
#merubah tipe data satu ke tipe data lain
#tipe data = int, float, string, bool

data_int = 0

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) #akan false kalo 0
print ("data = ", data_int, "type = ", type(data_int))
print ("data = ", data_float, "type = ", type(data_float))
print ("data = ", data_string, "type = ", type(data_string))
print ("data = ", data_bool, "type = ", type(data_bool))