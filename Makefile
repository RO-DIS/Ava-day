VENV = env
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip3

run: $(VENV)/bin/activate
	$(PYTHON) main.py

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)