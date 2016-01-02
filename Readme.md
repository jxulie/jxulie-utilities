JXULIE-UTILITIES
================

This module provides a set of utilities.

Installation
------------

After downloading and extracting the package, install the module by running
`python setup.py install` from within the extracted package directory. (If you
encounter errors, you may need to run setup with elevated permissions:
`sudo python setup.py install`.)

Library Usage
-------------

Usage of the module is very simple. 

Script Usage
------------

    from jxulie_slice.sliceDict import SLICE_DICT
    test_dict = {"a":5, "b":3, "c":23, "d":234, "e":9}
    print (SLICE_DICT().run(test_dict, 3))


References
----------



License
-------

The package is made available under the terms of the
MIT License.

Copyright © 2009 [jxulie][me]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[me]: http://github.com/jxulie/
[pypi]: http://pypi.python.org/