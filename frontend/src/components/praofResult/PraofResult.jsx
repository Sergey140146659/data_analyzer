import './praofResult.css'

const PraofResult = ({objImages}) => {
    console.log(objImages.points_pic, objImages.supsmooth_points_pic, objImages.approximations_pic, objImages.amplitudes);
    return (
        <div className="praofResult">
            <img className="praofResult__image" id="section1" src={require(`../../${objImages.points_pic}`)} alt=""/>
            <img className="praofResult__image" id="section2" src={require(`../../${objImages.supsmooth_points_pic}`)} alt=""/>
            <img className="praofResult__image" id="section3" src={require(`../../${objImages.approximations_pic}`)} alt=""/>
            <img className="praofResult__image" id="section4" src={require(`../../${objImages.amplitudes}`)} alt=""/>
        </div>
    )
}

export default PraofResult;