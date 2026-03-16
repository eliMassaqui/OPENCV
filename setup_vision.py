import subprocess
import sys
import os

def run_command(command, shell=True):
    """Executa um comando e retorna o código de status."""
    return subprocess.call(command, shell=shell)

def print_styled(text, color="white", bg=""):
    """Simula o estilo visual do PowerShell no console."""
    colors = {
        "cyan": "96m", "green": "92m", "yellow": "93m", 
        "red": "91m", "magenta": "95m", "white": "97m",
        "gray": "90m", "blue_bg": "44m", "green_bg": "42m"
    }
    prefix = f"\033[{colors.get(bg, '')}\033[{colors.get(color, '37m')}"
    print(f"{prefix}{text}\033[0m")

def setup_environment():
    # Limpar tela (cls)
    os.system('cls' if os.name == 'nt' else 'clear')

    print_styled("-" * 50, "cyan")
    print_styled("      🚀 INICIANDO CONFIGURAÇÃO DO AMBIENTE      ", "white", "blue_bg")
    print_styled("            NOME: vision | PYTHON: 3.10.19        ", "cyan")
    print_styled("-" * 50, "cyan")
    print()

    # 1. Criação do Ambiente
    print_styled("📦 [1/4] Criando base Conda...", "yellow")
    create_cmd = "conda create -n vision python=3.10.19 -y"
    
    if run_command(create_cmd) == 0:
        print_styled(" ✔️ Ambiente criado com sucesso!", "green")
    else:
        print_styled(" ❌ Erro ao criar ambiente. Verifique se o Conda está no PATH.", "red")
        input("Pressione Enter para sair...")
        sys.exit(1)

    # 2 e 3. Instalação de Pacotes (Usando o caminho direto do pip do novo ambiente)
    # Em scripts, é mais seguro chamar o pip do ambiente recém-criado diretamente
    if os.name == 'nt':
        pip_path = "conda run -n vision python -m pip install"
    else:
        pip_path = "conda run -n vision python -m pip install"

    print_styled("\n👁️ [3/4] Instalando Visão Computacional (MediaPipe/OpenCV)...", "cyan")
    print_styled("    Aguarde, processando pacotes pesados...", "gray")
    
    cv_packages = "mediapipe==0.10.20 opencv-python==4.12.0.88 opencv-contrib-python==4.11.0.86"
    run_command(f"{pip_path} {cv_packages} --quiet")
    print_styled(" ✔️ Visão Computacional instalada!", "green")

    # 4. Hardware e Matemática
    print_styled("\n🔌 [4/4] Finalizando: Hardware, JAX e Matemática...", "magenta")
    hw_packages = "numpy==1.26.4 jax==0.6.2 jaxlib==0.6.2 scipy==1.15.3 matplotlib==3.10.8 pillow==12.1.0 sounddevice==0.5.3 pyserial==3.5"
    run_command(f"{pip_path} {hw_packages} --quiet")

    print()
    print_styled("-" * 50, "green")
    print_styled("        ✅ AMBIENTE VISION PRONTO PARA USO!       ", "white", "green_bg")
    print_styled("-" * 50, "green")
    print()
    print_styled(" Para ativar agora: ", "white")
    print_styled(" conda activate vision", "cyan")
    print_styled(f" Projeto atual: Wandi Vision System", "yellow")
    print()
    input("Pressione Enter para finalizar...")

if __name__ == "__main__":
    setup_environment()