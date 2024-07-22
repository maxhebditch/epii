from unittest.mock import MagicMock, patch

import pytest
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from epii.main import generate_app
from epii.main import main as main_module


@pytest.fixture
def app():
    if not QApplication.instance():
        app = QApplication()
    else:
        app = QApplication.instance()
    return app


def test_generate_app():
    app = generate_app()
    assert isinstance(app, QApplication)


def test_main_with_existing_app(app):
    with patch("epii.main.sys") as sys_mock:
        QTimer.singleShot(100, app.instance().quit)

        main_module()
        assert sys_mock.exit.called


def test_main_without_existing_app():
    with (
        patch("epii.main.sys") as sys_mock,
        patch("epii.main.QApplication") as app_mock,
    ):
        QTimer.singleShot(100, app_mock.return_value.instance().quit)

        main_module()
        assert sys_mock.exit.called


def test_main_with_exception():
    with (
        patch("epii.main.sys") as sys_mock,
        patch("epii.main.QApplication") as app_mock,
    ):
        app_mock.side_effect = Exception("Failed to create QApplication")

        main_module()
        assert sys_mock.exit.called


def test_viewmodel_initialization():
    with (
        patch("epii.main.sys"),
        patch("epii.main.ViewModel") as mock_view_model,
        patch("epii.main.Model", new_callable=MagicMock) as mock_model,
        patch("epii.main.Controller", new_callable=MagicMock),
        patch("epii.main.View", new_callable=MagicMock),
    ):
        model_instance = mock_model.return_value

        app = generate_app()
        QTimer.singleShot(100, app.quit)

        main_module()

        mock_view_model.assert_called_once_with(model_instance)


def test_controller_initialization():
    with (
        patch("epii.main.sys"),
        patch("epii.main.Controller") as mock_controller,
        patch("epii.main.ViewModel", new_callable=MagicMock) as mock_view_model,
        patch("epii.main.Model", new_callable=MagicMock),
        patch("epii.main.View", new_callable=MagicMock),
    ):
        viewmodel_instance = mock_view_model.return_value

        app = generate_app()
        QTimer.singleShot(100, app.quit)

        main_module()

        mock_controller.assert_called_once_with(viewmodel_instance)


def test_view_initialization():
    with (
        patch("epii.main.sys"),
        patch("epii.main.View") as mock_view,
        patch("epii.main.Controller", new_callable=MagicMock) as mock_controller,
        patch("epii.main.ViewModel", new_callable=MagicMock) as mock_view_model,
        patch("epii.main.Model", new_callable=MagicMock),
    ):
        controller_instance = mock_controller.return_value
        viewmodel_instance = mock_view_model.return_value

        app = generate_app()
        QTimer.singleShot(100, app.quit)

        main_module()

        mock_view.assert_called_once_with(controller_instance, viewmodel_instance)


def test_qapplication_singleton_behavior():
    app1 = generate_app()
    app2 = generate_app()
    assert app1 is app2
