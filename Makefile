dependencias:
	python3 install -r requirements.txt
central:
	python3 src/app_servidor_central.py

distribuido:
	python3 src/app_servidor_distribuido.py
