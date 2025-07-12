# Misky Wav2Lip

Este es un proyecto experimental donde se anima un personaje a partir de una imagen fija usando **Wav2Lip**.

## 🚀 Cómo usarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/shesith/Misky-wav2lip.git

2. Crea un entorno virtual
  python -m venv env39
  env39\Scripts\activate

3. Instala las dependencias:
  pip install -r requirements.txt

4. Ejecuta el script:
  python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face inputs/TU_IMAGEN.jpg --audio inputs/TU_AUDIO.wav

📂 Estructura del proyecto
Misky-wav2lip/
├── inputs/
│   ├── TU_IMAGEN.jpg
│   └── TU_AUDIO.wav
├── checkpoints/
│   └── wav2lip_gan.pth
├── results/
├── inference.py
├── requirements.txt
└── README.md

💡 Recomendaciones

Usa imágenes cuadradas (por ejemplo, 256x256 o 512x512)

Asegúrate de que el audio esté en formato .wav, 44.1 kHz, mono.