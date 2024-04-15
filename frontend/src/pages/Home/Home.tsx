// pages/HomePage/Home.tsx
import "./Home.scss";

// import Button from '../../components/Button/Button';
import Rectangle from "../../components/Rectangle/Rectangle";
import ScrollAction from "../../components/ScrollAction/ScrollAction";
// import Navmenu from "../../components/Navmenu/Navmenu";

const Home = () => {
  const links = [
    { name: "Strona główna", url: "/home", icon: "src/assets/icons/home.png" },
    { name: "O nas", url: "#info", icon: "src/assets/icons/user.png" },
    { name: "Panel użytkownika", url: "/dashboard", icon: "src/assets/icons/manage.png"},
    { name: "Logowanie", url: "/login", icon: "src/assets/icons/login.png" },
  ];

  return (
    <div className="app-page home-page">
      <div className="main-section">
        <Rectangle links={links}>
          <img src="src/assets/images/logo.png" alt="Logo" className="logo" />
          <h1>Witaj na stronie głównej</h1>
        </Rectangle>
        <ScrollAction />
      </div>
      <div id="info" className="info-section">
        <p>
          Informacje o: Fundacja Projekt ROZ Już od 18 lat prowadzimy w Krakowie
          Rodzinny Dom Dziecka „Mały Książę”, a w myśl nowych przepisów placówkę
          opiekuńczo-wychowawczą typu rodzinnego. To miejsce, w którym przez
          cały rok, 24 godziny na dobę, żyjemy w 14 osobowej rodzinie. Mieszkają
          z nami i wychowują się dzieci, które nie mogą mieszkać wraz ze swoimi
          rodzinami biologicznymi, ale mają z nimi kontakt, w szczególnych
          wypadkach mogą do nich wrócić lub być przysposobione przez innych.
          Lata doświadczeń, pozwoliło nam spojrzeć na sprawy opieki zastępczej w
          inny sposób, bo też z innej perspektywy. Wiemy, że można inaczej: bez
          narzekania, bez epatowania nieszczęściem, bez ujawniania wizerunku
          dzieci!!! Wiedzą o tym też nasi przyjaciele dzięki wsparciu, których w
          lipcu 2012 powołaliśmy FUNDACJĘ PROJEKT ROZ. Są to osoby wcześniej
          niezwiązane z pieczą zastępczą, które jej obraz budowały na podstawie
          kontaktów z nami, a szczególnie z dziećmi nam powierzonymi. To oni i
          nasze dzieci są największym i najlepszym źródłem informacji o naszej
          działalności. Skrót ROZ to: Rodzinna Opieka Zastępcza, ale też: •
          ROZwój, ROZum, wyROZumiałość, ROdZina. Nadrzędnym celem jest
          propagowanie wiedzy o rodzinnych formach opieki zastępczej, poprzez
          zbieranie i upublicznianie dobrych praktyk z terenu całej Polski.
          Naszym atutem jest doświadczenie, poparte rzetelną wiedzą
          merytoryczną. Zwracamy się do Państwa z prośbą o pomoc w prowadzeniu
          naszego PROJEKTU ROZ, a zarazem domu „Mały Książę”. Wierzymy, że każdy
          z Was znajdzie obszar, w jakim będzie mógł nas wesprzeć, czy to
          finansowo, czy poprzez pomoc w organizacji zajęć edukacyjnych,
          wypoczynku, jak również w na przykład kontaktach z lekarzami,
          prawnikami. Jesteśmy przekonani i to chcemy przekazać innym, że
          prowadzenie rodziny zastępczej, rodzinnego domu dziecka czy placówki
          typu rodzinnego to praca zespołowa, a zespół ten tworzą dzieci
          biologiczne, przyjaciele, sponsorzy, wolontariusze, sąsiedzi,
          pracownicy urzędów.
        </p>
      </div>
    </div>
  );
};

export default Home;
