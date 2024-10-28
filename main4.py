from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
from typing import Union, List, Dict, Any, Optional


app = FastAPI()


class SpaceProbe(BaseModel):
    identifier: str
    mission: Union[str, None] = None
    velocity: float
    fuel_level: Union[float, None] = None


@app.get("/space-probes/")
async def register_probe(probe: SpaceProbe):
    return probe
