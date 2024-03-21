import React, { useState } from "react";
import { Navigate } from "react-router-dom";

import useAuth from "../../hooks/useAuth";

function Logout() {
  const { logout } = useAuth();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string>("");
  const { isLoggedIn, loginUser } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await loginUser(username, password);
      setError("");
    } catch (error: any) {
      setError(error.message);
    }
  };

  handleSubmit;

  if (isLoggedIn) {
    logout();
  } else {
    return <Navigate to="/home" />;
  }

  // Ta funkcja renderuje pusty element, ponieważ hook useNavigate został już użyty
  return null;
}

export default Logout;
