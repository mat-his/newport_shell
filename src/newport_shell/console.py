import usb
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import ValidationError, Validator

from newport_shell.command_parser import CommandParser
from newport_shell.utils import check_ids

FINDER_COMMANDS = ['open', 'list', 'exit']
NEWFOCUS_ID_VENDOR = 0x104d


class FindDeviceValidator(Validator):

    def validate(self, document):
        text = document.text
        if text.split(' ')[0] not in FINDER_COMMANDS:
            raise ValidationError(message="Allowed commands: "
                                  f"{' / '.join(FINDER_COMMANDS)}")


class ConsoleManager():

    def __init__(self) -> None:
        self._stop_finder = False
        self._closed = False
        self._available_devices = {}

    def list(self) -> None:
        devs = usb.core.find(idVendor=NEWFOCUS_ID_VENDOR)
        self._available_devices = {}
        for dev in devs:
            self._available_devices[dev.device.idProduct] = dev.device.product
            print("Manufacturer:", dev.device.manufacturer)
            print("Device:", dev.device.product)
            print("idVendor:", hex(dev.device.idVendor))
            print("idProduct:", hex(dev.device.idProduct))
            print('==========')

    def exit(self) -> None:
        self._closed = True
        self._stop_finder = True
        exit(0)

    def open(self, *args: str) -> None:
        ids = check_ids(*args, raising=False)
        parser = CommandParser(*ids)
        try:
            parser.connect()
        except ValueError as e:
            print(e)
            # go back to `find` session
            return
        # open `device` session
        self._stop_finder = True
        session = PromptSession()
        device_name = (self._available_devices[ids[1]]
                       if self._available_devices else "NewFocus")
        while not self._closed:
            cmd = session.prompt(f'\n{device_name}> ',
                                 auto_suggest=AutoSuggestFromHistory(),
                                 completer=WordCompleter(['q', 'quit',
                                                          'exit']))
            if cmd.lower() in ['q', 'quit', 'exit']:
                self.exit()
            try:
                if res := parser.command(cmd):
                    print(res)
            except usb.core.USBTimeoutError:
                print(f'ERROR => Invalid {device_name} command')

    def find(self) -> None:
        session = PromptSession()

        while not self._stop_finder:
            cmd = session.prompt('> ',
                                 auto_suggest=AutoSuggestFromHistory(),
                                 validator=FindDeviceValidator(),
                                 validate_while_typing=False,
                                 completer=WordCompleter(FINDER_COMMANDS))
            if not hasattr(self, cmd.split(' ')[0]):
                print('Invalid command')
                continue
            getattr(self, cmd.split(' ')[0])(*cmd.split(' ')[1:])
