import './App.css';
import AppHeader from './component/AppHeader';
import TattooItem from './component/TattooItem';

function App() {
  return (
    <div className="app">
        {/* เรียกใช้งาน appHeader */}
        <AppHeader />
        
        <div className="app-grid">
            <TattooItem title="ลายสักที่มือ" thumbnailUrl="/image/tattoo1.jpg" alt="" />
            <TattooItem title="ลายสักที่แขน" thumbnailUrl="/image/tattoo2.jpg" alt="" />
            <TattooItem title="ลายสักที่ข้อมือ" thumbnailUrl="/image/tattoo3.jpg" alt="" />
            <TattooItem title="ลายสักที่ต้นแขน" thumbnailUrl="/image/tattoo4.jpg" alt="" />
        </div>
    </div>
  );
}

export default App;
