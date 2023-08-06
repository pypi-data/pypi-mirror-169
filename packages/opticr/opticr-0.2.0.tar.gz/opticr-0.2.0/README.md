# opticr

Python library to expose a single interface and API to few OCR tools (google vision, Tesseract)

## Install
### Required binaries available in the $PATH
#### poppler-utils (pdf2image)

[https://github.com/Belval/pdf2image#how-to-install](https://github.com/Belval/pdf2image#how-to-install)

#### tesseract

[https://tesseract-ocr.github.io](https://tesseract-ocr.github.io/tessdoc/Home.html)

### Install OpticR
#### With pip

``` shell
pip install opticr
```

#### With poetry

``` shell
poetry add opticr
```

or to get the latest 'dangerous' version

```
poetry add  git+https://github.com/lzayep/opticr@main
```

## Usage

``` python
from opticr import OpticR

ocr = OpticR("tesseract")
pathtofile = "test/contract.pdf
pages: list[str] = ocr.get_pages(pathtofile)

```

With google-vision:

``` python
from opticr import OpticR

ocr = OpticR("google-vision", options={"google-vision": {"auth": {"token": ""}}})

# file could come from an URL
pathtofile = "https://example.com/contract.pdf
pages: list[str] = ocr.get_pages(pathtofile)

```

Cache the result, if the file as already been OCR return immediatly the previous result.
Result are stored temporarly in the local storage or shared storage such as Redis.
``` python
from opticr import OpticR

ocr = OpticR("tesseract", options={"cache":
                         {"backend": "redis", redis: "redis://"}}

# file could come from an URL
pathtofile = "https://example.com/contract.pdf
pages: list[str] = ocr.get_pages(pathtofile, cache=True)

```
