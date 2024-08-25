load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "lib",
    srcs = glob(
        ["*.py"],
        exclude = ["*_test.py"],
    ),
    visibility = ["//visibility:public"],
    deps = ["//src/extractor:lib"],
)

py_test(
    name = "markdown_composer_test",
    srcs = [
        "markdown_composer_test.py",
    ],
    deps = [
        ":lib",
        requirement("pytest"),
    ],
)
