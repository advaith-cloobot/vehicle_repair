import React    from "react";
import template from "./invoice_list.jsx";

class invoice_list extends React.Component {
  render() {
    return template.call(this);
  }
}

export default invoice_list;
