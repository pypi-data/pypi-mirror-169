import reacton as react
from reacton import ipywidgets as w


@react.component
def MyApp1():
    value, set_value = react.use_state(True)
    with Container() as main:
        if value:
            w.Button(description="button")
        else:
            w.IntSlider(description="slider")
    return main


app = MyApp()


@react.component
def Container(children=[]):
    return w.HBox(children=children)


@react.component
def MyApp():
    value, set_value = react.use_state(True)

    def toggle():
        set_value(not value)

    if value:
        button1 = w.Button("b1", on_click=toggle)
        button1 = w.Button("b2", on_click=toggle)
    else:
        button1 = w.Button("s1", on_click=toggle)
        button2 = button1
    return Container(children=[button1, button2])


app = MyApp()
