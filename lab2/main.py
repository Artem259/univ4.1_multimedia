import os
import sys

from PySide6 import QtGui
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from MainWindow import Ui_MainWindow


def hhmmss(ms):
    s = round(ms / 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%02d:%02d" % (m, s))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer(self)

        self.player.mediaStatusChanged.connect(self.player_media_status_handler)
        self.player.playbackStateChanged.connect(self.player_playback_state_handler)
        self.player.positionChanged.connect(self.player_position_handler)
        self.player.durationChanged.connect(self.player_duration_handler)
        self.player.errorOccurred.connect(self.player_error_occurred_handler)

        self.video_widget = QVideoWidget()
        self.audio_widget = QAudioOutput()
        self.player.setVideoOutput(self.video_widget)
        self.player.setAudioOutput(self.audio_widget)
        self.verticalLayout.insertWidget(0, self.video_widget)

        self.actionOpen.triggered.connect(self.open_file_handler)
        self.playButton.clicked.connect(self.play_button_handler)
        self.volumeButton.clicked.connect(self.volume_button_handler)
        self.volumeSlider.sliderMoved.connect(self.volume_slider_handler)
        self.playerSlider.sliderMoved.connect(self.player_slider_moved_handler)
        self.playerSlider.sliderPressed.connect(self.player_slider_pressed_handler)
        self.playerSlider.sliderReleased.connect(self.player_slider_released_handler)
        self.backButton.pressed.connect(self.back_button_handler)
        self.forwardButton.pressed.connect(self.forward_button_handler)

        self.current_volume = 100
        self.audio_widget.setVolume(self.current_volume)
        self.player_last_state = None

        self.show()

    def player_media_status_handler(self, status):
        if status == QMediaPlayer.LoadedMedia:
            self.player.play()
            self.player.pause()
            self.player.setPosition(0)

    def player_playback_state_handler(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playButton.setIcon(QtGui.QIcon("resources/pause.png"))
        else:
            self.playButton.setIcon(QtGui.QIcon("resources/play.png"))

    def player_position_handler(self, position):
        self.positionLabel.setText(hhmmss(position))
        if not self.playerSlider.isSliderDown():
            self.playerSlider.setValue(position)

    def player_duration_handler(self, duration):
        self.playerSlider.setRange(0, duration)
        self.durationLabel.setText(hhmmss(duration))

    def player_error_occurred_handler(self, error, error_string):
        self.statusBar.showMessage(f"Error [{error}] " + error_string, 5000)

    def open_file_handler(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "All files (*.*);;mp3 Audio (*.mp3);;"
                                              "mp4 Video (*.mp4);;avi Video (*.avi)")

        if path:
            self.player.setSource(QUrl.fromLocalFile(path))

    def play_button_handler(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def volume_button_handler(self):
        pass  # todo

    def volume_slider_handler(self, value):  # todo
        if self.volumeSlider.hasTracking():
            print(11)
        else:
            print(0)

    def player_slider_moved_handler(self, value):
        self.player.setPosition(value)

    def player_slider_pressed_handler(self):
        self.player_last_state = self.player.playbackState()
        self.player.pause()

    def player_slider_released_handler(self):
        if self.player_last_state == QMediaPlayer.PlayingState:
            self.player.play()

    def back_button_handler(self):
        self.player.setPosition(max(0, self.player.position() - 5000))

    def forward_button_handler(self):
        self.player.setPosition(min(self.player.duration() - 1, self.player.position() + 5000))


if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
