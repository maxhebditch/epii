import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

from epii.model import Model
from epii.notes.note import notes
from epii.view import View
from epii.view_model import ViewModel


def generate_app() -> QApplication | QCoreApplication:
    app = QApplication.instance()
    if app is None:
        app = QApplication()

    return app


def get_model() -> Model:
    return Model(notes)


def main() -> None:
    app = generate_app()
    model = get_model()
    viewmodel = ViewModel(model)
    view = View(viewmodel)
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  # pragma: no cover
