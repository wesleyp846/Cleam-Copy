import os
import shutil

folder_path = "E:/"
duplicates_folder = os.path.join(folder_path, "duplicados")

file_sizes = {}

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        # Define a faixa de tamanhos de arquivo a ser considerada como duplicata
        size_range = range(file_size - 2048, file_size + 2049)
        found_duplicate = False
        for size in file_sizes.keys():
            if size in size_range:
                found_duplicate = True
                # Arquivo duplicado encontrado
                duplicate_name = f"{size}_{len(file_sizes[size])}"
                duplicate_path = os.path.join(duplicates_folder, duplicate_name)
                shutil.move(file_path, duplicate_path)
                file_sizes[size].append(duplicate_name)
                break
        if not found_duplicate:
            file_sizes[file_size] = [file_name]

# Imprime tamanhos de arquivos
print("\nTamanhos de arquivos:")
for file_size, file_names in file_sizes.items():
    print(f"{file_size} bytes:")
    for file_name in file_names:
        print(f" - {file_name}")
