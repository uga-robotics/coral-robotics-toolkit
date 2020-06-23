#!/usr/bin/python3

import datetime


class DebugMessages:
    def __init__(self, class_object=None):
        if class_object is not None:
            self.className = class_object.__class__.__name__
            self.classID = id(class_object)

        else:
            self.className = "None"
            self.classID = 0

        # Initializing the debug strings for easier printing
        self.infoStr = "[INFO]\t[" + self.className + "\tID=" + str(self.classID) + "]"
        self.debugStr = "[DEBUG]\t[" + self.className + "\tID=" + str(self.classID) + "]"
        self.warningStr = "[WARN]\t[" + self.className + "\tID=" + str(self.classID) + "]"
        self.errorStr = "[ERROR]\t[" + self.className + "\tID=" + str(self.classID) + "]"
        self.fatalStr = "[FATAL]\t[" + self.className + "\tID=" + str(self.classID) + "]"

    def info(self, message):
        current_dt = datetime.datetime.now()

        print(self.infoStr + "[" + "{0:d}{1:d}{2:d}-{3:d}{4:2d}{5:d}".format(current_dt.year, current_dt.month,
                                                                             current_dt.day, current_dt.hour,
                                                                             current_dt.minute,
                                                                             current_dt.second) + "]: " + message)

    def debug(self, message):
        current_dt = datetime.datetime.now()

        print(self.debugStr + "[" + "{0:d}{1:d}{2:d}-{3:d}{4:2d}{5:d}".format(current_dt.year, current_dt.month,
                                                                              current_dt.day, current_dt.hour,
                                                                              current_dt.minute,
                                                                              current_dt.second) + "]: " + message)

    def warning(self, message):
        current_dt = datetime.datetime.now()

        print(self.warningStr + "[" + "{0:d}{1:d}{2:d}-{3:d}{4:2d}{5:d}".format(current_dt.year, current_dt.month,
                                                                                current_dt.day, current_dt.hour,
                                                                                current_dt.minute,
                                                                                current_dt.second) + "]: " + message)

    def error(self, message):
        current_dt = datetime.datetime.now()

        print(self.errorStr + "[" + "{0:d}{1:d}{2:d}-{3:d}{4:2d}{5:d}".format(current_dt.year, current_dt.month,
                                                                              current_dt.day, current_dt.hour,
                                                                              current_dt.minute,
                                                                              current_dt.second) + "]: " + message)

    def fatal(self, message):
        current_dt = datetime.datetime.now()

        print(self.fatalStr + "[" + "{0:d}{1:d}{2:d}-{3:d}{4:2d}{5:d}".format(current_dt.year, current_dt.month,
                                                                              current_dt.day, current_dt.hour,
                                                                              current_dt.minute,
                                                                              current_dt.second) + "]: " + message)
