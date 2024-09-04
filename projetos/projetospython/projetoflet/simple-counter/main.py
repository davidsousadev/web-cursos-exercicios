import flet as ft
import yt_dlp
import os
import subprocess
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados
DATABASE_URL = 'sqlite:///audios.db'
Base = declarative_base()

class Audio(Base):
    __tablename__ = 'audios'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    url = Column(String(500))
    file_name = Column(String(500))

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.title = "YouTube Audio Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    url_field = ft.TextField(label="YouTube URL", width=400)
    status_text = ft.Text(value="", width=400)
    download_list = ft.Column()

    def refresh_download_list():
        download_list.controls.clear()
        audios = session.query(Audio).all()
        for audio in audios:
            item = ft.Row([
                ft.Text(audio.title, width=200),
                ft.IconButton(ft.icons.PLAY_ARROW, on_click=lambda e, audio=audio: play_audio(audio)),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e, audio=audio: delete_audio(audio)),
            ])
            download_list.controls.append(item)
        page.update()

    def download_audio(e):
        url = url_field.value
        if not url:
            status_text.value = "URL cannot be empty!"
            page.update()
            return
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(id)s.%(ext)s',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                id = info_dict['id']
                title = info_dict['title']
                audio = Audio(title=title, url=url, file_name=id)
                session.add(audio)
                session.commit()
                status_text.value = "Audio downloaded successfully!"
        except Exception as ex:
            status_text.value = f"Error: {ex}"
        
        refresh_download_list()
        page.update()

    def play_audio(audio):
        file_path = os.path.join('downloads', f"{audio.file_name}.m4a")
        if os.path.exists(file_path):
            subprocess.run(['xdg-open', file_path])

    def delete_audio(audio):
        session.delete(audio)
        session.commit()
        file_path = os.path.join('downloads', f"{audio.file_name}.m4a")
        if os.path.exists(file_path):
            os.remove(file_path)
        refresh_download_list()

    def clear_downloads(e):
        folder = 'downloads'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        refresh_download_list()

    def clear_table(e):
        session.query(Audio).delete()
        session.commit()
        refresh_download_list()

    refresh_download_list()

    page.add(
        ft.Column(
            [
                url_field,
                ft.Row(
                    [
                        ft.ElevatedButton("Download Audio", on_click=download_audio),
                        ft.ElevatedButton("Clear Downloads", on_click=clear_downloads),
                        ft.ElevatedButton("Clear Table", on_click=clear_table),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                status_text,
                download_list,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
