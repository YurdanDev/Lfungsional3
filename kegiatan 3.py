random_list = [3.1, 0, "Hello", 5.5, 107, 2.7, "Python", "world", 12]

# Filter untuk memisahkan nilai float, int, dan string
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_value(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped_data = list(map(map_int_value, int_data))

# Output
print("Data Float:", float_data)
print("Data Int:")
for item in int_mapped_data:
    print(item)
print("Data String:", string_data)