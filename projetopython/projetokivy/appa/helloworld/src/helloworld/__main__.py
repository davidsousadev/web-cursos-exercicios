import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import yt_dlp
import os
import platform

class YouTubeDownloaderApp(toga.App):
    def startup(self):
        # Configurar janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Configurar layout
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Campo de entrada de URL
        self.url_input = toga.TextInput(placeholder='Enter YouTube URL', style=Pack(flex=1))

        # Botões de controle
        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        download_button = toga.Button('Download', on_press=self.download_audio, style=Pack(padding=5))
        play_button = toga.Button('Play', on_press=self.play_audio, style=Pack(padding=5))
        pause_button = toga.Button('Pause', on_press=self.pause_audio, style=Pack(padding=5))
        stop_button = toga.Button('Stop', on_press=self.stop_audio, style=Pack(padding=5))

        # Adicionar botões ao layout
        button_box.add(download_button)
        button_box.add(play_button)
        button_box.add(pause_button)
        button_box.add(stop_button)

        # Adicionar widgets ao layout principal
        main_box.add(self.url_input)
        main_box.add(button_box)

        self.main_window.content = main_box
        self.main_window.show()

        # Variável para armazenar o caminho do último arquivo baixado
        self.last_downloaded_file = None

    def get_download_path(self):
        if platform.system() == 'Android':
            return '/storage/emulated/0/Download'
        else:
            return os.path.join(os.path.expanduser('~'), 'Downloads')

    def download_audio(self, widget):
        url = self.url_input.value
        if not url:
            self.main_window.info_dialog("Error", "Please enter a valid URL.")
            return

        try:
            download_path = self.get_download_path()
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                id = info_dict['id']
                title = info_dict['title']
                self.last_downloaded_file = os.path.join(download_path, f"{id}.mp3")

                self.main_window.info_dialog("Success", f"Downloaded {title} as {id}.mp3")
        except Exception as e:
            self.main_window.info_dialog("Error", f"Error occurred during download: {e}")

    def play_audio(self, widget):
        if self.last_downloaded_file and os.path.exists(self.last_downloaded_file):
            import android
            android.play_audio(self.last_downloaded_file)  # Substitua com a função correta para tocar áudio no Android
            self.main_window.info_dialog("Playing", f"Playing {os.path.basename(self.last_downloaded_file)}")
        else:
            self.main_window.info_dialog("Error", "No downloaded file to play or file not found.")

    def pause_audio(self, widget):
        # Implementar pausa de áudio para Android
        pass

    def stop_audio(self, widget):
        # Implementar parada de áudio para Android
        pass

def main():
    return YouTubeDownloaderApp('YouTube Downloader', 'org.beeware.android')

if __name__ == '__main__':
    main().main_loop()
