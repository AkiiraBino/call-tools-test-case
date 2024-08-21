import json
import wave

from loguru import logger
from vosk import KaldiRecognizer, Model


def transcribe_audio2json(file_path: str, language: str) -> None:
    if language == "ru":
        language = "russian"
        model = Model("models/vosk-model-small-ru-0.22")
    elif language == "en":
        language = "english"
        model = Model("models/vosk-model-small-en-us-0.15")
    else:
        raise ValueError(f"Language {language} not invalid")

    wf = wave.open(file_path, "rb")
    recognizer = KaldiRecognizer(model, wf.getframerate())

    result_text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            result_text += result.get("text", "") + " "

    final_result = json.loads(recognizer.FinalResult())
    result_text += final_result.get("text", "")

    log_data = {
        "file": file_path,
        "language": language,
        "transcription": result_text.strip(),
    }

    log_file = file_path + ".json"
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=4)

    logger.info(f"Распознанный текст сохранен в файл: {log_file}")
