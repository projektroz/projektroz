import React from 'react';

function LoginForm() {
  return (
    <form>
      <label>
        Nazwa użytkownika:
        <input type="text" />
      </label>
      <label>
        Hasło:
        <input type="password" />
      </label>
      <button type="submit">Zaloguj się</button>
    </form>
  );
}

export default LoginForm;
