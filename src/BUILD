cc_library (
    name = "libproject1",
    srcs = ["project1.cpp"],
    hdrs = ["project1.h"],
    visibility = ["//visibility:public"],
)

cc_binary (
    name = "project1",
    srcs = ["main.cpp"],
    deps = [
        ":libproject1",
    ],
)