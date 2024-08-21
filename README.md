# Installation
`poetry install`
# Run
`make ru_transcribe` or `python main.py --file_path=data/ru.wav --mode=transcribe --language=ru`

`make en_transcribe` or `python main.py --file_path=data/eng.wav --mode=transcribe --language=en`

`make ru_modify` or `python main.py --file_path=data/ru.wav --speed=2.0 --volume=10`

`make en_modify` or `python main.py --file_path=data/eng.wav --speed=2.0 --volume=10`
# Options
```
  -h, --help            show this help message and exit
  --file_path FILE_PATH
                        Path to audio file. Required
  --mode MODE           Operating mode (modify/transcribe). Default modify
  --speed SPEED         New audio file playback speed. Required for modify mode
  --volume VOLUME       Changing the volume. Required for modify mode
  --on_play ON_PLAY     Whether to enable audio
  --language LANGUAGE   Language text for transcribe (en/ru). Required for transcribe mode
```