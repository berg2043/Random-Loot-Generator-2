import { useState } from 'react';
import { useDispatch } from 'react-redux';
import './App.css';
import Loot from './../Loot/Loot';

function App() {
  // States
  const [cr, setCr] = useState(null);
  const [group, setGroup] = useState('I');
  
  // Setup Dispatch
  const dispatch = useDispatch();

  function roll(event){
    event.preventDefault();
    console.log(cr,group);
    dispatch({
      type: 'GET_ROLL',
      payload: {
        challengeRating: cr,
        lootType: group
      }
    })
  }
  return (
    <div className="App">
      <div className="roll-container">
        <div className="roll-item">
          <form onSubmit={(event)=>{roll(event)}}>
            <label>CR</label>
            <br/>
            <input type="text" onChange={(event)=>{setCr(event.target.value)}}/>
            <br/>
            <label>Drop Method</label>
            <br/>
            <input 
              type="radio" 
              id="individual" 
              name="group-size" 
              checked={group === 'I'} 
              value = 'I' 
              onChange={()=>{setGroup('I')}}
            />
            <label htmlFor="individual">Individual Monster</label>
            <input 
              type="radio" 
              id="group" 
              name="group-size" 
              checked={group === 'G'} 
              value = 'G' 
              onChange={()=>{setGroup('G')}}
            />
            <label htmlFor="group">Loot Horde</label>
            <br/>
            <button>Roll!</button>
          </form>
        </div>
        <Loot/>
        <div className="roll-item"></div>
      </div>
    </div>
  );
}

export default App;
