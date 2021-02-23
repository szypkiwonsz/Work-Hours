import React from 'react';
import {Link} from 'react-router-dom';

const Home = (props) => (
    <div className="container">
        <div className="jumbotron mt-5">
            <h1 className="display-4">Count your working hours.</h1>
            <p className="lead">Thanks to our application, you can easily calculate your salary, save your working hours
                and print them in a nice form!
            </p>
            <hr className="my-4"/>
            <p>Click the button below to access your account.</p>
            <Link className="btn btn-primary btn-lg" to='/login' role="button">Login</Link>
        </div>
    </div>
);

export default Home;
