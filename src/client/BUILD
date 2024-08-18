load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "lib",
    srcs = glob(
        ["*.py"],
        exclude = ["*_test.py"],
    ),
    visibility = ["//visibility:public"],
    deps = [requirement("telegraph")],
)

py_test(
    name = "telegraph_client_test",
    srcs = [
        "telegraph_client_test.py",
    ],
    deps = [
        "//src/client:lib",
        requirement("pytest"),
    ],
)
