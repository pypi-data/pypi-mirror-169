"""Read inline files stored inside another file."""

__version__ = "1.0.0"

import re
import json
import inspect
import yaml
import xml.etree.ElementTree as ET
from typing import Any

class InvalidFormatError(Exception):
    def __init__(self, message = "File doesn't follow the required format.") -> None:
        self.message = message
        super().__init__(self.message)

class WrongExtensionError(Exception):
    def __init__(self, message = "File does not have the proper extension.") -> None:
        self.message = message
        super().__init__(self.message)

class InlineFiles:
    """
    This class allows users to use and interact with "inline files".

    Inline files are files stored inside another file, as comments.
    This is an example of two inline files inside a Python file:
    ```
    def hello_world():
        print("Hello World!")

    r\"\"\"ILF
    __ID1__
    Hello World!
    __ID2__
    def ping():
        return "pong"
    __ID3:json__
    {
        "hello": "world"
    }
    \"\"\"
    ```

    The comment/docstring used to store these inline files is denoted by the tag "ILF" after the opening quotes, and each inline file is prefixed by a line containing two sets of underscores, along with the file's title. In this example, there are three inline files, "ID1", "ID2" and "ID3". The third file has an optional extension, which allows for it to be opened and read as a JSON file. Supported extensions are "json", "xml", and "yaml".

    The constructor allows for a file to be specified, but the default behavior is to open the file which imports and instantiates the class.

    An instance of this class can be used to fetch an inline file by its name through the method `get_file(file_id)`.

    From the previous example, by adding the following lines to the file:
    ```
    from inline_files import InlineFiles

    ilf = InlineFiles()
    f = ilf.get_file("ID1")
    print("File ID1: " + f)
    ```

    The expected output would be:

    `File ID1: Hello World!`
    """
    def __init__(self, file : str = None) -> None:
        """
        `file` : str, optional
            The file from which inline files will be read. Defaults to the file where the class is used.
        """
        
        self._files = dict()
        self._extensions = dict()
        
        if not file: file = inspect.stack()[1].filename

        with open(file, encoding="UTF-8") as f:
            content = f.read()
            ilf = re.search(r"(?P<quote>[\"']{3})ILF(.*?)(?P=quote)", content, re.DOTALL)
            if ilf:
                for fid, extension, text in re.findall(r"__(\w+)(:[a-z]+)?__\n(.*?)(?=__\w+(?::[a-z]+)?__|\Z)", ilf.group(2), re.DOTALL):
                    self._files[fid] = text
                    if extension not in ("", ":"):
                        self._extensions[fid] = extension.lstrip(":")
            else:
                raise InvalidFormatError

    def get_file(self, file_id : str, raw = False) -> str | None:
        """Returns the content of the inline file specified by `file_id`, or `None` if the inline file does not exist. If the file has a compatible extension, the method returns the file as a structure, which depends on the extension.
        
        ### Arguments
        `file_id` : str
            The inline file's ID.
        `raw` : bool, optional
            If the inline file has an extension, setting this parameter to "True" returns the file's contents as a string.
        """
        if raw:
            return self._files.get(file_id)
            
        match self.get_extension(file_id):
            case "json":
                return self.get_json(file_id)
            case "yaml":
                return self.get_yaml(file_id)
            case "xml":
                return self.get_xml(file_id)
            case _:
                return self._files.get(file_id)

    def get_extension(self, file_id : str) -> str | None:
        """Returns the extension of the inline file specified by `file_id`, or `None` if the inline file does not exist or does not have an extension.
        
        ### Arguments
        `file_id` : str
            The inline file's ID.
        """
        return self._extensions.get(file_id)

    def get_json(self, file_id : str) -> Any:
        """Attempts to return an internal representation of the JSON file specified by `file_id`. Raises an exception if the file does not exist or is not a JSON file.
        
        ### Arguments
        `file_id` : str
            The inline file's ID.
        """
        if file_id in self._files:
            if self._extensions.get(file_id) == "json":
                return json.loads(self._files[file_id])
            else:
                raise WrongExtensionError()
        else:
            raise FileNotFoundError("Inline file does not exist")

    def get_yaml(self, file_id : str) -> Any:
        """Attempts to return an internal representation of the YAML file specified by `file_id`. Raises an exception if the file does not exist or is not a YAML file.
        
        ### Arguments
        `file_id` : str
            The inline file's ID.
        """
        if file_id in self._files:
            if self._extensions.get(file_id) == "yaml":
                return yaml.safe_load(self._files[file_id])
            else:
                raise WrongExtensionError()
        else:
            raise FileNotFoundError("Inline file does not exist")

    def get_xml(self, file_id : str) -> Any:
        """Attempts to return an internal representation of the XML file specified by `file_id`. Raises an exception if the file does not exist or is not a XML file.
        
        ### Arguments
        `file_id` : str
            The inline file's ID.
        """
        if file_id in self._files:
            if self._extensions.get(file_id) == "xml":
                return ET.fromstring(self._files[file_id])
            else:
                raise WrongExtensionError()
        else:
            raise FileNotFoundError("Inline file does not exist")