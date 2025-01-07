import React, { use }    from "react";
// import template from "./invoice.jsx";
import { useEffect,useState } from "react";
import { useNavigate, useParams,useLocation } from 'react-router-dom';
import httpClient from "../../httpClient";
// import template from "./invoice_list.jsx";
import './invoice_list.css';

const InvoiceList = () => {
  const token = sessionStorage.getItem('token');
  const [InvoiceList, setInvoiceList] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch_invoice_list();
  }, []);

  function fetch_invoice_list(){
    const data = {
      token: token
    }
    httpClient.post('/get_invoice_list',data,{
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log(response.data)
        console.log('response fetch_invoice_list : ', response);
        const data = response.data;
        console.log("\n\ndata fetch_invoice_list :: ",data);
        if (data.status) {
          // setInvoiceData(data.payment_invoice_dict);
          setInvoiceList(data.payment_invoice_list);
        }
        else{
          // alert("Invalid Email or Password");
          console.log("Failed to fetch invoice list");
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const handleInvoiceClick = (id) => {
    console.log("Invoice ID : ",id);
    navigate(`/layout/invoice/${id}`);
  };

  return (
    <div className="invoice-list-container">
      <h1>Previous Invoice List</h1>
      <div className="invoice-list">
        {InvoiceList.map((invoice, index) => (
          <button
            key={index}
            className="invoice-button"
            onClick={() => handleInvoiceClick(invoice.pi_id)}
          >
            <span role="img" aria-label="document" className="document-icon">📄</span>
            Invoice #{index + 1}
          </button>
        ))}
      </div>
    </div>
  );

}

export default InvoiceList;
