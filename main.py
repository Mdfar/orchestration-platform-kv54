from fastapi import FastAPI, HTTPException from pydantic import BaseModel from typing import List, Optional from agents.orchestrator import AIOrchestrator

app = FastAPI(title="Staqlt AI Orchestration Platform") orchestrator = AIOrchestrator()

class TaskRequest(BaseModel): user_id: str prompt: str context: Optional[dict] = {}

@app.post("/v1/execute") async def execute_workflow(request: TaskRequest): try: result = await orchestrator.run_workflow(request.prompt, request.context) return {"status": "success", "data": result} except Exception as e: raise HTTPException(status_code=500, detail=str(e))

if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)