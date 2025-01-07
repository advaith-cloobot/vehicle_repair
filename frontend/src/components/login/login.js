import React , { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
// import template from "./login.jsx";

// class login extends React.Component {
//   render() {
//     return template.call(this);
//   }
// }



const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    check_login(email, password);
  };

  function check_login(user_email,user_password) {
    console.log(user_email)
    navigate("/layout/home");
  }




  return (
    <div className="login-container">
      <header className="login-header">
        <p>Login</p>
      </header>
      <div className="login-form">
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
      </div>
    </div>
  )
};

export default Login;
