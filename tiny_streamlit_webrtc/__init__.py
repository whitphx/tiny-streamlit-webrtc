import logging
import os
import streamlit.components.v1 as components
from aiortc import RTCPeerConnection, RTCSessionDescription

logger = logging.getLogger(__name__)

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


def tiny_streamlit_webrtc(key=None):
    component_value = _component_func(key=key, default=None)

    if component_value:
        offer_json = component_value["offerJson"]

        # Debug
        st.write(offer_json)

        offer = RTCSessionDescription(sdp=offer_json["sdp"], type=offer_json["type"])

        pc = RTCPeerConnection()

        @pc.on("track")
        def on_track(track):
            logger.info("Track %s received", track.kind)
            pc.addTrack(track)  # Passthrough. TODO: Implement video transformation

        # TODO: `await` does not work in a function. It must be used inside a coroutine.
        # handle offer
        await pc.setRemoteDescription(offer)

        # send answer
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)

        # TODO: How to send back the answer to frontend?
        # answer_json = json.dumps(
        #     {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        # )


    return component_value


if not _RELEASE:
    import streamlit as st

    tiny_streamlit_webrtc()
