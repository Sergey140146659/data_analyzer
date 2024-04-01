import './praofResult.css'

const PraofResult = ({objImages}) => {
    console.log(objImages.points_pic, objImages.supsmooth_points_pic, objImages.approximations_pic, objImages.amplitudes);
    return (
        <div className="praofResult">
            <img className="praofResult__image" src={require(`../../${objImages.points_pic}`)} alt=""/>
            <img className="praofResult__image" src={require(`../../${objImages.supsmooth_points_pic}`)} alt=""/>
            <img className="praofResult__image" src={require(`../../${objImages.approximations_pic}`)} alt=""/>
            <img className="praofResult__image" src={require(`../../${objImages.amplitudes}`)} alt=""/>
        </div>
    )
}

export default PraofResult;