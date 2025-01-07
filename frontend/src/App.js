import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/layout/layout'; // Parent with left nav
import Login from './components/login/login';
import Home from './components/home/home'; // Child of Layout

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        {/* Nesting Layout and Home */}
        <Route path="/layout/*" element={<Layout />}>
          <Route path="home" element={<Home />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
