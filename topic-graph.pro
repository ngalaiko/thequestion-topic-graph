TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    bridges_articulations.cpp \
    cliques.cpp \
    cut.cpp \
    definitions.cpp \
    degree.cpp \
    dfsbfs.cpp \
    spanning.cpp

SUBDIRS += \
    topics-graph.pro

DISTFILES += \
    topic-graph.pro.user \
    topics-graph.pro.user \
    components.txt \
    degree.txt \
    diameter.txt \
    input.in

HEADERS += \
    bridges_articulations.h \
    cliques.h \
    cut.h \
    definitions.h \
    degree.h \
    dfsbfs.h \
    spanning.h
