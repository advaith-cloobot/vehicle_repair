import React    from "react";
import template from "./invoice.jsx";

class invoice extends React.Component {
  render() {
    return template.call(this);
  }
}

export default invoice;
