load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "lib",
    srcs = glob(
        ["*.py"],
        exclude = ["*_test.py"],
    ),
    visibility = ["//visibility:public"],
    deps = [requirement("readabilipy")],
)

py_test(
    name = "readability_extractor_test",
    srcs = [
        "readability_extractor_test.py",
    ],
    deps = [
        ":lib",
        requirement("pytest"),
    ],
)
