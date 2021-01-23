import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";
import React, { ReactNode } from "react"

interface State {
  numClicks: number
}

class TinyWebrtc extends StreamlitComponentBase<State> {
  public state = { numClicks: 0 }

  public render = (): ReactNode => {
    const name = this.props.args["name"]

    return (
      <span>
        Hello, {name}! &nbsp;
        <button onClick={this.onClicked} disabled={this.props.disabled}>
          Click Me!
        </button>
      </span>
    )
  }

  private onClicked = (): void => {
    this.setState(
      prevState => ({ numClicks: prevState.numClicks + 1 }),
      () => Streamlit.setComponentValue(this.state.numClicks)
    )
  }
}

export default withStreamlitConnection(TinyWebrtc)
