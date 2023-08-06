# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opticr', 'opticr.ocr']

package_data = \
{'': ['*']}

install_requires = \
['ocrmypdf>=14.0.0,<15.0.0',
 'pdf2image>=1.16.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pytesseract>=0.3.10,<0.4.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'opticr',
    'version': '0.2.0',
    'description': 'expose a single interface and API to few OCR tools',
    'long_description': '# opticr\n\nPython library to expose a single interface and API to few OCR tools (google vision, Tesseract)\n\n## Install\n### Required binaries available in the $PATH\n#### poppler-utils (pdf2image)\n\n[https://github.com/Belval/pdf2image#how-to-install](https://github.com/Belval/pdf2image#how-to-install)\n\n#### tesseract\n\n[https://tesseract-ocr.github.io](https://tesseract-ocr.github.io/tessdoc/Home.html)\n\n### Install OpticR\n#### With pip\n\n``` shell\npip install opticr\n```\n\n#### With poetry\n\n``` shell\npoetry add opticr\n```\n\nor to get the latest \'dangerous\' version\n\n```\npoetry add  git+https://github.com/lzayep/opticr@main\n```\n\n## Usage\n\n``` python\nfrom opticr import OpticR\n\nocr = OpticR("tesseract")\npathtofile = "test/contract.pdf\npages: list[str] = ocr.get_pages(pathtofile)\n\n```\n\nWith google-vision:\n\n``` python\nfrom opticr import OpticR\n\nocr = OpticR("google-vision", options={"google-vision": {"auth": {"token": ""}}})\n\n# file could come from an URL\npathtofile = "https://example.com/contract.pdf\npages: list[str] = ocr.get_pages(pathtofile)\n\n```\n\nCache the result, if the file as already been OCR return immediatly the previous result.\nResult are stored temporarly in the local storage or shared storage such as Redis.\n``` python\nfrom opticr import OpticR\n\nocr = OpticR("tesseract", options={"cache":\n                         {"backend": "redis", redis: "redis://"}}\n\n# file could come from an URL\npathtofile = "https://example.com/contract.pdf\npages: list[str] = ocr.get_pages(pathtofile, cache=True)\n\n```\n',
    'author': 'lzayep',
    'author_email': 'ec@lza.sh',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
