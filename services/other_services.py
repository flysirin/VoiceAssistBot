from pathlib import Path
import textwrap


def delete_temp_files(path: str = "temp") -> None:
    folder = Path(path)
    for file in folder.glob("*"):
        if file.is_file() and file.name != ".gitignore":
            try:
                file.unlink()
            except BaseException as e:
                print(f"File '{file}', can not delete. \n{e}")


def split_text(text: str, max_length: int = 4000) -> list[str]:
    wrapped_text = textwrap.wrap(text=text, width=max_length, break_long_words=False)
    return wrapped_text
