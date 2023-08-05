# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['typingvid']
install_requires = \
['CairoSVG>=2.5.2,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.9.1,<5.0.0',
 'moviepy>=1.0.3,<2.0.0']

entry_points = \
{'console_scripts': ['typingvid = typingvid:main']}

setup_kwargs = {
    'name': 'typingvid',
    'version': '0.1.0',
    'description': 'An open-source, simple but extensible typing animation generator.',
    'long_description': '# Typingvid\n\n![PyPI](https://img.shields.io/pypi/v/typingvid) ![PyPI - Status](https://img.shields.io/pypi/status/typingvid) ![PyPI - Downloads](https://img.shields.io/pypi/dm/typingvid) ![PyPI - License](https://img.shields.io/pypi/l/typingvid)\n\nTypingvid is a command line utility that allows users to quickly generate typing animation videos using different keyboard layouts and themes. To read more about the inner workings of the tool visit https://www.gavalas.dev/projects/typingvid.\n\n## Installation\n\n### Using a package installer\n\n![](https://www.gavalas.dev/assets/images/typingvid/gifs/pipinstall.gif)\n\nThe latest stable version of the script is available on the Python Package Index (PyPI) and can easily be installed using your favorite Python package installer (e.g. pip):\n\n    pip install typingvid\n\nor:\n\n    python3 -m pip install typingvid\n\nTo check If everything went smoothly, you can try running:\n\n    typingvid --help\n\n### From source\n\nAnother option is to clone the entire GitHub repository of the project as follows:\n\n    git clone https://github.com/GavalasDev/typingvid\n    cd typingvid\n    chmod +x typingvid.py\n    ./typingvid.py --help\n\n## Usage\n\nThe standard format of a typingvid command is the following:\n\n    typingvid -t TEXT [-l LAYOUT] [-o OUTPUT] [OPTIONS]\n\nTo see all available options, use:\n\n    typingvid --help\n\nFor example:\n\n    typingvid -t "hello world"\n\nwill generate an animation video using the default layout (en) and store it at the default output location (output.mp4).\n\nThe extension of the `OUTPUT` variable (option `-o`) defines the type of the output file. For example, to generate a simple GIF:\n\n    typingvid -t "lorem ipsum" -o "/path/to/file.gif"\n\nFor more examples, check out the [official page](https://www.gavalas.dev/projects/typingvid/#examples) of the tool.\n\n## License\n\nLicensed under the MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT).\n\n\n## Contribution\n\nUnless you explicitly state otherwise, any contribution intentionally submitted\nfor inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.\n\n',
    'author': 'Konstantinos Gavalas',
    'author_email': 'contact@gavalas.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.gavalas.dev/projects/typingvid',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
