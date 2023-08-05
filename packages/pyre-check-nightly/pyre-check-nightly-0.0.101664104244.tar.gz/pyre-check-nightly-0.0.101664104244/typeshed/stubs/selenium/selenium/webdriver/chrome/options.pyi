class Options:
    KEY: str
    def __init__(self) -> None: ...
    @property
    def binary_location(self): ...
    @binary_location.setter
    def binary_location(self, value) -> None: ...
    @property
    def capabilities(self): ...
    def set_capability(self, name, value) -> None: ...
    @property
    def debugger_address(self): ...
    @debugger_address.setter
    def debugger_address(self, value) -> None: ...
    @property
    def arguments(self): ...
    def add_argument(self, argument) -> None: ...
    @property
    def extensions(self): ...
    def add_extension(self, extension) -> None: ...
    def add_encoded_extension(self, extension) -> None: ...
    @property
    def experimental_options(self): ...
    def add_experimental_option(self, name, value) -> None: ...
    @property
    def headless(self): ...
    @headless.setter
    def headless(self, value) -> None: ...
    def set_headless(self, headless: bool = ...) -> None: ...
    def to_capabilities(self): ...
