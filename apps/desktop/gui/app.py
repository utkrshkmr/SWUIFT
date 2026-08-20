from __future__ import annotations
import os
import sys
from importlib.metadata import PackageNotFoundError, version
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
APP_DIR: str = os.path.dirname(os.path.abspath(sys.argv[0]))
RESOURCE_DIR: str = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(__file__)))

def _asset_path(name: str) -> str:
    return os.path.join(RESOURCE_DIR, name)

def platform_icon_path() -> str:
    names = (
        ('SWUIFT.icns', 'SWUIFT.png', 'SWUIFT.ico') if sys.platform == 'darwin'
        else ('SWUIFT.ico', 'SWUIFT.png', 'SWUIFT.icns') if sys.platform == 'win32'
        else ('SWUIFT.png', 'SWUIFT.ico', 'SWUIFT.icns')
    )
    return next((_asset_path(name) for name in names if os.path.isfile(_asset_path(name))), '')

try:
    APP_VERSION = version('swuift')
except PackageNotFoundError:
    APP_VERSION = '1.0.0'
try:
    with open(_asset_path('BUILD_INFO'), encoding='utf-8') as handle:
        BUILD_ID = handle.read().strip() or 'development'
except OSError:
    BUILD_ID = os.environ.get('SWUIFT_BUILD_ID', 'development')
_ICON_PATH: str = platform_icon_path()

def run() -> None:
    from .main_window import MainWindow
    app = QApplication(sys.argv)
    app.setApplicationName('SWUIFT')
    app.setOrganizationName('SWUIFT')
    app.setOrganizationDomain('buffalo.edu')
    if os.path.isfile(_ICON_PATH):
        app.setWindowIcon(QIcon(_ICON_PATH))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
