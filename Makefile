ru_transcribe:
	python main.py --file_path=data/ru.wav --mode=transcribe --language=ru

en_transcribe:
	python main.py --file_path=data/eng.wav --mode=transcribe --language=en

ru_modify:
	python main.py --file_path=data/ru.wav --speed=2.0 --volume=10

en_modify:
	python main.py --file_path=data/eng.wav --speed=2.0 --volume=10