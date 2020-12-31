import { combineReducers } from 'redux';

const createReducer = (string, type=[]) => {
  return (state=type, action) => {
    switch(action.type){
      case string: 
        return action.payload;
      case 'CLEAR_ALL':
        return type;
      default:
        return state;
    }
  }
}

const rootReducer = combineReducers({
  createReducer('LOOT')
});

export default rootReducer;