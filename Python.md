---
title: 'Python'
author: 'ju'
date: \today
bibliography: literatur-kfz.bib 
csl: zitierstil-number.csl
---
<!--update 11-8-23 Python-->

# Python


**Anaconda-Installation**

```
# Aktualisieren von Conda
conda update conda
# Aktualisieren aller Pakete
conda update --all
# Installieren des Anaconda Metapakets (optional):
conda install anaconda
# aktualisieren
conda update anaconda
```

**Shell-Konfigurationsdatei**

```
# .bashrc, .bash_profile, .zshrc
unalias python
# Python-Pfad - Python-Interpreter in Anaconda-Umgebung
which python
# Überprüfe die Python-Version
python3 --version
pip3 --version
```

**Anaconda-Umgebung**

```
# Erstelle eine neue Anaconda-Umgebung (optional, aber empfohlen):
conda create --name kfz_db_env python=3.11
# Anaconda-Umgebung aktivieren: 
# conda activate base
conda activate kfz_db_env
# Liste der installierten Pakete anzeigen
conda list
# Suche nach einem spezifischen Paket
conda list | grep PyQt5
# Installiere die benötigte Software
conda install pyqt
#pip install PyQt5

# Skript ausführen
python3 kfz_datenbank.py

# Deaktivieren einer Anaconda-Umgebung
conda deactivate
```

**Test grafische Benutzeroberfläche (GUI)**

`python3 name_script.py`

```
# Test GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Testfenster')
window.show()
sys.exit(app.exec_())
```