import {useState} from "react";

import AppSideBar from "../../appSideBar/AppSideBar";
import MainForm from "../../mainForm/MainForm";
import MainResult from "../../mainResult/MainResult";


import './mainPage.css';

const MainPage = () => {
    const [curData, setCurData] = useState({
        "data": [
            13.2,
            11.9,
            11.9,
            13.4,
            13.4,
            13.3,
            11.9,
            12.1,
            12.6,
            13.9,
            10.7,
            12.3,
            10.6,
            10.4,
            10.6,
            11,
            11,
            10.8,
            10.8,
            10.6,
            10.9,
            11.9,
            11.6,
            11.9,
            11.3,
            11.9,
            11.4,
            11.3,
            11,
            10.8,
            10.9,
            10.9,
            11,
            11.2,
            11.8,
            11.8,
            12.7,
            12.9,
            12.4,
            14.2,
            14.8,
            14.8,
            15.4,
            14.6,
            14.1,
            13.3,
            12.6,
            11.1,
            11.2,
            11.6
        ],
        "k": 7,
        "data_sorted": [
            10.4,
            10.6,
            10.6,
            10.6,
            10.7,
            10.8,
            10.8,
            10.8,
            10.9,
            10.9,
            10.9,
            11,
            11,
            11,
            11,
            11.1,
            11.2,
            11.2,
            11.3,
            11.3,
            11.4,
            11.6,
            11.6,
            11.8,
            11.8,
            11.9,
            11.9,
            11.9,
            11.9,
            11.9,
            11.9,
            12.1,
            12.3,
            12.4,
            12.6,
            12.6,
            12.7,
            12.9,
            13.2,
            13.3,
            13.3,
            13.4,
            13.4,
            13.9,
            14.1,
            14.2,
            14.6,
            14.8,
            14.8,
            15.4
        ],
        "n": 50,
        "x_min": 10.4,
        "x_max": 15.4,
        "R": 5,
        "d": 0.71,
        "unsorted_data": "first_part_pics/unsorted_data.png",
        "sorted_data": "first_part_pics/sorted_data.png",
        "intervals": [
            [
                10.4,
                11.11
            ],
            [
                11.11,
                11.83
            ],
            [
                11.83,
                12.54
            ],
            [
                12.54,
                13.26
            ],
            [
                13.26,
                13.97
            ],
            [
                13.97,
                14.69
            ],
            [
                14.69,
                15.4
            ]
        ],
        "empirical_frequencies": [
            16,
            9,
            9,
            5,
            5,
            3,
            3
        ],
        "interval_frequencies": [
            0.32,
            0.18,
            0.18,
            0.1,
            0.1,
            0.06,
            0.06
        ],
        "middle_points": [
            10.76,
            11.47,
            12.19,
            12.9,
            13.61,
            14.33,
            15.04
        ],
        "accumulated_frequencies": [
            0.32,
            0.5,
            0.68,
            0.78,
            0.88,
            0.94,
            1
        ],
        "empirical_density": [
            0.45,
            0.25,
            0.25,
            0.14,
            0.14,
            0.08,
            0.08
        ],
        "border_points": [
            10.4,
            11.11,
            11.83,
            12.54,
            13.26,
            13.97,
            14.69,
            15.4
        ],
        "emp_distr_function": "first_part_pics/emp_distr_function.png",
        "emp_density_no_curve": "first_part_pics/emp_density_no_curve.png",
        "sample_mean": 12.11,
        "sample_variance": 1.76,
        "corrected_sample_variance": 1.8,
        "mean_square_deviation": 1.34,
        "sample_asymmetry": 0.7,
        "sample_excess": -0.67,
        "emp_density_normal": "first_part_pics/emp_density_normal.png",
        "emp_density_lin": "first_part_pics/emp_density_lin.png",
        "emp_density_exp": "first_part_pics/emp_density_exp.png",
        "theoretical_probabilities_normal": [
            0.13,
            0.19,
            0.21,
            0.18,
            0.11,
            0.06,
            0.02
        ],
        "theoretical_frequencies_normal": [
            6.37,
            9.39,
            10.49,
            8.88,
            5.7,
            2.77,
            1.02
        ],
        "theoretical_probabilities_exp": [
            0.02,
            0.02,
            0.02,
            0.02,
            0.02,
            0.02,
            0.02
        ],
        "theoretical_frequencies_exp": [
            1.21,
            1.14,
            1.08,
            1.02,
            0.96,
            0.9,
            0.85
        ],
        "theoretical_probabilities_lin": [
            0.14,
            0.14,
            0.14,
            0.14,
            0.14,
            0.14,
            0.14
        ],
        "theoretical_frequencies_lin": [
            7.14,
            7.14,
            7.14,
            7.14,
            7.14,
            7.14,
            7.14
        ],
        "min_frequency_value": 5,
        "united_frequencies": [
            16,
            9,
            9,
            5,
            11
        ],
        "united_theoretical_frequencies_normal": [
            6.37,
            9.39,
            10.49,
            8.88,
            9.49
        ],
        "united_theoretical_frequencies_exp": [
            1.21,
            1.14,
            1.08,
            1.02,
            2.71
        ],
        "united_theoretical_frequencies_lin": [
            7.14,
            7.14,
            7.14,
            7.14,
            21.43
        ],
        "chi_squared_normal": 16.74,
        "chi_squared_exp": 333.27,
        "chi_squared_lin": 17.67,
        "theoretical_distribution_function_normal": [
            0.1,
            0.23,
            0.42,
            0.63,
            0.8,
            0.92,
            0.97,
            0.99
        ],
        "kolmogorov_statistics_normal": 0.71,
        "theoretical_distribution_function_exp": [
            0.58,
            0.6,
            0.62,
            0.64,
            0.67,
            0.68,
            0.7,
            0.72
        ],
        "kolmogorov_statistics_exp": 4.07,
        "theoretical_distribution_function_lin": [
            0,
            0.14,
            0.29,
            0.43,
            0.57,
            0.71,
            0.86,
            1
        ],
        "kolmogorov_statistics_lin": 1.78
    })

    return (
        <div className="pageContent">
            <AppSideBar/>
            <div className="mainContent">
                <h1 className="pageTitle">Первичная обработка статистических данных</h1>
                <MainForm setCurData={setCurData}/>
                <MainResult dataObj={curData}/>
            </div>
        </div>
    );
}

export default MainPage;