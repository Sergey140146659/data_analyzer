function App() {
  const getRequest = async (url) => {
      const response = await fetch(url, {
          method: 'GET'
      });
      return response.json();
  }

  getRequest('http://localhost:8000/default/default').then(res => console.log(res));

  return (
    <div>
      <h1>Приложение</h1>
    </div>
  );
}

export default App;
