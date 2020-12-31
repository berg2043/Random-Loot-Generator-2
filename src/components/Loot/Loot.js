import { useSelector } from 'react-redux';

function Loot(){

  const loot = useSelector(state=>state.loot)

  return(
    <div>{`${JSON.stringify(loot)}`}</div>
    
  )
}

export default Loot;