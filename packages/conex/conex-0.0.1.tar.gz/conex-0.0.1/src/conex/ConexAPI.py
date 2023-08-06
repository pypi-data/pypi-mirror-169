from .commands.ConfigSubCommand import ConfigSubCommand
from .commands.EditableSubCommand import EditableSubCommand
from .commands.UploadCommand import UploadCommand
from .internal.Utilities import Utilities
from conanapi import ConanAPI


class ConexAPI:
    config_filename = "conex.toml"

    def __init__(self, conan=ConanAPI()):
        self._config = ConfigSubCommand(conan, ConexAPI.config_filename)
        self._utils = Utilities(conan, self._config)
        self._editable = EditableSubCommand(conan, self._utils, self._config)
        self._upload = UploadCommand(conan, self._utils)

    @property
    def config(self):
        return self._config

    @property
    def editable(self):
        return self._editable

    @property
    def upload(self):
        return self._upload.upload
