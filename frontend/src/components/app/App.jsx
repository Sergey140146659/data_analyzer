import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainPage from "../pages/mainPage/MainPage";
import PraofPage from "../pages/praofPage/PraofPage";

function App() {
  const getRequest = async (url) => {
      const response = await fetch(url, {
          method: 'GET'
      });
      return response.json();
  }

  getRequest('http://localhost:8000/default/default').then(res => console.log(res));

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
