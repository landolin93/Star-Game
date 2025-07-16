from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from game_service import GameService
from models.game_models import GameState, GameSettings, GameResponse, CreateGameRequest, PlaceStarRequest, SelectDirectionRequest
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

games = {}

@app.post("/api/game", response_model=GameResponse)
async def create_game(request: CreateGameRequest):
    game = GameService.create_new_game(request.settings)
    game_id = game.id
    games[game_id] = game
    return {"success": True, "message": "Game created successfully", "game": {**game.dict(), "id": game_id}}

@app.get("/api/game/{game_id}", response_model=GameResponse)
async def get_game(game_id: str):
    if game_id not in games:
        return {"success": False, "message": "Game not found", "error": "Game not found"}
    return {"success": True, "message": "Game retrieved successfully", "game": {**games[game_id].dict(), "id": game_id}}

@app.post("/api/game/{game_id}/place-star", response_model=GameResponse)
async def place_star(game_id: str, request: PlaceStarRequest):
    if game_id not in games:
        return {"success": False, "message": "Game not found", "error": "Game not found"}
    success, detail = GameService.place_star(games[game_id], request.row, request.col)
    return {"success": success, "message": detail, "game": {**games[game_id].dict(), "id": game_id}}

@app.post("/api/game/{game_id}/select-direction", response_model=GameResponse)
async def select_direction(game_id: str, request: SelectDirectionRequest):
    if game_id not in games:
        return {"success": False, "message": "Game not found", "error": "Game not found"}
    success, detail = GameService.apply_direction(games[game_id], request.direction)
    return {"success": success, "message": detail, "game": {**games[game_id].dict(), "id": game_id}}

@app.post("/api/game/{game_id}/undo", response_model=GameResponse)
async def undo_move(game_id: str):
    if game_id not in games:
        return {"success": False, "message": "Game not found", "error": "Game not found"}
    success, detail = GameService.undo_move(games[game_id])
    return {"success": success, "message": detail, "game": {**games[game_id].dict(), "id": game_id}}
