// layout.js
import React from "react";
import "./layout.css";
import Home from "../home/home"; // Child component
import CarDetails from "../car_details/car_details"; // Child component
import { Link, Route, Routes,Outlet } from "react-router-dom";
import { useNavigate,useLocation } from "react-router-dom";


const Layout = () => {
  const navigate = useNavigate();
  const location = useLocation();


  return (
    <div className="layout-container">
      <nav className="left-nav">
        <ul>
        <li><a href="#" onClick={() => navigate("/layout/home")}>Home</a></li>
          <li><a href="#" onClick={() => navigate("/layout/car_details")}>Enter Car Details</a></li>
          <li><a href="#">List of Invoices</a></li>
          <li><a href="#">About Us</a></li>       
        </ul>
      </nav>
      <main className="content-area">
        {/* <Home /> 
        <CarDetails/> */}
        {/* <Outlet /> */}
        {location.pathname.endsWith("/layout/home") && <Home />}
        {location.pathname.endsWith("/layout/car_details") && <CarDetails />}
      </main>
    </div>
  );
};

export default Layout;
