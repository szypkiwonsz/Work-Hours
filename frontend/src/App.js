import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from './containers/Home';
import Login from './containers/Login';
import Signup from './containers/Signup';
import Activate from './containers/Activate';
import ResetPassword from './containers/ResetPassword';
import ResetPasswordConfirm from './containers/ResetPasswordConfirm';
import {Provider as AlertProvider} from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';
import {Provider} from 'react-redux';
import store from './store';

import Layout from './hocs/Layout';
import Alerts from './components/Alerts';

// alert options
const alertOptions = {
    timeout: 5000,
    position: 'bottom center'
}

const App = () => (
    <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
            <Router>
                <Layout>
                    <Alerts/>
                    <Switch>
                        <Route exact path='/' component={Home}/>
                        <Route exact path='/login' component={Login}/>
                        <Route exact path='/signup' component={Signup}/>
                        <Route exact path='/reset-password' component={ResetPassword}/>
                        <Route exact path='/password/reset/confirm/:uid/:token' component={ResetPasswordConfirm}/>
                        <Route exact path='/activate/:uid/:token' component={Activate}/>
                    </Switch>
                </Layout>
            </Router>
        </AlertProvider>
    </Provider>
);

export default App;