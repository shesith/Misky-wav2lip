# Misky Wav2Lip

Este es un proyecto experimental donde se anima un personaje a partir de una imagen fija usando **Wav2Lip**.

## 🚀 Cómo usarlo

1. Clona el repositorio:

   ```bash
   git clone https://github.com/shesith/Misky-wav2lip.git

   ```

2. Crea un entorno virtual
   python -m venv env39
   env39\Scripts\activate

3. Instala las dependencias:
   pip install -r requirements.txt

4. Ejecuta el script:
   python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face inputs/Misky_avatar1.png --audio inputs/input_audio.wav

📂 Estructura del proyecto
Misky-wav2lip/
├── inputs/
│ ├── TU_IMAGEN.jpg
│ └── TU_AUDIO.wav
├── checkpoints/
│ └── wav2lip_gan.pth
├── results/
├── inference.py
├── requirements.txt
└── README.md

💡 Recomendaciones

  Usa imágenes cuadradas (por ejemplo, 256x256 o 512x512)

  Asegúrate de que el audio esté en formato .wav, 44.1 kHz, mono.

📦 Archivos requeridos
  1. Modelo preentrenado de Wav2Lip (wav2lip_gan.pth)
  Para ejecutar correctamente el proyecto, necesitas descargar el modelo preentrenado:

🔗 Descargar wav2lip_gan.pth desde Google Drive
    https://drive.google.com/file/d/123f_V-MqiCH0qL0ArSup-1Hd8p86xPdd/view?usp=sharing

👉 Guarda el archivo dentro de la carpeta checkpoints/ con el nombre exacto:
    checkpoints/wav2lip_gan.pth

Si la carpeta checkpoints no existe, créala manualmente.

2. FFmpeg (requerido para generar el video final)
    Este proyecto requiere que tengas ffmpeg instalado y accesible desde la terminal.

👉 Instalación en Windows:
    Descarga FFmpeg desde: https://drive.google.com/drive/folders/1E_THtLFhMdwHsx2lU72gFPaShX6nAsqm?usp=sharing

Descomprime el archivo ZIP.

Copia la ruta de la carpeta bin, por ejemplo:
C:\ffmpeg\bin

Agrega esa ruta a las Variables de Entorno del sistema:

Panel de control > Sistema > Configuración avanzada del sistema > Variables de entorno > Editar Path > Nuevo > Pega la ruta

Abre una nueva terminal y ejecuta para asegurarte que se encuentra:
ffmpeg -version
