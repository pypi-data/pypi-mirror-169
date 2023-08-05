# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quadrantic']

package_data = \
{'': ['*']}

install_requires = \
['Shapely>=1.8.4,<2.0.0']

setup_kwargs = {
    'name': 'quadrantic',
    'version': '0.1.0',
    'description': 'Determination of quadrants based on angle, coordinates and others',
    'long_description': 'quadrantic\n##########\n\nDetermination of quadrants based on angle, coordinates and others\n\nOverview\n********\n\nThis library allows you to determine quadrant(s) based on\n\n- angle (360° or 400 Gon)\n- location (latlon)\n\nSetup\n*****\n\nVia Pip:\n\n.. code-block:: bash\n\n    pip install quadrantic\n\nVia Github (latest):\n\n.. code-block:: bash\n\n    pip install git+https://github.com/earthobservations/quadrantic\n\nImplementations\n***************\n\nGet quadrant for angle\n======================\n\nDetermine quadrant based on\n\nDegree\n\n.. code-block::\n\n    #####################\n    #         # 90°     #\n    #         #         #\n    # 180°    #      0° #\n    #####################\n    #         #         #\n    #         #         #\n    #         # 270°    #\n    #####################\n\nor\n\nGon\n\n.. code-block::\n\n    #####################\n    #         # 100°    #\n    #         #         #\n    # 200°    #      0° #\n    #####################\n    #         #         #\n    #         #         #\n    #         # 300°    #\n    #####################\n\n.. code-block:: python\n\n    from quadrantic import QuadrantFromAngle, AngleUnit, Q\n\n    quad = QuadrantFromAngle() # no args need for this method\n\n    # Single quadrant\n    quad.get(45.0, AngleUnit.DEGREE)\n    # [Q.FIRST]\n\n    # Two quadrants\n    quad.get(90.0, AngleUnit.DEGREE)\n    # [Q.FIRST, Q.SECOND]\n\n    # More then full circle (360°)\n    quad.get(450.0, AngleUnit.DEGREE) # same as above + 360°\n    # [Q.FIRST, Q.SECOND]\n\n    # Negative degree\n    quad.get(-45.0, AngleUnit.DEGREE)\n    # [Q.FOURTH]\n\n    # Degree in Gon\n    quad.get(90.0, AngleUnit.GON)\n    # [Q.FIRST]\n\nGet quadrant for coordinates\n============================\n\n.. code-block::\n\n    #####################\n    # (-1,1)  #   (1,1) #\n    #         #         #\n    #         # (0,0)   #\n    #####################\n    #         #         #\n    #         #         #\n    #         #         #\n    #####################\n\n.. code-block:: python\n\n    from quadrantic import QuadrantFromCoords, AngleUnit, Q\n    from shapely.geometry import Point\n\n    # Single quadrant\n    quad = QuadrantFromCoords((0.0, 0.0))\n    quad.get((1.0, 1.0))\n    # [Q.FIRST]\n\n    # Two quadrants\n    quad = QuadrantFromCoords((0.0, 0.0))\n    quad.get((0.0, 1.0))\n    # [Q.FIRST, Q.SECOND]\n\n    # All quadrants\n    quad = QuadrantFromCoords((0.0, 0.0))\n    quad.get((0.0, 0.0))\n    # [Q.FIRST, Q.SECOND, Q.THIRD, Q.FOURTH]\n\n    # Single quadrant with shapely Point\n    quad = QuadrantFromCoords(Point(0.0, 0.0))\n    quad.get(Point(1.0, 1.0))\n    # [Q.FIRST]\n\nExamples\n********\n\nVisualized examples can be found in the ``examples`` folder.\n\nLicense\n*******\n\nDistributed under the MIT License. See ``LICENSE.rst`` for more info.\n\nChangelog\n*********\n\nDevelopment\n===========\n\n0.1.0 (25.09.2022)\n==================\n\n- Add first version of quadrantic\n',
    'author': 'Benjamin Gutzmann',
    'author_email': 'gutzemann@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/earthobservations/quadrantic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
