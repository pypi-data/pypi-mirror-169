"""Open all documents in preparation for grading."""

from __future__ import annotations

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error
from win32com.client import constants

from gradedoc import shared


def open_all():
    """Open all documents in preparation for grading."""

    (paths, _) = shared.get_paths()
    for path in paths:
        document = docxrev.Document(path, save_on_exit=False, close_on_exit=False)
        with document:
            # Open the revisions pane.
            document.com.ActiveWindow.View.SplitSpecial = constants.wdPaneRevisions
