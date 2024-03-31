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
                </div>
                <div className="mainResult__item">
                    <p>Число выборочных значений, попавших в каждый интервал</p>
                    <p className="data">
                        {dataObj.empirical_frequencies.map((item, index, arr) =>
                            <span key={index}>
                                m<sub>{index}</sub> = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Частоты интервального ряда</p>
                    <p className="data">
                        {dataObj.interval_frequencies.map((item, index, arr) =>
                            <span key={index}>
                                p<sub>{index}</sub>* = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Середины интервалов</p>
                    <p className="data">
                        {dataObj.interval_frequencies.map((item, index, arr) =>
                            <span key={index}>
                                a̅<sub>{index}</sub> = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
                <div className="mainResult__item">
                    <img className="mainResult__item__image" src={require(`../../${dataObj.unsorted_data}`)}
                         alt=""/>
                </div>
                <div className="mainResult__item">
                    <img className="mainResult__item__image" src={require(`../../${dataObj.sorted_data}`)}
                         alt=""/>
                </div>
            </div>
            <div className="mainResult__block">
                <h2 className="mainResult__blockTitle">Построение эмпирической функции распределения</h2>
                <div className="mainResult__item">
                    <p>Накопленные частоты</p>
                    <p className="data">
                        {dataObj.accumulated_frequencies.map((item, index, arr) =>
                            <span key={index}>
                                z<sub>{index}</sub> = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
                <img className="mainResult__item__image" src={require(`../../${dataObj.emp_distr_function}`)}
                     alt=""/>
            </div>
            <div className="mainResult__block">
                <h2 className="mainResult__blockTitle">Построение эмпирической плотности распределения</h2>
                <div className="mainResult__item">
                    <p>Эмпирическая плотность распределения</p>
                    <p className="data">
                        {dataObj.empirical_density.map((item, index, arr) =>
                            <span key={index}>
                                ƒ<sub>{index}</sub>* = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
                <img className="mainResult__item__image" src={require(`../../${dataObj.emp_density_no_curve}`)}
                     alt=""/>
            </div>
            <div className="mainResult__block">
                <h2 className="mainResult__blockTitle">Получение точечных статических оценок</h2>
                <div className="mainResult__item">
                    <p>Выборочное среднее</p>
                    <p className="data">
                        ̅x = {dataObj.sample_mean}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Выборочная дисперсия</p>
                    <p className="data">
                        s<sup>2</sup> = {dataObj.sample_variance}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Исправленная выборочная дисперсия</p>
                    <p className="data">
                        ̅s̅<sup>2</sup> = {dataObj.sample_variance}
                    </p>
                    <p>Исправленное выборочное среднее отклонение</p>
                    <p className="data">
                        ̅s̅ = {dataObj.mean_square_deviation}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Выборочная асимметрия</p>
                    <p className="data">
                        A* = {dataObj.sample_asymmetry}
                    </p>
                </div>
                <div className="mainResult__item">
                    <p>Выборочный эксцесс</p>
                    <p className="data">
                        E* = {dataObj.sample_excess}
                    </p>
                </div>
            </div>
            <div className="mainResult__block">
                <h2 className="mainResult__blockTitle">Проверка гипотезы о нормальном распределении</h2>
                <div className="mainResult__item">
                    <p>Теоретические вероятности</p>
                    <p className="data">
                        {dataObj.theoretical_probabilities_normal.map((item, index, arr) =>
                            <span key={index}>
                                p<sub>{index}</sub> = {item}{index !== arr.length - 1 ? "," : ""}
                            </span>
                        )}
                    </p>
                </div>
            </div>
        </div>
    )
}

export default MainResult;