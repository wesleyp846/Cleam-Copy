import os
import hashlib
import shutil

folder_path = "C:/"
duplicates_folder = os.path.join(folder_path, "duplicados")

file_sizes = {}
file_hashes = {}

duplicates = []

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        file_sizes[file_name] = file_size
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
            file_hashes[file_name] = file_hash

        # Detecta arquivos duplicados
        if file_size in file_sizes.values():
            for other_file_name, other_file_size in file_sizes.items():
                if file_size == other_file_size and file_name != other_file_name:
                    if file_hashes[file_name] == file_hashes[other_file_name]:
                        if sorted([file_name, other_file_name]) not in duplicates:
                            duplicates.append(sorted([file_name, other_file_name]))

# Move arquivos duplicados para a pasta "duplicados"
if duplicates:
    print("Arquivos duplicados encontrados. Movendo para a pasta 'duplicados'...")
    if not os.path.exists(duplicates_folder):
        os.mkdir(duplicates_folder)
    for pair in duplicates:
        for file_name in pair:
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(duplicates_folder, file_name)
            shutil.move(old_path, new_path)
    print("Arquivos duplicados movidos com sucesso para a pasta 'duplicados'.")
else:
    print("Nenhum arquivo duplicado encontrado.")

# Imprime tamanhos de arquivos
print("\nTamanhos de arquivos:")
for file_name, file_size in file_sizes.items():
    print(f"{file_name}: {file_size} bytes")

# Imprime hashes de arquivos
print("\nHashes de arquivos:")
for file_name, file_hash in file_hashes.items():
    print(f"{file_name}: {file_hash}")
