const express = require('express');
const cors = require('cors');
const app = express();
const port = 8000;

app.use(cors());
app.use(express.json());
app.use(express.static('public')); // Serves index.html, styles.css, etc.

let games = []; // In-memory store for example

// API: Create a new game
app.post('/api/game', (req, res) => {
  const game = {
    id: games.length + 1,
    createdAt: new Date(),
  };
  games.push(game);
  res.json(game);
});

// Catch-all route for SPA
app.get('*', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
