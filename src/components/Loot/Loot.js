import { useSelector } from 'react-redux';
import './Loot.css';

function Loot() {

  const loot = useSelector(state => state.loot)

  return (
    <div className = "Loot">
      {Object.keys(loot).map(key => {
        return (
          <div>
            <h2>
              {key}
            </h2>
            <ul>
              {loot[key].map(item => {
                return (
                  <li>{item}</li>
                )
              })}
            </ul>
          </div>
        )
      })}
    </div>

  )
}

export default Loot;