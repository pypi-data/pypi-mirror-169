from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Macosx.button import MacButton


class MacCircleButton(MacButton):
    def __init__(self, parent: Widget, text: str = ""):
        self.build(parent.Me, text)

    def build(self, parent, text: str = ""):
        try:
            from tkmacosx.widgets.circlebutton import CircleButton
        except:
            pass
        else:
            self.Me = CircleButton(parent, text=text)

