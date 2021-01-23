import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "tiny_streamlit_webrtc",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("tiny_streamlit_webrtc", path=build_dir)


def tiny_streamlit_webrtc(name, key=None):
    component_value = _component_func(name=name, key=key, default=0)
    return component_value


if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")

    num_clicks = tiny_streamlit_webrtc("World")
    st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
    st.subheader("Component with variable args")

    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = tiny_streamlit_webrtc(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))
