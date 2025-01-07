import React from "react";
import "./home.css";

class Home extends React.Component {
  render() {
    return (
      <div className="home-container">
        <div className="title-section">
          <span role="img" aria-label="car tire" className="tire-icon">🛞</span>
          <h1>Car Repair Estimator Tool</h1>
          <span role="img" aria-label="car tire" className="tire-icon">🛞</span>
        </div>
        <div className="description-section">
          <p><span role="img" aria-label="book">📖</span> This is a tool in which car owners can input their car details and the issue they are currently facing with the car after which the tool will generate the possible repair steps based on the inputs given. It will also generate the cost and allow the user to enter his or her payment details in order to pay for the repair. The invoice for the transaction will also be available to view by the user as well as previous invoices.</p>
        </div>
        <div className="how-to-use-section">
          <h2><span role="img" aria-label="question mark">❓</span> How to Use:</h2>
          <ul>
            <li><span className="rotating-tire-icon" role="img" aria-label="car tire">🛞</span> Go to the 'Enter Car Details' tab on the left-hand pane and click. On doing this, the car detail form page will appear on the right.</li>
            <li><span className="rotating-tire-icon" role="img" aria-label="car tire">🛞</span> Enter the related details and click diagnose. The possible fixes along with the estimated cost will be generated and displayed.</li>
            <li><span className="rotating-tire-icon" role="img" aria-label="car tire">🛞</span> The user can click the enter payment details and input their payment details in the appearing fields.</li>
            <li><span className="rotating-tire-icon" role="img" aria-label="car tire">🛞</span> On clicking confirm payment, the user can view the invoice of the conducted transaction.</li>
            <li><span className="rotating-tire-icon" role="img" aria-label="car tire">🛞</span> The user can also view their previous invoices in case they have previously used the tool.</li>
          </ul>
        </div>
      </div>
    );
  }
}

export default Home;