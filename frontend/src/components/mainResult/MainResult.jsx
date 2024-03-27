import './mainResult.css'

const MainResult = ({dataObj}) => {
    console.log(dataObj)
    return (
        <div className="mainResult">
            <div className="mainResult__block">
                <h2 className="mainResult__blockTitle">Построение интервального статистического ряда</h2>
                <div className="mainResult__item">
                    <p>Объем выборки</p>
                    <p className="data">
                        <span>n = {dataObj.n},</span>
                        <span>x_min = {dataObj.x_min},</span>
                        <span>x_max = {dataObj.x_max}</span>
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Диапазон выборки</p>
                    <p className="data">
                        <span>x ∈ [{dataObj.x_min}, {dataObj.x_max}]</span>
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Размах выборки</p>
                    <p className="data">
                        <span>R = {dataObj.R}</span>
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Количество интервалов</p>
                    <p className="data">
                        <span>k = {dataObj.k}</span>
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Длина интервала</p>
                    <p className="data">
                        <span>d = {dataObj.d}</span>
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Интервалы статистического ряда</p>
                    <p className="data">
                        {dataObj.intervals.map((item, index, arr) =>
                            <span key={index}>
                                I<sub>{index}</sub> = [{item[0]}, {item[1]}){index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                    <p>Число выборочных значений, попавших в каждый интервал</p>
                    <p className="data">
                        {dataObj.empirical_frequencies.map((item, index, arr) =>
                            <span key={index}>
                                m<sub>{index}</sub> = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
            </div>
        </div>
    )
}

export default MainResult;