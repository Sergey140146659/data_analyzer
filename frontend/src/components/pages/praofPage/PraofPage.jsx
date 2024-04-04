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
            amplitudes_with_curves: "praof_pics/thumbnail5.png",
            interpolation_pic: "praof_pics/thumbnail3.png",
            points_pic: "praof_pics/thumbnail1.png",
            supsmooth_points_pic: "praof_pics/thumbnail2.png",
            coefs_greater: [0.67, -21.5, 1.04, -0.13],
            coefs_less: [-0.95, -0.11, -0.17, -21.09]
        })

    useEffect(() => {
        smoothScroll();
    }, []);


    return (
        <div className="pageContent">
            <AppSideBar place="praof" />
            <div className="praofContent">
                <h1 className="pageTitle">Последовательности ранжированных амплитуд относительно флуктуаций</h1>
                <PraofForm setCurData={setCurData} setLoading={setLoading} />
                {loading ? <span className="loader"></span> : <PraofResult obj={curData}/>}
            </div>
        </div>
    );
}

export default PraofPage;