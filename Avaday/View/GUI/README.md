# How to edit GUI

1. Install Qt Designer

    ```sh
    pip install pyqt6-tools
    ```

1. `cd` to the current directory.
1. Open `gui.ui` file in `designer`.

    ```sh
    designer gui.ui
    ```

1. Save to `gui.py`.

   ```sh
   pyuic6 -x gui.ui -o gui.py
   ```

1. Substitute old `class Ui_Dialog(object)` in your main GUI file for the newly generated one.
