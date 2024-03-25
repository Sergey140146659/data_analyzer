import { NavLink } from 'react-router-dom';
import './appSideBar.css';

const AppSideBar = () => {
    return <div className="sideBar">
        <nav>
            <NavLink to="/">Main</NavLink>
            <NavLink to="/praof">PRAOF</NavLink>
        </nav>
    </div>
}

export default AppSideBar;