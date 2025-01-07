import React , { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import httpClient from "../../httpClient";
// import { useNavigate } from "react-router-dom";
import "./car_details.css";
const CarDetails = () => {
  const [make, setMake] = useState("");
  const [model, setModel] = useState("");
  const [type, setType] = useState("");
  const [gearType, setGearType] = useState("");
  const [issues, setIssues] = useState("");
  const token = sessionStorage.getItem('token');
  const [vrId, setVrId] = useState("");
  const [possibleFixList, setPossibleFixList] = useState([]);
  const [estimatedAmount, setEstimatedAmount] = useState("");
  const [isDisabled, setIsDisabled] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [showPaymentDetails, setShowPaymentDetails] = useState(false);
  const [showInvoiceButton, setShowInvoiceButton] = useState(false);
  const [paymentMode, setPaymentMode] = useState("");
  const [mobileNumber, setMobileNumber] = useState("");
  const [bankName, setBankName] = useState("");
  const [address, setAddress] = useState("");
  const [invoice_id, setInvoice_id] = useState("");
  const navigate = useNavigate();

  const handleDiagnose = () => {
    setIsLoading(true);
    const data = {
      user_id: sessionStorage.getItem('user_id'), // Example user_id, replace with actual user_id
      vehicle_make: make,
      vehicle_model: model,
      vehicle_type: type,
      gear_type: type === "ICE" ? gearType : "",
      issues: issues,
      token: sessionStorage.getItem('token')
    };
    console.log(data);
    httpClient.post('/diagnose_problem_and_get_fix', data,{
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
    .then((response) => {
      console.log(response.data)
      console.log('response login : ', response);
      const data = response.data;
      console.log("\n\ndata login :: ",data);
      if (data.status) {
        setIsDisabled(true);
      setVrId(data.vr_id);
      setPossibleFixList(data.possible_fix_list);
      setEstimatedAmount(data.estimated_amount);
        console.log("Success");
      }
      else{
        // alert("Invalid Email or Password");
        console.log("Failed to genrate fixes");
      }
    })
    .catch((error) => {
      console.log(error)
    }).finally(() => {
      setIsLoading(false);
    });
  };

  const handleConfirmPayment = () => {
    
    const data = {
      vr_id: vrId,
      payment_mode: paymentMode,
      mobile_number: mobileNumber,
      bank_name: bankName,
      address: address,
      bill_amount: estimatedAmount,
      token: sessionStorage.getItem('token')
    };
    httpClient.post('/process_payment', data,{
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      console.log(response.data)
      console.log('response payment : ', response);
      const data = response.data;
      console.log("\n\ndata login :: ",data);
      if (data.status) {
        console.log("Success");
        setInvoice_id(data.pi_id);
        setShowInvoiceButton(true);
      }
      else{
        // alert("Invalid Email or Password");
        console.log("Failed to process payment");
      }

    }).catch((error) => {
        console.log("error :: ",error)
    });
  };

  function progress_to_invoice(){
    console.log("Invoice : ",invoice_id);
    navigate(`/layout/invoice/${invoice_id}`);
  }


  return (
    <div className="car-details-container">
      <div className="car-icons">
        <span role="img" aria-label="car">🚗</span>
        <h1>Enter the details of your car</h1>
        <span role="img" aria-label="car">🚗</span>
      </div>
      <div className="form-group">
        <label>Enter make:</label>
        <input type="text" value={make} onChange={(e) => setMake(e.target.value)} disabled={isDisabled} />
      </div>
      <div className="form-group">
        <label>Enter model:</label>
        <input type="text" value={model} onChange={(e) => setModel(e.target.value)} disabled={isDisabled} />
      </div>
      <div className="form-group">
        <label>Type of car:</label>
        <select value={type} onChange={(e) => setType(e.target.value)} disabled={isDisabled}>
          <option value="">Select</option>
          <option value="ICE">ICE</option>
          <option value="electric">Electric</option>
        </select>
      </div>
      {type === "ICE" && (
        <div className="form-group">
          <label>Gear type:</label>
          <select value={gearType} onChange={(e) => setGearType(e.target.value)} disabled={isDisabled}>
            <option value="">Select</option>
            <option value="manual">Manual</option>
            <option value="automatic">Automatic</option>
          </select>
        </div>
      )}
      <div className="form-group">
        <label>Please enter issues faced in the car:</label>
        <textarea value={issues} onChange={(e) => setIssues(e.target.value)} disabled={isDisabled} />
      </div>
      <button onClick={handleDiagnose} disabled={isDisabled}>Diagnose Problem</button>
      {isLoading && (
        <div className="loading-animation">
          <span role="img" aria-label="car">🚗</span>
        </div>
      )}

      {isDisabled && (
          <div className="diagnosis-result">
          <h2>Possible Fixes:</h2>
          <ul>
            {possibleFixList.map((fix, index) => (
              <li key={index}><span role="img" aria-label="spanner">🔧</span> {fix}</li>
            ))}
          </ul>
          <p>The Total estimated cost of the repair is: <span role="img" aria-label="rupee">₹</span>{estimatedAmount}</p>
          <button onClick={() => setShowPaymentDetails(true)}>Proceed to Payment</button>
        </div>
      )}

{showPaymentDetails && (
        <div className="payment-details">
          <h2>Enter Payment Details</h2>
          <div className="form-group">
            <label>Enter mode of payment:</label>
            <select value={paymentMode} onChange={(e) => setPaymentMode(e.target.value)}>
              <option value="">Select</option>
              <option value="netbanking">Netbanking</option>
              <option value="upi">UPI</option>
              <option value="card">Card</option>
            </select>
            <span role="img" aria-label="money">💵</span>
          </div>
          <div className="form-group">
            <label>Enter mobile number:</label>
            <input type="text" value={mobileNumber} onChange={(e) => setMobileNumber(e.target.value)} />
          </div>
          <div className="form-group">
            <label>Enter name of the bank used:</label>
            <input type="text" value={bankName} onChange={(e) => setBankName(e.target.value)} />
          </div>
          <div className="form-group">
            <label>Enter your address:</label>
            <textarea value={address} onChange={(e) => setAddress(e.target.value)} />
            <span role="img" aria-label="house">🏠</span>
          </div>
          <button onClick={handleConfirmPayment}>Confirm Payment</button>
        </div>
      )}

      {showInvoiceButton && (
        <button onClick={progress_to_invoice}>View Payment Invoice</button>
      )}
    </div>
  );
}

export default CarDetails;
