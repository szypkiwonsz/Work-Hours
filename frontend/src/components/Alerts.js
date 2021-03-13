import React, {Component, Fragment} from 'react';
import {withAlert} from 'react-alert';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';

// class that displays alerts (messages and errors) gets after making a request from the server
export class Alerts extends Component {
    static propTypes = {
        error: PropTypes.object.isRequired,
        message: PropTypes.object.isRequired
    }

    componentDidUpdate(prevProps) {
        const {error, alert, message} = this.props;
        // alerts from backend
        if (error !== prevProps.error) {
            if (error.status !== 200) {
                if (error.msg.email) alert.error(`${error.msg.email}`.split('.').join(''));
                if (error.msg.token) alert.error(`${error.msg.token}`.split('.').join(''));
                else alert.error(error.msg.detail);
            }
        }
        if (message !== prevProps.message) {
            if (message.loginSuccess) alert.success(message.loginSuccess);
            if (message.logoutSuccess) alert.success(message.logoutSuccess);
            if (message.registerSuccess) alert.success(message.registerSuccess);
            if (message.passwordResetSuccess) alert.success(message.passwordResetSuccess);
            if (message.passwordResetConfirmSuccess) alert.success(message.passwordResetConfirmSuccess);
        }
    }

    render() {
        return (
            <Fragment/>
        );
    }
}

const mapStateToProps = state => ({
    error: state.errors,
    message: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));
