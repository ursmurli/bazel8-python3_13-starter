load("@bazel_skylib//rules:build_test.bzl", "build_test")
load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:py_library.bzl", "py_library")
load("@rules_python//python:defs.bzl", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# # This stanza calls a rule that generates targets for managing pip dependencies
# # with pip-compile.
compile_pip_requirements(
    name = "requirements",
    src = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
    requirements_windows = "requirements_windows.txt",
)


py_binary(
    name = "cli",
    srcs = ["cli.py"],
    deps = [
        "@pypi//Typer:pkg",
        "@pypi//requests:pkg",
        "//:calculator",
    ],
)


py_binary(
    name = "hello",
    srcs = ["hello.py"],
)

py_library(
    name = "calculator",
    srcs = ["calculator.py"],
    visibility = ["//visibility:public"]
)

py_test(
    name = "calculator_test",
    srcs = ["calculator_test.py"],
    deps = [
        "//:calculator"
    ],
)