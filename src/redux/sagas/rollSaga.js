import axios from 'axios';
import { put, takeLatest, takeLeading } from 'redux-saga/effects';

function* getRoll(action){
  try {
    const response = yield axios.get(
      '/api/roll',
      { 
        params: {
          cr: action.payload.challengeRating,
          group: action.payload.lootType
        }
      }
    );
    yield put({type: 'LOOT', payload: response.data});
  } catch (error) {
    console.log('Error eith GetRoll', error);
  }
}

function* rollSaga(){
  yield takeLatest('GET_ROLL', getRoll);
}

export default rollSaga;