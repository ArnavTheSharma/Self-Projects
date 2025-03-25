async function getShortAnswer(query) {
  const appId = 'P4Q2RY-99L8PG5A7U'; 
  const url = `https://api.wolframalpha.com/v1/result?i=${encodeURIComponent(query)}&appid=${appId}`;

  try {
      const response = await fetch(url);
      if (response.ok) {
          const answer = await response.text();
          console.log('Wolfram Alpha Short Answer:', answer);
      } else {
          console.error('Error:', response.status, response.statusText);
      }
  } catch (error) {
      console.error('Error fetching result:', error);
  }
}

// Example usage:
getShortAnswer('what is 3+2');
