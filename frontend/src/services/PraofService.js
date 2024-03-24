const usePraofService = () => {
    const postData = (data) => {
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'data': data })
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Ошибка:', error));
    }
}

export default usePraofService;