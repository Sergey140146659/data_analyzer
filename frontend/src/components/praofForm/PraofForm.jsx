import usePraofService from "../../services/PraofService";

import './praofForm.css';

const PraofForm = ({setCurData}) => {
    const {postData} = usePraofService();
    const onSubmit = async (e) => {
        e.preventDefault();
        const data = e.target.querySelector("textarea").value
                     .split(", ")
                     .map(str => Number(str));
        setCurData(await postData(data));
    }

    return (
        <form onSubmit={(e) => onSubmit(e)}>
            <label className="textareaLabel" htmlFor="txtarea">Входные данные</label>
            <textarea id="txtarea" name="txtarea" placeholder="13.2, 11.9, 11.9, 13.4, 13.4, 13.3, 11.9, 12.1, 12.6, 13.9,
                10.7, 12.3, 10.6, 10.4, 10.6, 11.0, 11.0, 10.8, 10.8, 10.6,
                10.9, 11.9, 11.6, 11.9, 11.3, 11.9, 11.4, 11.3, 11.0, 10.8,
                10.9, 10.9, 11.0, 11.2, 11.8, 11.8, 12.7, 12.9, 12.4, 14.2" ></textarea>
            <button className="submitButton" type="submit">Отправить</button>
        </form>
    )
}

export default PraofForm;