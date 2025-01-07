import React , { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import httpClient from "../../httpClient";
import './login.css';


const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSignUp, setIsSignUp] = useState(false);
  const [userName, setUserName] = useState("");
  const [signUpEmail, setSignUpEmail] = useState("");
  const [signUpPassword, setSignUpPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    check_login(email, password);
  };

  function check_login() {
    // navigate("/layout/home");
    const data = {
      user_email: email,
      user_password: password
    }
    httpClient.post('/check_login', data)
      .then((response) => {
        console.log(response.data)
        console.log('response login : ', response);
        const data = response.data;
        console.log("\n\ndata login :: ",data);
        if (data.status) {
          sessionStorage.setItem('token', data.data);
          sessionStorage.setItem('user_id', data.user_id);
          sessionStorage.setItem('user_name', data.user_name);
          navigate("/layout/home");
        }
        else{
          alert("Invalid Email or Password");
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const handleSignUp = () => {
    // Sign up logic here
    const data = {
      user_name: userName,
      user_email: signUpEmail,
      user_password: signUpPassword
    }
    httpClient.post('/sign_up_user', data)
      .then((response) => {
        console.log(response.data)
        console.log('response login : ', response);
        const data = response.data;
        console.log("\n\ndata login :: ",data);
        if (data.status) {
          alert("Account Created Successfully");
          setIsSignUp(false);
        }
        else{
          alert("Invalid Email or Password");
        }
      })
      .catch((error) => {
        console.log(error)
      })
  };




  return (
    <div className="login-container">
      <h1 className="title">Car Repair Estimator Tool</h1>
      <span role="img" aria-label="car" className="car-icon">🚗</span>
      <div className="login-frame">
        {!isSignUp ? (
          <div className="login-form">
            <header className="login-header">
              <p>Login</p>
            </header>
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
            <button onClick={() => setIsSignUp(true)}>Sign Up</button>
          </div>
        ) : (
          <div className="sign-up-form">
            <header className="login-header">
              <p>Sign Up</p>
            </header>
            <input
              type="text"
              placeholder="User Name"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
            />
            <input
              type="email"
              placeholder="Email"
              value={signUpEmail}
              onChange={(e) => setSignUpEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              value={signUpPassword}
              onChange={(e) => setSignUpPassword(e.target.value)}
            />
            <button onClick={handleSignUp}>Create Account</button>
            <button onClick={() => setIsSignUp(false)}>Back to Login</button>
          </div>
        )}
      </div>
    </div>
  )
};

export default Login;
