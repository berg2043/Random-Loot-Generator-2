import './App.css';

function App() {
  return (
    <div className="App">
      <div className="roll-container">
        <div className="roll-item">
          <form>
            <label>CR</label>
            <br/>
            <input type="text"/>
            <br/>
            <label>Drop Method</label>
            <br/>
            <input type="radio" id="individual" name="group-size" defaultChecked/>
            <label htmlFor="individual">Individual Monster</label>
            <input type="radio" id="group" name="group-size"/>
            <label htmlFor="group">Loot Horde</label>
            <br/>
            <button>Roll!</button>
          </form>
        </div>
        <div className="roll-item"></div>
      </div>
    </div>
  );
}

export default App;
