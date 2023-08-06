from typing import Callable, Generic, TypeVar
from dash import Dash, html, dcc, Input, Output
import reacton as react
from reacton.core import ComponentFunction, ComponentWidget
from dash.development.base_component import Component


W = TypeVar("W")  # used for widgets
T = TypeVar("T")  # used for widgets


def snake_to_setter(name):
    parts = name.split("_")
    name = "".join([k.title() for k in parts])
    return f"set{name}"


def snake_to_camel(name):
    parts = name.split("_")
    name = parts[0] + "".join([k.title() for k in parts[1:]])
    return name


class Element(Generic[T], react.core.Element[T]):
    def add_children(self, children):
        self.kwargs["children"] = children
        # if len(children) == 1 and isinstance(children[0].component, ComponentFunction) and children[0].component.name.endswith("Layout"):
        #     self.kwargs["layout"] = children[0]
        # elif isinstance(self.component, ComponentWidget) and self.component.widget == Qt.QMainWindow:
        #     self.kwargs["central_widget"] = children[0]
        # else:
        #     import pdb

        #     pdb.set_trace()

    def _create_widget(self, kwargs):
        kwargs, listeners = self._split_kwargs(kwargs)
        assert isinstance(self.component, ComponentWidget)
        widget = self.component.widget(**kwargs)
        # for name, value in kwargs.items():
        #     self._update_widget_prop(widget, name, value)
        for name, callback in listeners.items():
            self._add_widget_event_listener(widget, name, callback)
        return widget

    def _update_widget_prop(self, widget, name, value):
        import pdb

        pdb.set_trace()
        # setattr(widget)
        # name = snake_to_setter(name)
        # method = getattr(widget, name)
        # method(value)

    def _update_widget(self, widget: Component, el_prev: "Element", kwargs):
        args = []
        for name, value in kwargs.items():
            if name.startswith("on_") and name not in args:
                self._update_widget_event_listener(widget, name, value, el_prev.kwargs.get(name))
            else:
                self._update_widget_prop(widget, name, value)

    def _add_widget_event_listener(self, widget: Component, name: str, callback: Callable):
        context = react.core._get_render_context().context
        name = name[3:]
        # import pdb

        # pdb.set_trace()
        root = context.root_element
        id = root.kwargs["id"]
        input_id = self.kwargs["id"]
        app.callback(Output(id, "children"), Input(input_id, name))(callback)
        # target_name = snake_to_camel(name[3:])

        # signal = getattr(widget, target_name)
        # signal.connect(callback)

    def _remove_widget_event_listener(self, widget: Component, name: str, callback: Callable):
        target_name = snake_to_camel(name[3:])
        signal = getattr(widget, target_name)
        signal.disconnect(callback)


def Markdown(**kwargs):
    comp = react.core.ComponentWidget(widget=dcc.Markdown)
    kwargs = {**locals(), **kwargs}
    del kwargs["comp"]
    del kwargs["kwargs"]
    return Element(comp, **kwargs)


def Dropdown(**kwargs):
    comp = react.core.ComponentWidget(widget=dcc.Dropdown)
    kwargs = {**locals(), **kwargs}
    del kwargs["comp"]
    del kwargs["kwargs"]
    return Element(comp, **kwargs)


def Div(**kwargs):
    comp = react.core.ComponentWidget(widget=html.Div)
    kwargs = {**locals(), **kwargs}
    del kwargs["comp"]
    del kwargs["kwargs"]
    return Element(comp, **kwargs)


@react.component
def App():
    colors = ["#001f3f", "#0074D9", "#85144b", "#3D9970"]
    color, set_color = react.use_state(colors[0])

    def _set_color(value):
        print("setting to", value)
        set_color(value)
        return value

    with Div(id="main") as main:
        Dropdown(id="lala", options=[{"label": i, "value": i} for i in colors], value=color, on_value=_set_color)
        Markdown(children="## Hi")
        Markdown(children="lala")
    return main


app = Dash(__name__)
widget, rc = react.core.render_fixed(App())


app.layout = html.Div(id="root", children=[widget])


if __name__ == "__main__":
    app.run_server(debug=True)
