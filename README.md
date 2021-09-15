# Avaday

## Application for avatar generation

### (day -> дай == give)

## Linux installation

1. Create and activate virtual environment

   ```sh
   conda create -n TM python=3.7
   conda activate TM
   ```

1. Install this application to [make imports work](https://stackoverflow.com/a/50194143)

   ```sh
   pip install -e .
   ```

1. Install _PyQt6_

    ```sh
    pip install PyQt6
    ```

1. Install pyqtgraph

    ```sh
    pip install pyqtgraph
    ```

1. Install PIL

    ```sh
    pip install pillow
    ```
<!-- 
1. Install PyOpenGL

    ```sh
    pip install PyOpenGL
    ```

1. Install OpenGL

    ```sh
    sudo apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev
    sudo apt-get update
    ``` -->



1. Change library a bit

    We need to fix a bug with camera in GL file, so
    go to *View/app.py*, `Ctrl+Left mouse click` on

    ```python
    GLViewWidget
    ```

    In the line

    ```python
    widget = gl.GLViewWidget()
    ```

    to navigate to `GLViewWidget.py`.

    Find the function

    ```python
    reset()
    ```

    and change lines in it as follows.

    ```python
    self.opts['fov'] = 60                ## horizontal field of view in degrees
    self.opts['elevation'] = 90          ## camera's angle of elevation in degrees
    self.opts['azimuth'] = 0             ## camera's azimuthal angle in degrees 
    ```

## Running on Linux

```sh
python main.py
```
