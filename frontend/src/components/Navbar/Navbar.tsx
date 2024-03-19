import { Link } from 'react-router-dom';
import './Navbar.scss';

function Navbar() {
    return (
      <div className="navbar">
        <ul>
          <li><Link to="/">Strona Główna</Link></li>
          <li><Link to="/login">Logowanie</Link></li>
          {}
        </ul>
      </div>
    );
  }

  export default Navbar