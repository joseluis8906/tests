#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowFlags(Qt::Window | Qt::FramelessWindowHint);
    w.setParent(0);
    w.setAttribute(Qt::WA_NoSystemBackground, true);
    w.setAttribute(Qt::WA_TranslucentBackground, true);
    w.show();

    return a.exec();
}
