from fastapi import APIRouter
import os

router = APIRouter()

sessionsPastas = "sessions"

@router.get("/")
def listarContas():
    sessionsLista = []
    
    for i in os.listdir(sessionsPastas):
        
        if i .endswith('.session'):
            sessionsLista.append(
                i.replace('.session', '')
            )
    return {
        'accounts': sessionsLista
    }