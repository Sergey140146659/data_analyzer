import useMainService from '../../services/MainService';

import './mainForm.css'

const MainForm = ({setCurData, setLoading}) => {
    const {postData} = useMainService();
    const onSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        const data = e.target.querySelector("textarea").value
            .split(", ")
            .map(str => Number(str));
        const k = Number(e.target.querySelector("input[type='number']").value);

        postData(data, k).then((res) => {
            console.log(res);
            setCurData(res);
            setLoading(false);
        })

    }
    return (
        <form onSubmit={(e) => onSubmit(e)}>
            <label className="textareaLabel" htmlFor="txtarea">Входные данные</label>
            <textarea id="txtarea" name="txtarea" defaultValue="13.2, 11.9, 11.9, 13.4, 13.4, 13.3, 11.9, 12.1, 12.6, 13.9,
                10.7, 12.3, 10.6, 10.4, 10.6, 11.0, 11.0, 10.8, 10.8, 10.6,
                10.9, 11.9, 11.6, 11.9, 11.3, 11.9, 11.4, 11.3, 11.0, 10.8,
                10.9, 10.9, 11.0, 11.2, 11.8, 11.8, 12.7, 12.9, 12.4, 14.2,
                14.8, 14.8, 15.4, 14.6, 14.1, 13.3, 12.6, 11.1, 11.2, 11.6"></textarea>
            <label className="textareaLabel" htmlFor="txtarea">Количество интервалов</label>
            <input type="number"></input>
            <button className="submitButton" type="submit">Отправить</button>
        </form>
    )
}

export default MainForm;