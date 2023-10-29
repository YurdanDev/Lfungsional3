data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]

integer_values = []

for entry in data:
    data_split = entry.split()
    # Menggunakan filter untuk hanya mengambil nilai integer
    filtered_values = list(filter(str.isdigit, data_split))
    integer_values.append(filtered_values)

for values in integer_values:
    print(values)