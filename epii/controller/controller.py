from epii.view_model.view_model import ViewModel


class Controller:
    def __init__(self, viewmodel: ViewModel) -> None:
        self.viewmodel = viewmodel

    def update_data(self) -> None:
        self.viewmodel.update_data()
