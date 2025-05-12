/* eslint-disable jsx-a11y/alt-text */
import './App.css';

function App() {
  return (
    <div className="app">
        <header className="app-header-logo">
            <img src='/image/logo.jpg' />
                
        </header>
        <div className="app-grid">
            <div className="tattoo-item">
                <img src="/image/tattoo1.jpg" />
                <h4>ต่ายน้อย 1</h4>
            </div>
            <div className="tattoo-item">
                <img src="/image/tattoo2.jpg" />
                <h4>ต่ายน้อย 1</h4>
            </div>
            <div className="tattoo-item">
                <img src="/image/tattoo3.jpg" />
                <h4>ต่ายน้อย 1</h4>
            </div>
            <div className="tattoo-item">
                <img src="/image/tattoo4.jpg" />
                <h4>ต่ายน้อย 1</h4>
            </div>
            
        </div>
    </div>
  );
}

export default App;
