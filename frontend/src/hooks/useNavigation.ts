// useNavigation.ts
import { useNavigate } from 'react-router-dom';

const useNavigation = () => {
  const navigate = useNavigate();

  const redirectToDashboard = () => {
    navigate('/dashboard'); 
  };

  // Możesz dodać więcej funkcji nawigacji tutaj w przyszłości

  return {
    redirectToDashboard,
    // Dodaj inne funkcje nawigacji tutaj
  };
};

export default useNavigation;
