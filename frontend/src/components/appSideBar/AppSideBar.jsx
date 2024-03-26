import { NavLink } from 'react-router-dom';
import './appSideBar.css';

const AppSideBar = () => {
    return (
        <div className="sideBar__wrapper">
            <div className="sideBar">
                <nav>
                    <NavLink to="/">ПОСД</NavLink>
                    <NavLink to="/praof">ПРАОФ</NavLink>
                </nav>
            </div>
        </div>);
}

export default AppSideBar;