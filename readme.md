## Descripción
Transcriptor básico de audio en español.

## Instalación
### 1. Clona el repositorio
```
git clone https://github.com/sosa-marcelo/audio-transcription.git
cd audio-transcription
```

### 2. Crea y activa un entorno virtual
```
python -m venv venv
- Windows: venv\Scripts\activate
- macOS y Linux: source venv/bin/activate
```

### 3. Instala las dependencias:
```
pip install -r requirements.txt
```

### 4. Cómo usarlo
1. Coloca tu archivo MP3 en la carpeta `audio/` con el nombre `audio.mp3`
2. Ejecuta el script: `python3 main.py`
3. Verás la transcripción en la terminal y también se guardará automáticamente en output/transcription.txt.
