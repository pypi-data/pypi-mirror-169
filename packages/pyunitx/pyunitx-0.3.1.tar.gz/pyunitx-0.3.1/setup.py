# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyunitx']

package_data = \
{'': ['*']}

install_requires = \
['sigfig>=1.3.2,<2.0.0']

setup_kwargs = {
    'name': 'pyunitx',
    'version': '0.3.1',
    'description': 'First-class manipulation of physical quantities',
    'long_description': '# Units\n\n[![Coverage Status](https://coveralls.io/repos/github/the-nick-of-time/units/badge.svg?branch=main)](https://coveralls.io/github/the-nick-of-time/units?branch=main)\n[![Documentation Status](https://readthedocs.org/projects/pyunitx/badge/?version=latest)](https://pyunitx.readthedocs.io/en/latest/?badge=latest)\n\nWhen doing calculations using physical measurements, it\'s all too easy to forget to account for\nunits. This can result in problems when you find you\'ve been adding kilograms to newtons and\nyour calculation is off by a factor of ten.\n\nThis library uses the standard library `decimal.Decimal` for all calculations to avoid most\nfloating-point calculation pitfalls. Values given are automatically converted so you can enter\nany value that constructor can take. Functionally, this means that float notation should be\ngiven as strings rather than float literals.\n\nQ. How many meters does light travel in a millisecond?\n\n```pycon\n>>> from pyunitx.time import seconds\n>>> from pyunitx.constants import c\n>>> \n>>> (c * seconds("1e-3")).sig_figs(5)\n2.9979E+5 m\n\n```\n\nQ. What is that in feet?\n\n```pycon\n>>> from pyunitx.time import seconds\n>>> from pyunitx.constants import c\n>>> \n>>> (c * seconds("1e-3")).to_feet().sig_figs(5)\n9.8357E+5 ft\n\n```\n\nQ. How fast is someone on the equator moving around the center of the earth?\n\n```pycon\n>>> from pyunitx.time import days\n>>> from pyunitx.constants import earth_radius\n>>> from math import pi\n>>> \n>>> circumference = 2 * pi * earth_radius\n>>> (circumference / days(1)).to_meters_per_second().sig_figs(3)\n464 m s^-1\n\n```\n\nQ. What\'s the mass of air in one of your car tires, if the inner radius is 6 inches, the outer\nradius is 12.5 inches, the width is 8 inches, and it\'s filled to 42 psi?[^1]\n\n[^1]: No, I don\'t write homework problems.\n\n```pycon\n>>> from pyunitx.length import inches\n>>> from pyunitx.pressure import psi\n>>> from pyunitx.constants import R, air_molar_mass\n>>> from pyunitx.temperature import celsius, celsius_to_kelvin_absolute\n>>> from math import pi\n>>> \n>>> volume = (pi * inches(8) * (inches("12.5") ** 2 - inches(6) ** 2)).to_meters_cubed()\n>>> pressure = psi(42).to_pascals()\n>>> temperature = celsius_to_kelvin_absolute(celsius(25))\n>>> mols = pressure * volume / (R * temperature)\n>>> mass = mols * air_molar_mass\n>>> mass.to_avoirdupois_pounds_mass().sig_figs(3)\n0.369 lbm_A\n\n```\n\nAll constants like `R` are defined in SI base units so you will need to convert your units, but\nas you can see, that task is easy. It\'s just a matter of calling `.to_<other unit>()`. You can\nconvert from any unit to another that measures the same dimension this way. If you\'re going to a\ncomposite unit that hasn\'t been explicitly declared with a name, this is still possible, and the\nlibrary will create a converter for you - you just need to get the name right. The name format\nis as intuitive as possible, as you can see with the above examples.\n\nA name is made of the names of the base units, suffixed with `_squared`, `_cubed`, etc. to\nrelate the size of the exponent and prefixed by `per_` if the exponent is negative. Units with\nnegative exponents are made singular[^2] to follow how you would say it.\n\n[^2]: Naively; it\'s done by just stripping off a trailing \'s\' if there is one.\n\nSome examples of the most complicated possible situations will be illustrative.\n\n```pycon\n>>> from pyunitx.constants import gas_constant, stefan_boltzmann\n>>> print(gas_constant.to_feet_pounds_per_mole_per_rankine().sig_figs(4))\n3.407 ft^2 slug mol^-1 °R^-1 s^-2\n\n>>> print(stefan_boltzmann.to_horsepower_per_feet_squared_per_rankine_to_the_fourth().sig_figs(5))\n3.7013E-10 slug s^-3 °R^-4\n\n```\n\nYou will notice that the output will have all units broken down to their bases. It is guaranteed\nto be equivalent.\n\n',
    'author': 'Nick Thurmes',
    'author_email': 'nthurmes@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
