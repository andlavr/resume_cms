import typing

from PySide6 import QtWidgets
from ui.blog import Ui_Form
from database import create_post_blog, get_posts_labels, del_post, load_post, update_post


class Blog(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.textBrowser_Main_text.setReadOnly(False)

        self.init_signals()

        self.load_posts()

    def init_signals(self) -> None:
        """
        Инициализация сигналов
        :return:
        """

        self.ui.pushButtonCreate.clicked.connect(self.create_post)
        self.ui.pushButtonDelete.clicked.connect(self.dell_post)
        self.ui.pushButton_Save.clicked.connect(self.update_post)

        self.ui.listWidget_Titles_name.itemClicked.connect(self.load_post)

    def create_post(self) -> None:

        """
        Создание поста

        :return: объект типа QtWidgets либо None
        """

        post_name, ok = QtWidgets.QInputDialog.getText(self, "Новый пост", "Введите название поста")
        if not ok and not post_name:
            return

        post_body, ok = QtWidgets.QInputDialog.getMultiLineText(self, "Новый пост", "Введите содержимое поста")
        if not ok and not post_body:
            return

        create_post_blog(post_name, post_body)

        self.load_posts()

    def dell_post(self) -> None:
        """
        Удаление поста

        :return: None
        """

        # self.ui.Titles_name.takeItem(self.ui.Titles_name.currentRow())

        if not self.ui.listWidget_Titles_name.selectedIndexes():
            return



        item_text = self.ui.listWidget_Titles_name.currentItem().text()
        post_id = item_text.split(": ")[0]
        # print(post_id)
        del_post(int(post_id))
        self.load_posts()

    def load_posts(self) -> None:
        """
        Добавление названия поста в ListWidget

        :return: None
        """
        self.ui.listWidget_Titles_name.clear()
        # posts_lables = QtWidgets.QListWidget.addItems(self, get_posts_labels)
        self.ui.listWidget_Titles_name.addItems(get_posts_labels())

    def load_post(self, item) -> None:
        """
        Добавление названия поста и самого поста в виджеты

        :param item: str
        :return: None
        """
        # print(item.text())
        post_id = item.text().split(": ")[0]
        post = load_post(int(post_id))
        # print(post)
        self.ui.lineEdit_Post_name.setText(post.title)
        self.ui.textBrowser_Main_text.setText(post.body)

    def update_post(self) -> None:
        """
        Обновляет данные в виджетах и передает их в метод update_post

        :return:None
        """

        item_text = self.ui.listWidget_Titles_name.currentItem().text()
        id_ = item_text.split(": ")[0]

        update_post(int(id_), self.ui.lineEdit_Post_name.text(), self.ui.textBrowser_Main_text.toPlainText())

        self.load_posts()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = Blog()
    win.show()

    app.exec()
