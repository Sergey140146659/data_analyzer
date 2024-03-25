const usePraofService = () => {
    const postData = async (data) => {
        console.log(data)
        try {
            const response = await fetch('http://localhost:8000/praof/data_processing', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'data': data})
            });

            if (!response.ok) {
                throw new Error('Ошибка HTTP: ' + response.status);
            }

            return await response.json();
        } catch (error) {
            console.error('Произошла ошибка:', error);
            return null;
        }
    }


    return {postData};
}

export default usePraofService;