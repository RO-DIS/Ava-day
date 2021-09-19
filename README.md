# Avaday

## Application for avatar generation

### (day -> дай == give)

## Linux installation

1. Open terminal in the project root folder

2. Create and activate virtual environment

   ```sh
   conda create -n Avaday python=3.7
   conda activate Avaday
   ```

3. Install this application to [make imports work](https://stackoverflow.com/a/50194143)

   ```sh
   pip install -e .
   ```

4. Install _PyQt6_

    ```sh
    pip install PyQt6
    ```

5. Install pyqtgraph

    ```sh
    pip install pyqtgraph
    ```

6. Install PIL

    ```sh
    pip install pillow
    ```

## Running on Linux

1. In terminal from project root folder

    ```sh
    python main.py
    ```

1. See output in /resources/output_images
