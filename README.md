# Avaday

## Application for avatar generation

### (day -> дай == give)

## Linux installation

1. [Install Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

2. Open terminal in the project root folder

3. Create and activate a new virtual environment

   ```sh
   conda create -n Avaday python=3.7
   conda activate Avaday
   ```

4. Install this application to [make imports work](https://stackoverflow.com/a/50194143)

   ```sh
   pip install -e .
   ```

5. Install _PyQt6_

    ```sh
    pip install PyQt6
    ```

6. Install pyqtgraph

    ```sh
    pip install pyqtgraph
    ```

7. Install pyopengl

    ```sh
    pip install pyopengl
    ```

8. Install PIL

    ```sh
    pip install pillow
    ```

## Running on Linux

1. In terminal from project root folder

    ```sh
    python main.py
    ```

1. Drag'n'drop an image into app window

1. Do you see a big window with black background?

   Click and hold the left mouse button, then move the mouse to change the view.

   The mini-view in the main window will update too! This is how a little avatar will look like.

1. When you have found a cool view, click on `Save as` button to choose where to save your avatar.

1. Type some `name.png` and click on `Save`. Ta-da!