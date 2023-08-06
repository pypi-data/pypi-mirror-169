from contextlib import contextmanager

import pywintypes

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error
import fire

from gradedoc.add_template_comments import add_template_comments
from gradedoc.close_all import close_all
from gradedoc.copy_example import copy_example
from gradedoc.delete_all_comments import delete_all_comments
from gradedoc.open_all import open_all
from gradedoc.save_all import save_all
from gradedoc.toggle_active_review_pane import toggle_active_review_pane
from gradedoc.update_active_grade import update_active_grade
from gradedoc.update_all_grades import update_all_grades


def main():
    with word():
        try:
            fire.Fire(
                {
                    "example": copy_example,
                    "active": update_active_grade,
                    "all": update_all_grades,
                    "addcom": add_template_comments,
                    "open": open_all,
                    "save": save_all,
                    "close": close_all,
                    "delcom": delete_all_comments,
                    "pane": toggle_active_review_pane,
                }
            )
        except pywintypes.com_error as error:
            raise TypeError(
                "Cannot access the document. Save the document, close it,\n"
                "then re-open it and try again."
            ) from error


@contextmanager
def word():
    try:
        yield
    finally:
        try:
            docxrev.quit_word_safely()  # If used as a CLI, quit Word if nothing was open
        except pywintypes.com_error as error:
            raise TypeError(
                "Cannot access the document. Save the document, close it,\n"
                "then re-open it and try again."
            ) from error
