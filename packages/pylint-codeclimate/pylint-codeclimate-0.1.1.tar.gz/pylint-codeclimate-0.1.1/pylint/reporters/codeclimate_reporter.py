import hashlib
import linecache

from pylint.reporters.json_reporter import JSONReporter

# Code Climate specs
#   https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md
# GitLab specs:
#   https://docs.gitlab.com/ee/ci/testing/code_quality.html#implementing-a-custom-tool
#
# Output must be info, minor, major, critical, or blocker
SEVERITY_MAP = {
    "convention": "info",
    "refactor": "minor",
    "warning": "normal",
    "error": "critical",
    "fatal": "blocker",
}


def get_fingerprint(item):
    string = ""
    string += item["path"] + ","
    string += item["message-id"] + ","
    string += str(item["line"]) + ","
    string += str(item["column"] or "") + "\n"

    # FIXME: We should handle the exact string described by the positions
    string += linecache.getline(item["path"], item["line"])
    return hashlib.md5(string.encode("UTF-8")).hexdigest()


class CodeClimateReporter(JSONReporter):
    name = "codeclimate"
    extension = "codeclimate"

    @staticmethod
    def serialize(message):
        item = JSONReporter.serialize(message)
        output = {
            "fingerprint": get_fingerprint(item),
            "severity": SEVERITY_MAP[item["type"]],
            "description": item["message"],
            "location": {"path": item["path"]},
        }
        # Handle lines vs position
        if item["endLine"] is None:
            output["location"]["lines"] = {"begin": item["line"]}
        else:
            # FIXME: if begin to ends spans the whole line, might as well use "lines"
            # and not "position"
            output["location"]["position"] = {
                "begin": {
                    "line": item["line"],
                    "column": item["column"],
                },
                "end": {
                    "line": item["endLine"],
                    "column": item["endColumn"],
                },
            }
        return output


def register(linter):
    linter.register_reporter(CodeClimateReporter)
