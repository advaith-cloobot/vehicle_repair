// layout.js
import React from "react";
import "./layout.css";
import Home from "../home/home"; // Child component

const Layout = () => {
  return (
    <div className="layout-container">
      <nav className="left-nav">
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Enter Car Details</a></li>
          <li><a href="#">List of Invoices</a></li>
          <li><a href="#">About Us</a></li>
        </ul>
      </nav>
      <main className="content-area">
        <Home /> {/* This renders the child component */}
      </main>
    </div>
  );
};

export default Layout;
