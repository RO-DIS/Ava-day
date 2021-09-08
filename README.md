# Avaday

## Application for avatar generation

### (day -> дай == give)

## Linux installation

### Install _PyQt6_

```sh
$ sudo apt install PyQt6
```

### Install pyqtgraph

```sh
$ sudo apt install pyqtgraph
```

### Install PyOpenGL

```sh
$ pip install PyOpenGL
```


### Install OpenGL

```sh
$ sudo apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev
$ sudo apt-get update
```

### Change library a bit

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
$ python main.py
```
