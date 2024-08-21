import os
from datetime import datetime
from pathlib import Path

from loguru import logger
from pydub import AudioSegment
from pydub.playback import play


def modify_audio(
    file_path: str | Path,
    speed: float = 1.0,
    volume_change: int = 0,
    on_play: bool = True,
) -> None:
    audio = AudioSegment.from_file(file_path)

    new_sample_rate = int(audio.frame_rate * speed)
    audio = audio._spawn(
        audio.raw_data, overrides={"frame_rate": new_sample_rate}
    )
    audio = audio.set_frame_rate(audio.frame_rate)

    audio = audio + volume_change

    fp_list = [
        "data/modified",
        str(datetime.now()),
        os.path.basename(file_path),
    ]
    output_path = "_".join(fp_list)

    logger.info(f"Modify file saved: {output_path}")
    audio.export(output_path)
    if on_play:
        play(audio)
