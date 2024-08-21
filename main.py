import argparse
import os

from src.modify import modify_audio
from src.transcribe import transcribe_audio2json

parser = argparse.ArgumentParser()

parser.add_argument(
    "--file_path", help="Path to audio file. Required", type=str, required=True
)
parser.add_argument(
    "--mode",
    default="modify",
    help="Operating mode (modify/transcribe). Default modify",
    type=str,
)
parser.add_argument(
    "--speed",
    help="New audio file playback speed. Required for modify mode",
    type=float,
)
parser.add_argument(
    "--volume",
    help="Changing the volume. Required for modify mode",
    type=int,
)
parser.add_argument(
    "--on_play", help="Whether to enable audio", default=True, type=bool
)
parser.add_argument(
    "--language",
    help="Language text for transcribe (en/ru). Required for transcribe mode",
    type=str,
)


def main():
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        raise FileNotFoundError(f"File {args.file_path} not exists")

    if not args.file_path.endswith(".wav"):
        raise ValueError("File format not supported")

    if args.mode == "modify" and (args.speed is None or args.volume is None):
        raise ValueError(
            "In file modification mode, the args speed and volume are required"
        )
    elif args.mode == "modify":
        modify_audio(args.file_path, args.speed, args.volume, args.on_play)
        return

    if args.language is None:
        raise ValueError(
            "In file transcribe mode, the args language are required"
        )
    else:
        transcribe_audio2json(args.file_path, args.language)


if __name__ == "__main__":
    main()
