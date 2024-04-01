import {Link, NavLink} from 'react-router-dom';
import './appSideBar.css';

const AppSideBar = ({place}) => {
    return (
        <div className="sideBar__wrapper">
            <div className="sideBar">
                <nav>
                    {place === 'main' ?
                        <>
                            <NavLink to="/">ПОСД</NavLink>
                            <div className="subLinks">
                                <a href="#section1">Интервальный статистический ряд</a>
                                <a href="#section2">Эмпирическая функция распределения</a>
                                <a href="#section3">Эмпирическая плотность распределения</a>
                                <a href="#section4">Точечные статистические оценки</a>
                                <a href="#section5">Гипотеза о нормальном распределении</a>
                                <a href="#section6">Гипотеза о экспоненциальном распределении</a>
                                <a href="#section7">Гипотеза о линейном распределении</a>
                            </div>
                        </>
                        : <NavLink to="/">ПОСД</NavLink>
                    }

                    <NavLink to="/praof">ПРАОФ</NavLink>
                </nav>
            </div>
        </div>
    );
}

export default AppSideBar;