import {useState} from "react";

import AppSideBar from "../../appSideBar/AppSideBar";
import PraofForm from "../../praofForm/PraofForm";
import PraofResult from "../../praofResult/PraofResult";

import './praofPage.css';


const PraofPage = () => {
    const [loading, setLoading] = useState(false);
    const [curData, setCurData] = useState(
        {
            amplitudes: "praof_pics/85Fn0HsoIuM.jpg",
            approximations_pic: "praof_pics/EQug5D207ck.jpg",
            points_pic: "praof_pics/hESTmzVfIHQ.jpg",
            supsmooth_points_pic: "praof_pics/YhsdQuC2ymA.jpg"
        })

    return (
        <div className="pageContent">
            <AppSideBar/>
            <div className="praofContent">
                <h1 className="pageTitle">Последовательность ранжирования амплитуд относительно флуктуации</h1>
                <PraofForm setCurData={setCurData} setLoading={setLoading} />
                {loading ? <span className="loader"></span> : <PraofResult objImages={curData}/>}
            </div>
        </div>
    );
}

export default PraofPage;