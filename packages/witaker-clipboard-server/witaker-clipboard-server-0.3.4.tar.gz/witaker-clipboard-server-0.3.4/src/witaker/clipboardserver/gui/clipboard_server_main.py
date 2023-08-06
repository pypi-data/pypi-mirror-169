import argparse
import signal

from witaker.clipboardserver import (
    name,
    version,
    create_flask_app,
    AuthorizedClipboardUtil,
    add_program_arguments,
    if_version_print_version_and_exit,
    get_port_or_default_port,
    get_auth_key_or_generate_auth_key,
    program_version_color,
)
from witaker.clipboardserver.gui import ClipboardServerApp


def signal_handler(signal, frame):
    print(" * CTRL+C detected, exiting ... ")
    exit(1)


def clipboard_server_gui_main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    gui_argument_parser = argparse.ArgumentParser(
        prog="witaker-clipboard-server-gui",
        description="Launch GUI for Witaker Clipboard Server local web service",
        allow_abbrev=True,
        add_help=True,
    )
    add_program_arguments(gui_argument_parser)
    args = gui_argument_parser.parse_args()

    if_version_print_version_and_exit(args)

    port = get_port_or_default_port(args)
    secret_auth_key = get_auth_key_or_generate_auth_key(args)
    print(f" * Initializing GUI for {program_version_color(name, version)}")
    
    gui = ClipboardServerApp(secret_auth_key)
    gui.set_server_port(port)
    gui.run()
    return 0
