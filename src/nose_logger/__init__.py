import logging
import os

import psutil
from nose.plugins import Plugin

log = logging.getLogger("nose.plugins.nose_logger")


class NoseLoggerPlugin(Plugin):
    name = "NoseLoggerPlugin"
    data = {}
    logfile = "chrome-leak.log"

    def options(self, parser, env=os.environ):
        super(NoseLoggerPlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoseLoggerPlugin, self).configure(options, conf)
        self.enabled = True
        log.info("NoseLoggerPlugin enabled")
        if not self.enabled:
            return

    def running_chrome_processes(self):
        return len([p for p in psutil.process_iter() if p.name() == "chrome"])

    def beforeTest(self, test):
        chrome_processes = self.running_chrome_processes()
        self.chrome_pids_before = chrome_processes
        self.data[test.id()] = {"before": chrome_processes}
        # log.info("beforeTest: %s, %i", test.id(), chrome_processes)
        with open(self.logfile, "a") as f:
            f.write("beforeTest: %s, %i\n" % (test.id(), chrome_processes))

    def afterTest(self, test):
        chrome_processes = self.running_chrome_processes()
        self.data[test.id()]["after"] = chrome_processes
        # log.info("afterTest: %s, %i", test.id(), chrome_processes)
        with open(self.logfile, "a") as f:
            f.write("afterTest: %s, %i\n" % (test.id(), chrome_processes))
        # if chrome_processes != self.chrome_pids_before:
        #     log.critical(
        #         "Chrome processes changed during test: %s by %i",
        #         test.id(),
        #         chrome_processes - self.chrome_pids_before,
        #     )
