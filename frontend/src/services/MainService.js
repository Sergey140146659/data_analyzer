const useMainService = () => {
    const postData = async (data, k) => {
        try {
            const response = await fetch('http://localhost:8000/first_part/data_processing', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'data': data, "k": k})
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

export default useMainService;