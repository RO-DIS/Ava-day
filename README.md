# Avaday

## Application for avatar generation

### (day -> дай == give)

## Linux installation

1. Open terminal in some folder and clone the project

   ```sh
   git clone https://github.com/RO-DIS/Ava-day
   ```

1. Open terminal in the project root folder

   ```sh
   cd Ava-day
   ```

1. [Install Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

1. Create and activate a new virtual environment

   ```sh
   conda create -n Avaday python=3.7
   conda activate Avaday
   ```

1. Install all necessary packages, including [this application](https://stackoverflow.com/a/50194143).

    ```sh
    pip install -e . PyQt6 pyqtgraph pyopengl pillow
    ```

## Running on Linux

1. Continue in the same terminal. Run application

    ```sh
    python main.py
    ```

2. Drag'n'drop an image into app window

3. Do you see a big window with black background? Try to change the view with your mouse or touchpad!

   - Click and hold the left mouse button, then move the mouse to change the view. 

   - You can also scroll your mouse wheel to zoom in or out.

4. When you have found a cool view, click on `Save as` button to choose where to save your avatar.

5. Type some `name.png`, choose a folder, and click on `Save`. Ta-da!
