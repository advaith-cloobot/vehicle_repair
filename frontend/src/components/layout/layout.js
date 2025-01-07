// layout.js
import React from "react";
import "./layout.css";
import Home from "../home/home"; // Child component
import CarDetails from "../car_details/car_details"; // Child component
import { Link, Route, Routes,Outlet } from "react-router-dom";
import { useNavigate,useLocation } from "react-router-dom";
import Invoice from "../invoice/invoice";
import InvoiceList from "../invoice_list/invoice_list";

const Layout = () => {
  const navigate = useNavigate();
  const location = useLocation();

  function logout(){
    sessionStorage.clear();
    navigate("/");
  }


  return (
    <div className="layout-container">
      <nav className="left-nav">
        <ul>
        <li><a href="#" onClick={() => navigate("/layout/home")}>Home</a></li>
          <li><a href="#" onClick={() => navigate("/layout/car_details")}>Enter Car Details</a></li>
          <li><a href="#"onClick={() => navigate("/layout/list_invoice")} >List of Invoices</a></li>
          <li><a href="#"onClick={() => logout()}>Log Out</a></li>       
        </ul>
      </nav>
      <main className="content-area">
        {/* <Home /> 
        <CarDetails/> */}
        {/* <Outlet /> */}
        {location.pathname.endsWith("/layout/home") && <Home />}
        {location.pathname.endsWith("/layout/car_details") && <CarDetails />}
        {location.pathname.includes("/layout/invoice") && <Invoice />}
        {location.pathname.includes("/layout/list_invoice") && <InvoiceList />}
      </main>
    </div>
  );
};

export default Layout;
