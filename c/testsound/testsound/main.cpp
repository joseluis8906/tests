#include <QCoreApplication>
#include <QAudioRecorder>
#include <QUrl>
#include <QTimer>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);


    QAudioEncoderSettings audioSettings;
    audioSettings.setCodec("audio/PCM");
    audioSettings.setSampleRate(32000);
    audioSettings.setBitRate(16);
    audioSettings.setChannelCount(1);
    audioSettings.setQuality(QMultimedia::NormalQuality);
    audioSettings.setEncodingMode(QMultimedia::ConstantQualityEncoding);

    QAudioRecorder *audioRecorder = new QAudioRecorder(&a);
    audioRecorder->setEncodingSettings(audioSettings);
    audioRecorder->setContainerFormat("wav");
    audioRecorder->setOutputLocation(QUrl::fromLocalFile("test.wav"));
    audioRecorder->setAudioInput("default");

    QTextStream qtin(stdin);
    QString opt;

    while (true)
    {
        qInfo("r). To recordq\ns).To stop\nq). To quit\n");
        opt = qtin.readLine();

        if (opt == "r")
        {
            qInfo ("Recording.\n");
            audioRecorder->record();
        }
        else if (opt == "s")
        {
            qInfo ("Stop.\n");
            audioRecorder->stop();
        }
        else if (opt == "q")
        {
            qInfo ("Quit.\n");
            audioRecorder->stop();
            QTimer::singleShot(0, &a, SLOT(quit()));
            break;
        }
    }

    delete audioRecorder;
    audioRecorder = NULL;
    return a.exec();
}
