// src/pages/Home.tsx

import React from 'react'
import Navbar from '../../components/Navbar/Navbar'
import './Home.scss'
import background from '../../assets/images/background.png'; 

function Home() {
  return (
    <div className="home-page" style={{ backgroundImage: `url(${background})`}}>
      <Navbar />
      <div className="content">
        <h1>PROJEKT ROZ</h1>
        <div className="words">
          <h2>ROZWÓJ</h2>
          <h2>OPIEKA</h2>
          <h2>ZAUFANIE</h2>
        </div>
        <button className="btn btn-primary">Logowanie</button>
      </div>
    </div>
  );
}

export default Home;
