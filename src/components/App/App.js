import './App.css';
import Input from './../Input/Input'
import Loot from './../Loot/Loot';

function App() {

  return (
    <div className="App">
      <div className="Roll-Container">
        <Input className="Roll-Input"/>
        <Loot className="Roll-Input"/>
      </div>
    </div>
  );
}

export default App;
