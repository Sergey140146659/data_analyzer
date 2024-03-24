import './praofResult.css'

const PraofResult = ({objImages}) => {
    console.log(objImages);
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