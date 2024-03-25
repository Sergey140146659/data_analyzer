import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import MainPage from "../pages/mainPage/MainPage";
import PraofPage from "../pages/praofPage/PraofPage";

import './app.css';

function App() {
  return (
      <div className="app">
          <Router>
              <Routes>
                  <Route path="/" element={<MainPage/>}/>
                  <Route path="/praof" element={<PraofPage/>}/>
              </Routes>
          </Router>
      </div>
  );
}

export default App;
