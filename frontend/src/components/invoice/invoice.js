import React, { use }    from "react";
// import template from "./invoice.jsx";
import { useEffect,useState } from "react";
import { useNavigate, useParams,useLocation } from 'react-router-dom';
import httpClient from "../../httpClient";
import './invoice.css';
const Invoice = () => {

  const token = sessionStorage.getItem('token');
  const [invoiceData, setInvoiceData] = useState(null);
  
  const { id } = useParams();
  useEffect(() => {
    
    console.log("Invoice : ",id);
    fetch_invoice_details(id);
  }, []);


  function fetch_invoice_details(p_id){
    console.log("fetch_invoice_details : ",p_id);
    const data = {
      p_id : p_id
    }
    httpClient.post('/get_payment_invoice_details', data,{
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log(response.data)
        console.log('response fetch_invoice_details : ', response);
        const data = response.data;
        console.log("\n\ndata fetch_invoice_details :: ",data);
        if (data.status) {
          setInvoiceData(data.payment_invoice_dict);
        }
        else{
          alert("Invalid Email or Password");
        }
      })
      .catch((error) => {
        console.log(error)
      })

  }
  if (!invoiceData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="invoice-container">
      <div className="invoice-header">
        <span role="img" aria-label="document">📄</span>
        <h1>Payment Invoice</h1>
        <span role="img" aria-label="document">📄</span>
      </div>
      <div className="invoice-section">
        <h2>Billed to:</h2>
        <p>{invoiceData.user_name}</p>
        <p>{invoiceData.mobile_number}</p>
        <p>{invoiceData.address}</p>
      </div>
      <div className="invoice-section">
        <h2>Vehicle Details <span role="img" aria-label="car">🚗</span></h2>
        <p><strong>Make:</strong> {invoiceData.vehicle_make}</p>
        <p><strong>Model:</strong> {invoiceData.vehicle_model}</p>
        <p><strong>Type:</strong> {invoiceData.vehicle_type}</p>
        <div className="invoice-subsection">
          <h3>Issues Faced <span role="img" aria-label="danger">⚠️</span></h3>
          <p>{invoiceData.issues}</p>
        </div>
      </div>
      <div className="invoice-section">
        <h2>Repair Details</h2>
        <ul>
          {invoiceData.possible_fixes.map((fix, index) => (
            <li key={index}><span role="img" aria-label="spanner">🔧</span> {fix}</li>
          ))}
        </ul>
      </div>
      <div className="invoice-section">
        <h2>Payment Details</h2>
        <p><strong>Mode of Payment:</strong> {invoiceData.mode_of_payment}</p>
        <p><strong>Affiliated Bank:</strong> {invoiceData.bank}</p>
        <p><strong>Bill Amount:</strong> <span role="img" aria-label="rupee">₹</span>{invoiceData.bill_amount}</p>
      </div>
    </div>
  );
}

export default Invoice;
