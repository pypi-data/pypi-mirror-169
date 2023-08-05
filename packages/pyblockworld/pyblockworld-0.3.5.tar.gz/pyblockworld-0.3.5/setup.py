# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyblockworld']
install_requires = \
['pyglet>=1.5.26,<2.0.0']

setup_kwargs = {
    'name': 'pyblockworld',
    'version': '0.3.5',
    'description': 'Minecraft like block world in Python',
    'long_description': '# PyBlockWorld\n\nEine an Minecraft angelehnte Welt aus Blöcken.\n\n## Installation\n\nDie Installation erfolgt über ``pip install pyblockworld``.\n\n## Start\n\nNach der Installation kann die Welt mit ``python -m pyblockworld`` gestartet\nwerden.\n\n## API\n\n```python\n    from pyblockworld import World\n\n    #\n    # BEISPIEL 1\n    #\n    \n    # Eine Funktion, die beim Drücken der B-Taste aufgerufen werden soll\n    def b_key_pressed(world:World):\n        print("B pressed. Player at", world.player_position())\n        \n    # Erstellen einer neuen Welt\n    world = World()\n    # Die Funktion für die build-Taste (b) wird zugewiesen\n    world.build_key_pressed = b_key_pressed\n    # Die Welt wird gestartet\n    world.run()\n\n    #\n    # BEISPIEL 2\n    #\n\n    # Nun werden beim Drücken der Taste ein paar Blöcke platziert.\n    def b_key_pressed(world:World):\n        # Neue Blöcke können mit setBlock gesetzt werden.\n        # Verfügbare Materialien stehen in World.MATERIALS und umfassen\n        # air, default:brick, default:stone, default:sand, default:grass\n        print("Block types", World.MATERIALS)\n        x,y,z = world.player_position()\n        # Einen Block platzieren\n        world.setBlock(x,y,z, "default:brick")\n\n        # Mehrere Blöcke auf einmal abseits des Spielers platzieren\n        x,y,z = x,y,z+3\n        world.setBlocks(x,y,z, x+3,y+3,z+3, "default:grass")\n        \n    world = World()\n    world.build_key_pressed = b_key_pressed\n    world.run()\n```\n\n## Quellen\n\nDer Quellcode basiert auf dem Code von [SensorCraft](https://github.com/AFRL-RY/SensorCraft),\nder wiederum auf dem Code von [Craft](https://github.com/fogleman/Craft/) basiert.\n\n\n## Changelog\n\n* 3.5.4 \n  * Changelog eingeührt\n  * Support für Python 3.8\n\n  ',
    'author': 'Marco Bakera',
    'author_email': 'marco@bakera.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
