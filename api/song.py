import fastapi
from fastapi import Depends
from sqlmodel import Session, select

from db.db_setup import get_session
from db.models import Song, SongCreate

router = fastapi.APIRouter()

@router.get("/songs", response_model=list[Song])
async def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@router.post("/songs")
async def add_song(song: SongCreate, session: Session = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    session.commit()
    session.refresh(song)
    return song