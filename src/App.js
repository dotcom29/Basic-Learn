import './App.css';
import AppHeader from './component/AppHeader';
import TattooItem from './component/TattooItem';
import TattooPost from './component/TattooPost';

function App() {
  return (
    <div className="app">
        {/* เรียกใช้งาน appHeader */}
        <AppHeader />
        
        <div className="app-grid">
            <TattooItem />
            <TattooItem />
            <TattooItem />
            <TattooItem />
        </div>
        <TattooPost />
    </div>
  );
}

export default App;
