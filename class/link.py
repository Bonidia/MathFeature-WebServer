import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "link_button",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("link_button", path=build_dir)

def link_button(name, url, key=None):
    component_value = _component_func(name=name, url=url, key=key, default=False)
    return component_value

if not _RELEASE:
    import streamlit as st
    st.header('Link button test')
    if link_button('Open Link', 'https://docs.streamlit.io/en/stable/'):
        st.balloons()