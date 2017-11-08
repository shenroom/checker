set PYTHONPATH=D:\develop\SoftwareRepo\python\2.7.3\Lib\site-packages
set PATH=D:\develop\SoftwareRepo\python\2.7.3\Lib\site-packages\PySide;%PATH%

pyside-uic core\resources\check_dialog.ui -o core\ui\check_dialog.py
pyside-uic core\resources\check_item_widget.ui -o core\ui\check_item_widget.py
pyside-rcc core\resources\resources.qrc -o core\ui\resources_rc.py
pause
