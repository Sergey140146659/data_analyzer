import {useEffect, useState} from "react";

import AppSideBar from "../../appSideBar/AppSideBar";
import PraofForm from "../../praofForm/PraofForm";
import PraofResult from "../../praofResult/PraofResult";

import './praofPage.css';
import {smoothScroll} from "../../../services/utilities";


const PraofPage = () => {
    const [loading, setLoading] = useState(false);
    const [curData, setCurData] = useState(
        {
            amplitudes: "praof_pics/thumbnail4.png",
            approximations_pic: "praof_pics/thumbnail3.png",
            points_pic: "praof_pics/thumbnail1.png",
            supsmooth_points_pic: "praof_pics/thumbnail2.png"
        })

    useEffect(() => {
        smoothScroll();
    }, []);


    return (
        <div className="pageContent">
            <AppSideBar place="praof" />
            <div className="praofContent">
                <h1 className="pageTitle">Последовательность ранжирования амплитуд относительно флуктуации</h1>
                <PraofForm setCurData={setCurData} setLoading={setLoading} />
                {loading ? <span className="loader"></span> : <PraofResult objImages={curData}/>}
            </div>
        </div>
    );
}

export default PraofPage;