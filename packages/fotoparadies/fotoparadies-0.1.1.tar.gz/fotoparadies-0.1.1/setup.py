# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fotoparadies']

package_data = \
{'': ['*']}

install_requires = \
['platformdirs>=2.5.2,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['fotoparadies = fotoparadies.main:app']}

setup_kwargs = {
    'name': 'fotoparadies',
    'version': '0.1.1',
    'description': 'Shows status of fotoparadies orders',
    'long_description': '# Fotoparadies Status Checker 📸⁉️ [![PyPI version](https://badge.fury.io/py/fotoparadies.svg)](https://badge.fury.io/py/fotoparadies)\n\n📝 Der Fotoparadies Status Checker ermöglicht das Überprüfen des aktuellen Status von abgegebenen Fotoaufträgen (beispielsweise im DM).\n\n![](https://github.com/hija/fotoparadies/raw/main/doc/img/01_status.png)\n\n## Installation\nAm einfachsten installierst du das Tool mit pip:\n\n`pip install fotoparadies`\n\nDanach öffnest du ein neues Terminal / CMD / Shell / ... Fenster und kannst den `fotoparadies`-Befehl verwenden.\nBeispiele findest du im folgenden:\n\n## Funktionsweise\n1. **Neue Aufträge hinzufügen**\n   \n    Ein neuer Auftrag wird hinzugefügt, indem das Tool mit `fotoparadies add [Filial-Nummer] [Auftragsnummer] (Name)` aufgerufen wird.\n    Der Parameter Name ist optional, er hilft aber die Aufträge voneinander zu unterscheiden.\n\n    ![](https://github.com/hija/fotoparadies/raw/main/doc/img/00_add.png)\n\n2. **Status der Aufträge anzeigen**\n\n    Den Status der Aufträge, lässt sich mit `fotoparadies status` anzeigen:\n\n    ![](https://github.com/hija/fotoparadies/raw/main/doc/img/01_status.png)\n\n3. **Gelieferte Aufträge löschen**\n   \n   Gelieferte Aufträge (Status "Delivered") lassen sich automatisch mit dem `fotoparadies cleanup` Befehl löschen:\n\n   ![](https://github.com/hija/fotoparadies/raw/main/doc/img/02_cleanup.png)\n\n4. **Auftrag manuell löschen**\n\n    Ein Auftrag lässt sich mit dem `fotoparadies remove [Name]` Befehl manuell löschen. Name ist entweder der in Schritt 1 gesetzter Name oder alternativ die Auftragsnummer.\n\n    ![](https://github.com/hija/fotoparadies/raw/main/doc/img/03_remove.png)\n\n## FAQ\n\n**Q: Wieso ist der Status ERROR?**\n\nA: Der Status ist ERROR, wenn der Auftrag noch nicht im Großlabor angekommen und eingescannt wurde.',
    'author': 'hilko',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hija/fotoparadies',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
