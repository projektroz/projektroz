// src/App.tsx

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <Routes> {}
          <Route path="/login" element={<Login />} /> {}
          <Route path="/" element={<Home />} /> {}
        </Routes> {}
      </div>
    </Router>
  );
}

export default App;
