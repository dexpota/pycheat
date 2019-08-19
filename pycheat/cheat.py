from sys import stdin
from yaml import load, FullLoader
from pygments.lexers.shell import BashLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

def humanize(cheat):
    """
    Renders a human readable cheat.
    """
    description = cheat["description"]
    command = cheat["command"]

    print(description)
    print()
    print("\t" + highlight(command, BashLexer(), TerminalFormatter()))
    print()


def select(cheat):
    #command = cheat["command"]

    buffer1 = Buffer()

    kb = KeyBindings()

    @kb.add('c-q')
    def exit_(event):
        """
        Pressing Ctrl-Q will exit the user interface.

        Setting a return value means: quit the event loop that drives the user
        interface and return this value from the `Application.run()` call.
        """
        event.app.exit()

    root_container = VSplit([
        # One window that holds the BufferControl with the default buffer on
        # the left.
        Window(content=BufferControl(buffer=buffer1)),

        # A vertical line in the middle. We explicitly specify the width, to
        # make sure that the layout engine will not try to divide the whole
        # width by three for all these windows. The window will simply fill its
        # content by repeating this character.
        Window(width=1, char='|'),

        # Display the text 'Hello world' on the right.
        Window(content=FormattedTextControl(text='Hello world')),
    ])

    layout = Layout(root_container)

    app = Application(key_bindings=kb, layout=layout, full_screen=True)

    app.run()

    lexer = BashLexer()
    tokens = list(lexer.get_tokens(command))

    print_formatted_text(PygmentsTokens(tokens))
    pass


if __name__ == "__main__":
    select(None)
    #list(map(select, load(stdin, Loader=FullLoader)["cheats"]))
