import {useState} from "react";

import AppSideBar from "../../appSideBar/AppSideBar";
import Form from "../../form/Form";
import PraofResult from "../../praofResult/PraofResult";

import './praofPage.css';


const PraofPage = () => {
    const [curData, setCurData] = useState(
        {amplitudes: "/PRAOF/praof_pics/85Fn0HsoIuM.jpg",
            approximations_pic: "/PRAOF/praof_pics/EQug5D207ck.jpg",
            points_pic: "/PRAOF/praof_pics/hESTmzVfIHQ.jpg",
            supsmooth_points_pic: "/PRAOF/praof_pics/YhsdQuC2ymA.jpg"})

    return (
        <div className="pageContent">
            <AppSideBar/>
            <Form labelName="Входные данные" setCurData={setCurData} />
            <PraofResult objImages={curData} />
        </div>
    );
}

export default PraofPage;