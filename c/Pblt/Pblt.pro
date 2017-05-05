QT += core
QT += bluetooth
QT -= gui

CONFIG += c++11

TARGET = Pblt
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    program.cpp

HEADERS += \
    program.h
