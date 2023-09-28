random_list = [105, 3.1, "Hello", 737, "Python", 27, "World", 412, 5.5, "AI"]

int_dict = {}  # Untuk menyimpan nilai integer dalam bentuk dictionary
float_tuple = ()  # Untuk menyimpan nilai float dalam bentuk tuple
string_list = []  # Untuk menyimpan nilai string dalam bentuk list

for item in random_list:
    if isinstance(item, int):
        # Membagi angka menjadi satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100

        # Menyimpan dalam dictionary
        int_dict[item] = {"Ratusan": ratusan, "Puluhan": puluhan, "Satuan": satuan}
    elif isinstance(item, float):
        # Menambahkan float ke dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menambahkan string ke dalam list
        string_list.append(item)

print("\nNilai integer dalam bentuk dictionary:")
print(int_dict)
print("\nNilai float dalam bentuk tuple:")
print(float_tuple)
print("\nNilai string dalam bentuk list:")
print(string_list)
