import './form.css';

const Form = ({labelName}) => {
    const sendData = (e) => {
        e.preventDefault();
        console.log('asd')
    }

    return (
        <form onSubmit={(e) => sendData(e)}>
            <label className="textareaLabel" htmlFor="txtarea">{labelName}</label>
            <textarea id="txtarea" name="txtarea" rows="5" defaultValue={123} ></textarea>
            <button className="submitButton" type="submit">Отправить</button>
        </form>
    )
}

export default Form;