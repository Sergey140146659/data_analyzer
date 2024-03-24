import AppSideBar from "../../appSideBar/AppSideBar";
import Form from "../../form/Form";

import './praofPage.css';


const PraofPage = () => {
    return (
        <div className="pageContent">
            <AppSideBar/>
            <Form labelName="Входные данные" />
        </div>
    );
}

export default PraofPage;