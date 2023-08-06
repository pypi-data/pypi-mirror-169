from typing import rev
import core as react

filter_like, set_filter_like = react.use_state(None)
set_filter_like([1, 1])

# reveal_type(filter_like)


# dtype: Optional[], Callable[[Optional[Tuple[str, int]]], None]

# from typing import Callable, Dict, TypeVar


# FuncT = TypeVar("FuncT", bound=Callable[..., None])


# def test(key, f: FuncT) -> Dict[str, FuncT]:
#     return {key: f}


# def f1(a: int, b: str):
#     pass


# def f2(a: int, b: str = "lala"):
#     pass


# d = test("lala", f2)


# d["lala2"] = f1

# Dict[str, Callable[[str, Optional[str], Any], Any]", target has type "Callable[[int, Optional[str]], Any]")
# T = TypeVar("T")

# d: Dict[str, Callable[[str, Optional[str], Any], Any]] = {"lala": f1, "hoeba": f2, "lala2": 3}
# f1(d)


# from inspect import isclass
# from typing import Any, Callable, Dict, Type
# import typing
# import ipywidgets as widgets
# from ipywidgets import Widget
# import ipywidgets
# import react
# import typing_extensions
# import reacton.ipywidgets as w
# from typing_extensions import Concatenate
# from .core import mime_bundle_default

# from reacton.core import ComponentFunction, ComponentWidget, Element

# # see https://peps.python.org/pep-0612/
# P = typing_extensions.ParamSpec("P")
# FuncT = typing.TypeVar("FuncT", bound=Callable[..., Element])
# T = typing.TypeVar("T")


# def component_widget(widget_class: Type[Widget], element_class: Type[Element] = Element):
#     def wrapper(f: Callable[P, T]):
#         def add_key(__key__=None, *args: P.args, **kwargs: P.kwargs):
#             comp = react.core.ComponentWidget(widget=widget_class)
#             return w.ButtonElement(comp, **kwargs)

#         return add_key

#     return wrapper
#     # kwargs: Dict[Any, Any] = w.without_default(Button, locals())
#     # if isinstance(kwargs.get("layout"), dict):
#     #     kwargs["layout"] = Layout(**kwargs["layout"])
#     # if isinstance(kwargs.get("style"), dict):
#     #     kwargs["style"] = w.ButtonStyle(**kwargs["style"])
#     # widget_cls = ipywidgets.widgets.widget_button.Button
#     # comp = react.core.ComponentWidget(widget=widget_cls)
#     # return w.ButtonElement(comp, **kwargs)


# @component_widget(ipywidgets.Button)
# def Button(
#     button_style: str = "",
#     description: str = "",
#     disabled: bool = False,
#     icon: str = "",
# ) -> Element[ipywidgets.widgets.widget_button.Button]:
#     """Button widget.

#     This widget has an `on_click` method that allows you to listen for the
#     user clicking on the button.  The click event itself is stateless.

#     Parameters
#     ----------
#     description: str
#        description displayed next to the button
#     tooltip: str
#        tooltip caption of the toggle button
#     icon: str
#        font-awesome icon name
#     disabled: bool
#        whether user interaction is enabled

#     :param button_style: Use a predefined styling for the button.
#     :param description: Button label.
#     :param disabled: Enable or disable user changes.
#     :param icon: Font-awesome icon name, without the 'fa-' prefix.
#     :param tooltip: Tooltip caption of the button.
#     """
#     pass


# # @overload
# # def component(obj: None = None, mime_bundle=...) -> Callable[[P], FuncT]:
# #     ...


# # @overload
# # ...


# # def component(obj: FuncT = None, mime_bundle: Dict[str, Any] = mime_bundle_default):
# def component(obj: Callable[P, Element] = None, mime_bundle: Dict[str, Any] = mime_bundle_default) -> Callable[Concatenate[("bla", str), P], Element]:
#     def wrapper(obj: Callable[P, Element]):
#         def add_key(bla=None, *args: P.args, **kwargs: P.kwargs):
#             if isclass(obj) and issubclass(obj, widgets.Widget):
#                 return ComponentWidget(widget=obj, mime_bundle=mime_bundle)(bla=bla, *args, **kwargs)
#             else:
#                 return ComponentFunction(f=obj, mime_bundle=mime_bundle)(bla=bla, *args, **kwargs)

#         #     return typing.cast(Callable[Concatenate[("__key__", str), P], Element], ComponentWidget(widget=obj, mime_bundle=mime_bundle))
#         # else:
#         #     return typing.cast(Callable[Concatenate[("__key__", str), P], Element], ComponentFunction(f=obj, mime_bundle=mime_bundle))

#         return add_key

#     if obj is not None:
#         return wrapper(obj)
#     else:
#         return wrapper


# @component
# def Child(a=1, b=2):
#     return w.VBox(children=[w.Button(__key__="button")], __key__="box")


# @component()
# def App():
#     return Child(__key__="child")


# app = App()
# # a = Button()
# Child()

# app = App()
