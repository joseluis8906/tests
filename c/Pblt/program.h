#ifndef PROGRAM_H
#define PROGRAM_H

#include <QObject>
#include <QBluetoothLocalDevice>
#include <QString>

namespace Pblt {

class Program : public QObject
{
    Q_OBJECT

private:

public:
    Program ();
    QBluetoothLocalDevice LocalDevices ();

public slots:
    void Receiver ();
};
}

#endif // PROGRAM_H
