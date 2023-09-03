import glob
import re
from LanguageProcessing import LanguageProcessing


def read_from_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        string = file.read()
    return string


def get_chapters(pattern, path):
    book = read_from_txt(path)
    chapter_pattern = re.compile(pattern)
    chapters = re.split(chapter_pattern, book)
    return chapters[1:]


def get_from_diary(path):
    filepaths = sorted(glob.glob(path))
    content_list = []
    for filepath in filepaths:
        with open(filepath) as file:
            content = file.read()
        content_list.append(content)
    dates = [filepath.strip(".txt").strip("diary\\") for filepath in filepaths]
    return content_list,dates


def handler():
    chapters = get_chapters("Chapter [0-9]+", "miracle_in_the_andes.txt")
    lang_processor = LanguageProcessing(chapters, "Category", "Value", "Chapter")
    lang_processor.graph_representation(
        "Line Chart with Positivity and Negativity of a book."
    )

    diary_txts,dates = get_from_diary("diary/*.txt")
    dates = [date for date in dates for _ in range(2)]
    lang_processor = LanguageProcessing(diary_txts, "Category", "Value", "Day")
    lang_processor.set_index(dates)
    lang_processor.graph_representation(
        "Line Chart with Positivity and Negativity of a Journal."
    )


if __name__ == "__main__":
    handler()
