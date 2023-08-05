from Paperl.Paperui.Widgets.widget import Widget
from typing import Literal

try:
    from tinui import TinUI


    class DWindow(Widget):
        def __init__(self, parent: Widget):
            self.build(parent.Me)

        def build(self, parent: Widget):
            self.Me = TinUI.TinUI(parent)

        def addButton(self, width: int = 100, height: int = 60, text: str = "Button", anchorType="nw",
                      font: tuple[str, int] = ("微软雅黑", 10), command=None,
                      foreground: str = "#000000", background: str = "#CCCCCC",
                      activeForeground: str = "#000000", activeBackground: str = "#999999"):
            me = self.Me.add_button(pos=(width, height), text=text, anchor=anchorType, font=font, command=command,
                                    bg=background, fg=foreground, activebg=activeBackground,
                                    activefg=activeForeground)
            return {"button": me[0], "id": me[4]}

        def addRoundButton(self, width: int = 100, height: int = 60, text: str = "Button", anchorType="nw",
                           font: tuple[str, int] = ("微软雅黑", 10), command=None,
                           foreground: str = "#1b1b1b", background: str = "#fbfbfb",
                           activeForeground: str = "#5d5d5d", activeBackground: str = "#f5f5f5"):
            me = self.Me.add_button2(pos=(width, height), text=text, anchor=anchorType, font=font, command=command,
                                     bg=background, fg=foreground, activebg=activeBackground,
                                     activefg=activeForeground)
            return {"button": me[0], "id": me[4]}

        def addTooltip(self, widget, foreground: str = "#3b3b3b", background: str = "#e7e7e7", borderColor="#e1e1e1",
                       text: str = "Button", delay: int = 0.05,
                       font: tuple[str, int] = ("微软雅黑", 10)):
            me = self.Me.add_tooltip(uid=widget["id"], bg=background, fg=foreground, font=font, text=text, delay=delay,
                                     outline=borderColor)
except:
    pass
