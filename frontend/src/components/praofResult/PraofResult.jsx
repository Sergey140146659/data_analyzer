import './praofResult.css'

const PraofResult = ({objImages}) => {
    console.log(objImages);
    return (
        <div className="praofResult">
            <img className="praof__resultImage" src={require(`../../${objImages.points_pic}`)} alt=""/>
            <img className="praof__resultImage" src={require(`../../${objImages.supsmooth_points_pic}`)} alt=""/>
            <img className="praof__resultImage" src={require(`../../${objImages.approximations_pic}`)} alt=""/>
            <img className="praof__resultImage" src={require(`../../${objImages.amplitudes}`)} alt=""/>
        </div>
    )
}

export default PraofResult;