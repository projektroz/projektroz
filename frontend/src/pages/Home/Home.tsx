// pages/HomePage/Home.tsx
import './Home.scss';

import Button from '../../components/Button/Button';
import Rectangle from '../../components/Rectangle/Rectangle'; 
import Navmenu from '../../components/Navmenu/Navmenu'; 

const Home = () => {
  return (
    <div className='home-page'>
      <Rectangle>
        <div className="content">
          <div className="left">
            <img src="src/assets/images/logo.png" alt="Logo" className="logo" />
            <h1>Witaj na stronie głównej</h1>
          </div>
          <div className="right">
              <Navmenu />
          </div>
        </div>
      </Rectangle>
    </div>
  );
};

export default Home;
