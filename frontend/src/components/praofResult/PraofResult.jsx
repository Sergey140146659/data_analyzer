import './praofResult.css'

const PraofResult = ({objImages}) => {
    console.log(objImages);
    return (
        <div className="praofResult">
            <img src={`${objImages.amplitudes}`} alt="" />
        </div>
    )
}

export default PraofResult;