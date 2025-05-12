import './App.css';
import AppHeader from './component/AppHeader';
import TattooItem from './component/TattooItem';

const tattoo1 = {
    title: "ลายสักที่มือ",
    thumbnailUrl: "image/tattoo1.jpg"
};

function App() {
  return (
    <div className="app">
        {/* เรียกใช้งาน appHeader */}
        <AppHeader />
        
        <div className="app-grid">
            <TattooItem tattoo={tattoo1} />
        </div>
    </div>
  );
}

export default App;
