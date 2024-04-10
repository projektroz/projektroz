// src/App.tsx

// import React from "react";
import { Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/global.scss";

import "./App.css";

// import PrivateRoutes from "./components/PrivateRoute/PrivateRoute";

import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import Logout from "./pages/Logout/Logout";
import Register from "./pages/Register/Register";
import Dashboard from "./pages/Dashboard/Dashboard";

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<Register />} />

        {/* <Route element={<PrivateRoutes />}> */}
        <Route path="/dashboard" element={<Dashboard />} />
        {/* </Route> */}
      </Routes>
    </>
  );
};

export default App;
