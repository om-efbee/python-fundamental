#belajar casting
#merubah tipe data satu ke tipe data lain
#tipe data = int, float, string, bool

print ("==== integer  ====")
data_int     = 1
print ("data = ", data_int, "type   = ", type(data_int))

data_float   = float(data_int)
data_string  = str(data_int)
data_bool    = bool(data_int) #akan false kalo 0
print ("data = ", data_float, "type  = ", type(data_float))
print ("data = ", data_string, "type = ", type(data_string))
print ("data = ", data_bool, "type   = ", type(data_bool))

print ("====float ====")

data_float   = 9.5
print ("data = ", data_float, "type   = ", type(data_float))
data_int     = int(data_float)
data_string  = str(data_float)
data_bool    = bool(data_float) #akan false kalo 0

print ("data = ", data_int, "type     = ", type(data_int))
print ("data = ", data_string, "type  = ", type(data_string))
print ("data = ", data_bool, "type    = ", type(data_bool))

print ("====boolean ====")

data_bool = False
print ("data = ", data_bool, "type = ", type(data_bool))
data_int = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool)
print ("data = ", data_int, "type = ", type(data_int))
print ("data = ", data_string, "type = ", type(data_string))
print ("data = ", data_float, "type = ", type(data_float))

print ("====string ====")

data_str = "10"
print ("data = ", data_str, "type = ", type(data_str))
data_int = int(data_str)
data_string = str(data_str)
data_float = float(data_str)
print ("data = ", data_int, "type = ", type(data_int))
print ("data = ", data_string, "type = ", type(data_string))
print ("data = ", data_float, "type = ", type(data_float))