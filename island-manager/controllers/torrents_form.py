from views.torrents_form.torrents_form import Ui_TorrentsForm
from controllers.create_torrent_form import CreateTorrentForm
from PyQt5.QtWidgets import QDialog, QHeaderView, QInputDialog, QLineEdit, QMenu, QAction, QMessageBox
from PyQt5.QtCore import Qt, QProcess
from models.TorrentsModel import TorrentsModel
from lib.util import sizeof_fmt, show_user_error_window, get_stack
import os

import logging

log = logging.getLogger(__name__)

class TorrentsForm:
    def __init__(self, parent, torrent_manager, config):
        self.window = QDialog(parent=parent)
        self.ui = Ui_TorrentsForm()
        self.ui.setupUi(self.window)
        self.config = config
        self.torrent_manager = torrent_manager
        self.torrents_model = TorrentsModel(self.window, self.torrent_manager)
        self.ui.torrents_table.setModel(self.torrents_model)
        self.apply_table_formatting()
        self.ui.torrents_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.torrents_table.customContextMenuRequested.connect(self.show_torrent_context_menu)
        self.ui.btn_add_torrent.clicked.connect(self.add_torrent)
        self.torrents_model.dataChanged.connect(self.update_rate)
        self.ui.btn_upload_limit.clicked.connect(self.set_global_upload_limit)
        self.ui.btn_download_limit.clicked.connect(self.set_global_download_limit)
        self.ui.btn_create_torrent.clicked.connect(self.show_create_torrent_dialog)

        self.load_display_limits()


    def show_torrent_context_menu(self, point):
        print(point)
        index = self.ui.torrents_table.indexAt(point)
        if index.isValid():
            menu = self.generate_torrents_menu(index)
            menu.popup(self.ui.torrents_table.mapToGlobal(point))

    def apply_table_formatting(self):
        self.ui.torrents_table.setColumnHidden(0, True)

        header = self.ui.torrents_table.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)


    def show_create_torrent_dialog(self):
        dialog = CreateTorrentForm(self.window, self.torrent_manager, self.config)
        dialog.exec()

    def generate_torrents_menu(self, index):
        infohash = str(self.ui.torrents_table.model().model_data[index.row()][0])
        name = str(self.ui.torrents_table.model().model_data[index.row()][1])
        print(infohash)
        menu = QMenu(self.window)
        pause = QAction("Pause", self.window)
        resume = QAction("Resume", self.window)
        delete = QAction("Delete", self.window)
        show_content = QAction("Show content", self.window)

        pause.triggered.connect(lambda: self.pause_torrent(infohash))
        resume.triggered.connect(lambda: self.resume_torrent(infohash))
        delete.triggered.connect(lambda: self.delete_torrent(infohash, name))
        show_content.triggered.connect(lambda: self.show_content(infohash))

        menu.addActions([pause, resume, show_content, delete])
        return menu

    def pause_torrent(self, infohash):
        self.torrent_manager.pause_torrent(infohash)
        self.torrents_model.updateModel()

    def resume_torrent(self, infohash):
        self.torrent_manager.resume_torrent(infohash)
        self.torrents_model.updateModel()

    def delete_torrent(self, infohash, name):
        dialog = QMessageBox(self.window)
        dialog.setIcon(QMessageBox.Warning)
        dialog.setText("Delete torrent")
        dialog.setInformativeText("The torrent %s and all its metadata will be deleted"\
                                  "\nWould you like to delete torrent data as well?" % name)
        dialog.addButton(QMessageBox.Cancel)
        dialog.addButton(QMessageBox.No)
        dialog.addButton(QMessageBox.Yes)
        dialog.setDefaultButton(QMessageBox.No)
        res = dialog.exec()
        if res == QMessageBox.Cancel or not (res == QMessageBox.Yes or res == QMessageBox.No):
            log.debug("Cancel torrent deletion")
            return
        try:
            log.debug("Deleting torrent: %s %s" %(infohash, name))
            self.torrent_manager.delete_torrent(infohash, (res == QMessageBox.Yes))
        except Exception as e:
            msg = "Error deleting torrent %s " % str(e)
            log.error(msg)
            log.exception(e)
            show_user_error_window(self.window, msg)

    def show_content(self, infohash):
        save_path = self.torrent_manager.get_save_path(infohash)
        log.debug("Save path is %s " % save_path)
        QProcess.startDetached(self.config["explorer"] + " %s" % os.path.abspath(save_path))

    def add_torrent(self):
        dialog = QInputDialog(self.window)
        res = QInputDialog.getText(dialog, "Add new torrent", "Paste magnet URI: ", QLineEdit.Normal)
        if res[0] and res[1]:
            self.torrent_manager.begin_torrent_download(magnet=res[0])
        self.torrents_model.updateModel()

    def update_rate(self):
        upload_rate = self.torrent_manager.get_global_upload_rate()
        download_rate = self.torrent_manager.get_global_download_rate()
        self.ui.lbl_download_speed.setText("%s/s" % sizeof_fmt(download_rate))
        self.ui.lbl_upload_speed.setText("%s/s" % sizeof_fmt(upload_rate))


    def set_global_upload_limit(self):
        res = QInputDialog.getInt(QInputDialog(self.window), "Set upload limit",
                                  "Enter new upload limit in bytes per second. Enter 0 to remove limit ", )
        if res[1]:
            self.torrent_manager.set_global_upload_limit(res[0])
            self.load_display_limits()

    def set_global_download_limit(self):
        res = QInputDialog.getInt(QInputDialog(self.window), "Set download limit",
                                  "Enter new download limit in bytes per second. Enter 0 to remove limit ", )
        if res[1]:
            self.torrent_manager.set_global_download_limit(res[0])
            self.load_display_limits()

    def load_display_limits(self):
        upload_limit = self.torrent_manager.get_global_upload_limit()
        download_limit = self.torrent_manager.get_global_download_limit()
        log.debug("Loading limits up %d down %d" % (upload_limit, download_limit))
        self.ui.btn_upload_limit.setText("Limit: %s" % (u"\u221E" if upload_limit == 0 else
                                         "%s/s" % sizeof_fmt(upload_limit)))
        self.ui.btn_download_limit.setText("Limit: %s" % (u"\u221E" if download_limit == 0 else
                                           "%s/s" % sizeof_fmt(download_limit)))

    def exec(self):
        self.window.exec()

