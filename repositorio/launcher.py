import subprocess
import sys
import os

# Executar o programa em uma janela separada no Windows
if sys.platform.startswith('win'):
    subprocess.Popen(
        [sys.executable, 'main.py'],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
else:
    # Para Linux/Mac, usar um terminal
    subprocess.Popen(['python', 'main.py'])
