// pages/HomePage/Home.tsx
import "./Home.scss";
import Rectangle from "../../components/Rectangle/Rectangle";
import Button from "../../components/Button/Button";

const Home = () => {
    // const links = [
    //   { name: "Strona główna", url: "/home", icon: "src/assets/icons/home.png" },
    //   { name: "Panel użytkownika", url: "/dashboard", icon: "src/assets/icons/manage.png"},
    //   { name: "Logowanie", url: "/login", icon: "src/assets/icons/login.png" },
    //   { name: "Rejestracja", url: "/register", icon: "src/assets/icons/login.png"}
    // ];

    return (
        <div className="app-page home-page">
            <Rectangle /*links={links}*/>
                <img
                    src="src/assets/images/logo.png"
                    alt="Logo"
                    className="logo"
                />
                <p className="description">
                    ProjektRoz jest platformą wspierającą zarządzanie danymi.
                </p>
                <p className="desctirpion">Zaloguj się, aby kontynuować.</p>
                <Button
                    label="ZALOGUJ"
                    onClick={() => (window.location.href = "/login")}
                />
            </Rectangle>
        </div>
    );
};

export default Home;

