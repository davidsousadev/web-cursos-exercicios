import React, { useState, useEffect } from 'react';
import './Api.css';

function Api() {
  const [searchTerm, setSearchTerm] = useState(''); // Termo de pesquisa
  const [results, setResults] = useState([]); // Resultados da pesquisa
  const [isLoading, setIsLoading] = useState(false); // Flag de carregamento

  useEffect(() => {
    const fetchResults = async () => {
      if (!searchTerm) return; // Não faz nada se o termo de pesquisa estiver vazio
      setIsLoading(true); // Ativa a flag de carregamento

      try {
        const response = await fetch(`https://itunes.apple.com/search?media=music&limit=30&term=${searchTerm}`);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        setResults(data.results); // Define os resultados da pesquisa
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setIsLoading(false); // Desativa a flag de carregamento
      }
    };

    fetchResults(); // Executa a função de busca ao montar o componente
  }, [searchTerm]); // Dispara novamente a busca sempre que o termo de pesquisa mudar

  const handleChange = (event) => {
    setSearchTerm(event.target.value); // Atualiza o termo de pesquisa conforme o usuário digita
  };

  return (
    <div>
      <h2>iTunes</h2>
      <input type="text" value={searchTerm} onChange={handleChange} placeholder="Search for music" />
      {isLoading && <p>Loading...</p>}
      {results.length > 0 ? (
        <ul>
          {results.map((result) => (
            <li key={result.trackId}>
              <strong>{result.trackName}</strong> by {result.artistName} <br />
              {result.previewUrl && <audio controls src={result.previewUrl}>Your browser does not support the audio element.</audio>}
            </li>
          ))}
        </ul>
      ) : (
        <p>No results found</p>
      )}
    </div>
  );
}

export default Api;


