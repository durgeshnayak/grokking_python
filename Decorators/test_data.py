TESTS = {
    "count_calls": "decorators_test.CountCallsTests",
    "jsonify": "decorators_test.JSONifyTests",
    "groot": "decorators_test.GrootTests",
    "four": "decorators_test.FourTests",
    "record_calls": "decorators_test.RecordCallsTests",
    "call": "functions_test.CallTests",
    "call_later": "functions_test.CallLaterTests",
    "exclude": "functions_test.ExcludeTests",
    "call_logger": "functions_test.CallLoggerTests",
    "call_again": "functions_test.CallAgainTests",
    "only_once": "functions_test.OnlyOnceTests",
    "is_ok": "initial_test.InitialTests",
    "coalesce_all": "more_test.CoalesceAllTests",
    "lazy_repr": "more_test.LazyReprTests",
    "positional_only": "more_test.PositionalOnlyTests",
    "at": "more_test.AtTests"
}

MODULES = {
    "decorators": [
        "count_calls",
        "jsonify",
        "groot",
        "four",
        "record_calls"
    ],
    "functions": [
        "call",
        "call_later",
        "exclude",
        "call_logger",
        "call_again",
        "only_once"
    ],
    "initial": [
        "is_ok"
    ],
    "more": [
        "coalesce_all",
        "lazy_repr",
        "positional_only",
        "at"
    ]
}
