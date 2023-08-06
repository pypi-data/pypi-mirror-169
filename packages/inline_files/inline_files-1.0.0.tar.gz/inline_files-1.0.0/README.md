# Inline Files

This Python package allows us to read and interact with *inline files*.

An inline file is a file stored within another file. This parent file can be any kind of file, but a .py file is preferred due to how an inline file is defined.

## Definition

We use the following syntax to define an inline file:

```py
r"""ILF
__ID1__
Hello World!
__ID2:json__
{
    "hello": "world"
}
"""
```

In other words, an inline file must be defined inside a multiline comment, or docstring, and must be preceded by `__[ID]__`, where `[ID]` is the inline file's name. In the example above, there are two inline files, "ID1" and "ID2", with "ID2" having an optional extension.

If an inline file is defined with an extension, the file will be read according to that extension. For example, a JSON file will be processed using the `json` module. Files without an extension are treated as text files. Currently, the module supports `json`, `yaml` and `xml` extensions. Below is another example of an inline file with an extension.

```py
r"""ILF
__file1:yaml__
filename: file1
extension: yaml
```

## Module

The module contains a constructor responsible for reading a file and extracting its inline files. By default, this file will be the file that calls the constructor, but another file can be specified.

The module's main method, `get_file()`, will return an inline file's contents, which can be a string or a structure, if the file has one of the supported extensions.

There is also a `get_extension()` method, used to retrieve an inline file's extension.

## Usage example

```py
from inline_files import InlineFiles

ilf = InlineFiles()

i = ilf.get_file("ID1")

print(i)

r"""ILF
__ID1__
Hello World!
__ID2__
def ping():
    return "pong"
"""
```

### Usage example with extensions

```py
from inline_files import InlineFiles

ilf = InlineFiles()

j = ilf.get_json("J")

print(j["filename"])

r"""ILF
__J:json__
{
    "filename": "J",
    "extension": "json"
}
"""
```