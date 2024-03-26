import {useState} from "react";

import AppSideBar from "../../appSideBar/AppSideBar";
import MainForm from "../../mainForm/MainForm";


import './mainPage.css';

const MainPage = () => {
    const [curData, setCurData] = useState(
        {})


    return <div className="pageContent">
            <AppSideBar/>
        <div className="mainContent">
            <h1 className="pageTitle">Первичная обработка статистических данных</h1>
            <MainForm setCurData={setCurData} />
        </div>

    </div>
}

export default MainPage;