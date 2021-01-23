import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {}

class TinyWebrtc extends StreamlitComponentBase<State> {
  public state = {}

  public render = (): ReactNode => {
    return <span></span>
  }
}

export default withStreamlitConnection(TinyWebrtc)
