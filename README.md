# PX-to-BMP
A .px file is a single line of text data containing RGB color values for each individual pixel.  RGB value pairs are stored within parentheses separated by commas.  The entire file is framed by square brackets.  There are no newline separators in a .px file, so the user must know the expected width of the image in order to wrap the image at that length.  This value can be specified with the "wrap_every" variable.  Without image wrapping at a specified length, the output image will be just 1 pixel tall, with every value pair generating in an unbroken line.<br/>
<br/>
A basic 2x1 resolution image would look like this:<br/>
**[(0.474193, 0.592056, 0.6304299999999999), (0.0, 0.0, 0.698955)]**<br/>
<br/>
A much more complex example of a .px file is provided in this project as "vga.px".<br/>
<br/>
## Dependencies
This project requires that the [Pillow](https://pypi.org/project/pillow/) library is installed.<br/>
You can install it using pip: **python -m pip install --upgrade Pillow**
