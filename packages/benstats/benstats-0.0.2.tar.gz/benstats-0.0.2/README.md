# benstats
A Python package for calculating Benford's Law statistics on images

[![PyPI - Version](https://img.shields.io/pypi/v/benstats.svg)](https://pypi.org/project/benstats)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/benstats.svg)](https://pypi.org/project/benstats)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install benstats
```

## Usage

### Importing the package

```python
import benstats
```

### Read an image
```python 
image = benstats.read("path/to", "image.png")
```
Supported image formats: bmp, dib, jpeg, jpg, jpe, jp2, png, webp, pbm, pgm, ppm, pxm, pnm, sr, ras, tiff, tif, exr, hdr, pic

### Calculate Benford's Law statistics
```python
benstats.benstats(image, channels=['rgb', 'gray'], scale=1, min=0, max=255)
```
- `channels`: list of channels to calculate statistics for. Possible values: `rgb`, `hsv`, `gray`, `lab`, `luv`, `xyz`, `ycbcr`
- `scale`: scale factor for the image. If `scale` is less than 1, the image will be downsampled. If `scale` is greater than 1, the image will be upsampled.
- `min`: new range min to map pixel values into. Default: 0
- `max`: new range max to map pixel values into. Default: 255

Returns a dictionary of channelwise statistics.

### Plotting Benford's Law statistics
```python
benstats.benplot(image, channels=['rgb'], scale=1, min=0, max=255)
```
Same parameters as above.

## License

`benstats` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

-----
Built by @gv-sh @bhaumikdebanshu