import { all } from 'redux-saga/effects';
import rollSaga from './rollSaga'

export default function* rootSaga() {
  yield all([
    rollSaga()
  ]);
}