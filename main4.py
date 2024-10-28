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


@app.post("/space-probes/")
async def register_probe(probe: SpaceProbe):
    probe_repr = probe.dict()
    if probe.fuel_level:
        fuel_level = f" with {probe.fuel_level} fuel level"
        probe_repr["fuel_level"] = fuel_level
    return probe_repr


@app.put("/space-probes/{probe_id}")
async def update_probe(probe_id: int, probe: SpaceProbe, q: Union[str, None] = None):
    response = {"probe_id": probe_id, **probe.dict()}
    if q:
        response.update({"additional": q})
    return response
