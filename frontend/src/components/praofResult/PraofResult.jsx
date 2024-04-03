import './praofResult.css'

const PraofResult = ({obj}) => {
    console.log(obj);
    return (
        <div className="praofResult">
            <img className="praofResult__image" id="section1" src={require(`../../${obj.points_pic}`)} alt=""/>
            <img className="praofResult__image" id="section2" src={require(`../../${obj.supsmooth_points_pic}`)}
                 alt=""/>
            <img className="praofResult__image" id="section3" src={require(`../../${obj.interpolation_pic}`)}
                 alt=""/>
            <img className="praofResult__image" id="section4" src={require(`../../${obj.amplitudes}`)} alt=""/>
            <div>
                <img className="praofResult__image" id="section4" src={require(`../../${obj.amplitudes_with_curves}`)}
                     alt=""/>
                <div className="praofResult__item">
                    <p>Формула огибающей кривой: y = c<sub>1</sub>*e<sup>(a<sub>1</sub>*x)</sup> + c<sub>2</sub>*e<sup>(a<sub>2</sub>*x)</sup>
                    </p>
                </div>
                <div className="praofResult__item">
                    <p>Коэффициенты положительной кривой:</p>
                    <p className="data">
                        <span>c<sub>1</sub> = {obj.coefs_greater[0]}</span>
                        <span>a<sub>1</sub> = {obj.coefs_greater[1]}</span>
                        <span>c<sub>2</sub> = {obj.coefs_greater[2]}</span>
                        <span>a<sub>2</sub> = {obj.coefs_greater[3]}</span>
                    </p>
                </div>
                <div className="praofResult__item">
                    <p>Коэффициенты отрицательной кривой:</p>
                    <p className="data">
                        <span>c<sub>1</sub> = {obj.coefs_less[0]}</span>
                        <span>a<sub>1</sub> = {obj.coefs_less[1]}</span>
                        <span>c<sub>2</sub> = {obj.coefs_less[2]}</span>
                        <span>a<sub>2</sub> = {obj.coefs_less[3]}</span>
                    </p>
                </div>
            </div>
        </div>
    )
}

export default PraofResult;