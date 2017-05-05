#include <QtGui/QApplication>
#include <QtGui/QPixmap>
#include <QtGui/QPainter>
#include <QtGui/QPen>
#include <QtGui/QBrush>
#include <QtGui/QLabel>

int main(int argc, char *argv[])
{
    QApplication app (argc, argv);
    QPixmap pm (100, 100);
    pm.fill ();

    QPainter p (&pm);
    p.setRenderHint (QPainter::Antialiasing, true);

    QPen pen (Qt::blue, 2);
    p.setPen (pen);

    QBrush brush (Qt::green);
    p.setBrush (brush);

    p.drawLine (1,1,10,10);
    QLabel l;

    l.setPixmap (pm);
    l.show ();

    return app.exec ();
}
