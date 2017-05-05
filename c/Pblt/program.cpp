#include "program.h"
#include <QDebug>

Pblt::Program::Program () :
    QObject ()
{
    QBluetoothLocalDevice localDevices;
    QList<QBluetoothAddress> remotes;
    if(localDevices.isValid())
    {
        remotes = localDevices.connectedDevices();
        qDebug() << localDevices.name();
        qDebug() << remotes.count();

    }
}

void Pblt::Program::Receiver()
{
    qDebug() << "si recibo\n";
}

