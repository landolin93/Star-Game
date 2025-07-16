Star Direction Game
A two-player strategy game where Player 1 places stars on a 6x6 grid, and Player 2 selects directions to fill empty squares with circles. The game ends after 8 rounds, with Player 1 winning if any empty squares remain, and Player 2 winning if the board is fully filled.
Rules

Player 1: Places a star (⭐) on an empty square.
Player 2: Selects a direction (N, S, E, W, NE, NW, SE, SW), turning empty squares in that direction from each star into circles (⭕).
Each direction can be used only once.
After 8 rounds, Player 1 wins if ≥1 empty square remains; Player 2 wins if none remain.
Settings (rounds, win threshold) can be adjusted via the settings panel.

Project Structure

front-end/: Single index.html file with embedded React and Tailwind CSS (via CDN).
backend/: FastAPI server with game logic.

Setup
Front-End

Place index.html in the front-end/ directory.
Serve index.html using a simple HTTP server (e.g., Python's http.server):cd front-end
python -m http.server 3000



Backend

Navigate to the backend directory:cd backend


Install dependencies:pip install -r requirements.txt


Start the backend:uvicorn main:app --reload --port 8000



Dependencies

Front-End: None (React, Axios, and Tailwind CSS loaded via CDN in index.html).
Backend: FastAPI, uvicorn, pydantic, python-dotenv

Deployment

Front-End: Host index.html on a static file server (e.g., GitHub Pages, Vercel, Netlify). Update BACKEND_URL in index.html to the deployed backend URL.
Backend: Deploy to Heroku or Render, ensuring CORS allows requests from the front-end URL.
