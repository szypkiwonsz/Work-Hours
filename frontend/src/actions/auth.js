import axios from 'axios';
import {createMessage} from './messages';
import {
    ACTIVATION_FAIL,
    ACTIVATION_SUCCESS,
    AUTHENTICATED_FAIL,
    AUTHENTICATED_SUCCESS,
    GET_ERRORS,
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT,
    PASSWORD_RESET_CONFIRM_FAIL,
    PASSWORD_RESET_CONFIRM_SUCCESS,
    PASSWORD_RESET_FAIL,
    PASSWORD_RESET_SUCCESS,
    SIGNUP_FAIL,
    SIGNUP_SUCCESS,
    USER_LOADED_FAIL,
    USER_LOADED_SUCCESS
} from './types';

export const checkAuthenticated = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        };

        const body = JSON.stringify({token: localStorage.getItem('access')});

        try {
            const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/verify/`, body, config)
            if (res.data.code !== 'token_not_valid') {
                dispatch({
                    type: AUTHENTICATED_SUCCESS
                });
            } else {
                dispatch({
                    type: AUTHENTICATED_FAIL
                });
            }
        } catch (err) {
            dispatch({
                type: AUTHENTICATED_FAIL
            });
        }
    } else {
        dispatch({
            type: AUTHENTICATED_FAIL
        });
    }
};

export const load_user = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        };

        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/users/me/`, config)

            dispatch({
                type: USER_LOADED_SUCCESS,
                payload: res.data
            })
        } catch (err) {
            dispatch({
                type: USER_LOADED_FAIL
            })
        }
    } else {
        dispatch({
            type: USER_LOADED_FAIL
        });
    }
};

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({email, password});

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/create/`, body, config);

        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        });
        dispatch(createMessage({loginSuccess: 'Login Success'}))

        dispatch(load_user());
    } catch (err) {
        const errors = {
            msg: err.response.data,
            status: err.response.status
        }

        dispatch({
            type: LOGIN_FAIL
        })
        dispatch({
            type: GET_ERRORS,
            payload: errors
        })
    }
};

export const signup = (email, password, re_password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({email, password, re_password});

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/`, body, config);

        dispatch({
            type: SIGNUP_SUCCESS,
            payload: res.data
        });
        dispatch(createMessage({registerSuccess: 'Confirm Your Registration via Link Sent To Your Email'}));
    } catch (err) {
        const errors = {
            msg: err.response.data,
            status: err.response.status
        }
        dispatch({
            type: SIGNUP_FAIL
        })
        dispatch({
            type: GET_ERRORS,
            payload: errors
        })
    }
};

export const verify = (uid, token) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({uid, token});

    try {
        await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/activation/`, body, config);

        dispatch({
            type: ACTIVATION_SUCCESS,
        });
    } catch (err) {
        dispatch({
            type: ACTIVATION_FAIL
        })
    }
};

export const reset_password = (email) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({email});

    try {
        await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/reset_password/`, body, config);

        dispatch({
            type: PASSWORD_RESET_SUCCESS
        })
        dispatch(createMessage({
            passwordResetSuccess: 'If The Given Email Exists, You Will Receive a Link To ' +
                'Reset Your Password'
        }));
    } catch (err) {
        dispatch({
            type: PASSWORD_RESET_FAIL
        })
    }
};

export const reset_password_confirm = (uid, token, new_password, re_new_password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({uid, token, new_password, re_new_password});

    try {
        await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/reset_password_confirm/`, body, config);

        dispatch({
            type: PASSWORD_RESET_CONFIRM_SUCCESS
        })
        dispatch(createMessage({passwordResetConfirmSuccess: 'Password Reset Successfully'}));
    } catch (err) {
        const errors = {
            msg: err.response.data,
            status: err.response.status
        }
        dispatch({
            type: PASSWORD_RESET_CONFIRM_FAIL
        })
        dispatch({
            type: GET_ERRORS,
            payload: errors
        })
    }
};

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    });
    dispatch(createMessage({logoutSuccess: 'Logout Success'}))
};
