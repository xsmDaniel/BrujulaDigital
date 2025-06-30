import os

EXPECTED_FOLDERS = [
    'src', 'docs', 'public', 'tests', 'scripts', '.github'
]
EXPECTED_FILES = [
    'README.md', 'CONTRIBUTING.md', '.env.example', 'package.json'
]
DOC_FILES = [
    'prompts_brujula_digital_xsm.json', 'Bitacora_Resumen_Brujula_Digital_XSM.pdf'
]

def check_repo_structure(base='.'):
    print("Verificando estructura de Brújula Digital...\n")
    # Carpetas principales
    for folder in EXPECTED_FOLDERS:
        path = os.path.join(base, folder)
        if os.path.isdir(path):
            print(f"✔ Carpeta encontrada: {folder}")
        else:
            print(f"✗ Falta carpeta: {folder}")

    # Archivos raíz
    for file in EXPECTED_FILES:
        path = os.path.join(base, file)
        if os.path.isfile(path):
            print(f"✔ Archivo encontrado: {file}")
        else:
            print(f"✗ Falta archivo: {file}")

    # Archivos importantes en /docs
    docs_path = os.path.join(base, 'docs')
    for doc_file in DOC_FILES:
        path = os.path.join(docs_path, doc_file)
        if os.path.isfile(path):
            print(f"✔ Archivo en /docs encontrado: {doc_file}")
        else:
            print(f"✗ Falta archivo en /docs: {doc_file}")

    print("\nRevisión terminada. Si hay ✗ revisa o crea los elementos faltantes.")

if __name__ == "__main__":
    check_repo_structure('.')