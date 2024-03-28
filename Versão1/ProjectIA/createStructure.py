import os

def create_project_structure(base_path):
    directories = [
        "controllers",
        "services",
        "utils",
        "models",
        "documentos",
    ]
    files = {
        "": [".env", "main.py", "requirements.txt"],
        "controllers": ["pdf_controller.py"],
        "services": ["genai_service.py"],
        "utils": ["env_loader.py"],
    }

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        for file in files.get(directory, []):
            open(os.path.join(dir_path, file), 'a').close()  # Cria o arquivo se não existir

    for file in files[""]:
        open(os.path.join(base_path, file), 'a').close()

if __name__ == "__main__":
    create_project_structure("Project-Gemini")
