import './App.css';
import AppHeader from './component/AppHeader';
import tattoos from './component/data/Tattoos';
import TattooItem from './component/TattooItem';

function App() {
    // eslint-disable-next-line no-unused-vars
    const tattooElements = tattoos.map((tattoo, index) => {
        return <TattooItem key={index} tattoo={tattoo} />;
    })
    return (
    <div className="app">
        {/* เรียกใช้งาน appHeader */}
        <AppHeader />
        
        <div className="app-grid">
            {tattooElements}
        </div>
    </div>
  );
}

export default App;
