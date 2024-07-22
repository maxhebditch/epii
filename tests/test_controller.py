from unittest.mock import Mock

from epii.controller.controller import Controller
from epii.view_model.view_model import ViewModel


def test_get_data_calls_model_get():
    controller = Controller(Mock(spec=ViewModel))
    controller.update_data()
    controller.viewmodel.update_data.assert_called_once()
