import { useState } from 'react';
import { useDispatch } from 'react-redux';
import './Input.css';

function Input() {
  // States
  const [cr, setCr] = useState(null);
  const [group, setGroup] = useState('I');
  
  // Setup Dispatch
  const dispatch = useDispatch();

  // Calls saga to send challenge rating and loot type to server
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
    <div className="roll-item">
      <h2>
        Input challenge rating and loot type
      </h2>
      <form onSubmit={(event)=>{roll(event)}}>
        <label><strong>Challenge Rating: </strong></label>
        
        <input type="text" onChange={(event)=>{setCr(event.target.value)}}/>
        <br/>
        <label><strong>Drop Method: </strong></label>
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
        <button id="Roll-Button">Roll!</button>
      </form>
    </div>
  )
}

export default Input;