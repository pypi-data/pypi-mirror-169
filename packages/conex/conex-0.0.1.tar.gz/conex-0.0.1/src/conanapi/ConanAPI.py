from .commands.ConfigSubCommand import ConfigSubCommand
from .commands.EditableSubCommand import EditableSubCommand
from .commands.InspectCommand import InspectCommand
from .commands.UploadCommand import UploadCommand
from .internal.Utilities import Utilities


class ConanAPI:
    def __init__(self):
        self._utilities = Utilities()
        self._config = ConfigSubCommand()
        self._editable = EditableSubCommand()
        self._inspect = InspectCommand()
        self._upload = UploadCommand()

    @property
    def utilities(self):
        return self._config

    @property
    def config(self):
        return self._config

    @property
    def editable(self):
        return self._editable

    @property
    def inspect(self):
        return self._inspect.inspect

    @property
    def upload(self):
        return self._upload.upload
