import './Login.css';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import authService from '../../services/authService.js';

function Login() {
    const navigate = useNavigate();
    let [email, setEmail] = useState('');
    let [password, setPassword] = useState('');


    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleFormSubmit = (event) => {
        event.preventDefault();

        authService.loginUser(({ email, password }))
            .then(user => {
                localStorage.setItem('user', JSON.stringify(user));
                navigate('/');
            })

        setEmail('');
        setPassword('');
    }


    return (
        <section className='login-page'>
            {/* <form className='login-form' onSubmit={handleFormSubmit}>
            <h2 className="login-page-title">
                Login
            </h2>
                <article className='input-group'>
                    <input id='login-email' type='text' value={email} onChange={handleEmailChange} placeholder="Email"/>
                </article>
                <article className='input-group'>
                    <input id='login-password' type='password' value={password} onChange={handlePasswordChange} placeholder="Password"/>
                </article>
                <input type='submit' value='Login' />
            </form> */}
           <form className="login-form" onSubmit={handleFormSubmit}>
                <h1>Log in</h1>
                            <input type="text" name="email" placeholder="E-mail" className='input-field' value={email} onChange={handleEmailChange} />
                            <input type="password" name="password" placeholder="Password" className='input-field' value={password} onChange={handlePasswordChange} />

                <p className="login-page-register">Haven't got an account? <a href="">Register</a></p>
                <p className="forgot_password">Forgot your password? <a href="">Reset Your Password</a></p>

                <input type="submit" name="login_submit" value="Log in"/>
            </form>
        </section>
    );
}

export default Login;