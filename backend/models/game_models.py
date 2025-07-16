from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class GameSettings(BaseModel):
    numberOfRounds: int = 8
    emptySquaresToWin: int = 1
    maxDirections: int = 8

class GameHistoryEntry(BaseModel):
    board: List[List[str]]
    currentPlayer: int
    gamePhase: str
    round: int
    availableDirections: List[str]
    winner: Optional[int]
    starsPlaced: int
    settings: GameSettings
    action: str
    timestamp: float

class GameState(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    board: List[List[str]] = Field(default_factory=lambda: [['empty'] * 6 for _ in range(6)])
    currentPlayer: int = 1
    gamePhase: str = 'placement'
    round: int = 1
    availableDirections: List[str] = Field(default_factory=lambda: ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW'])
    winner: Optional[int] = None
    starsPlaced: int = 0
    gameHistory: List[GameHistoryEntry] = Field(default_factory=list)
    settings: GameSettings = Field(default_factory=GameSettings)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class CreateGameRequest(BaseModel):
    settings: Optional[GameSettings] = None

class PlaceStarRequest(BaseModel):
    row: int
    col: int

class SelectDirectionRequest(BaseModel):
    direction: str

class GameResponse(BaseModel):
    success: bool
    message: str
    game: Optional[GameState] = None
    error: Optional[str] = None
