# if (
#     isinstance(el.component, ComponentFunction)
#     and _last_rc is not None
#     and isinstance(_last_rc.element.component, ComponentFunction)
#     and same_component(el.component, _last_rc.element.component)
#     and _last_rc.container is not None
#     and _last_rc.container._view_count == 0
# ):
#     hbox = widgets.VBox(_view_count=0)
#     _last_rc.render(el, hbox)
#     return hbox


# def test_make_reuse_state():
#     @react.component
#     def ButtonClick(**kwargs):
#         clicks, set_clicks = react.use_state(0)
#         return w.Button(description=f"Clicked {clicks} times", on_click=lambda: set_clicks(clicks + 1), **kwargs)

#     el = ButtonClick()
#     box = react.make(el)
#     button: ipywidgets.Button = box.children[0]
#     button.click()
#     assert button.description == "Clicked 1 times"

#     # same component name, we want to reuse the state
#     @react.component
#     def ButtonClick(**kwargs):
#         clicks, set_clicks = react.use_state(0)
#         return w.Button(description=f"Clicked {clicks} times!", on_click=lambda: set_clicks(clicks + 1), **kwargs)

#     el2 = ButtonClick()
#     box2 = react.make(el2)
#     assert box is box2
#     assert button.description == "Clicked 1 times!"

#     react.core._last_rc.close()


def make(el: Element, handle_error: bool = True):
    hbox = widgets.VBox(_view_count=0)

    def on_view_count(change):
        if change.new == 0:
            rc.close()
            hbox.close()

    hbox.observe(on_view_count, "_view_count")
    _, rc = render(el, hbox, "children", handle_error=handle_error)
    return hbox


