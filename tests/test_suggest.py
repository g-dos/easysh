from easysh.suggest import suggest


def test_startswith_match():
    results = suggest("lis")
    assert any("list" in r for r in results)


def test_exact_word_match():
    results = suggest("push")
    assert any("push" in r for r in results)


def test_prefix_fallback():
    # "sta" should match "status", "stash", "start"
    results = suggest("sta")
    assert len(results) > 0


def test_contains_fallback():
    # "anch" contains part of "branch", "new branch"
    results = suggest("anch")
    assert len(results) > 0


def test_empty_input_returns_defaults():
    results = suggest("")
    assert len(results) == 3


def test_returns_at_most_three():
    results = suggest("l")
    assert len(results) <= 3


def test_unknown_returns_defaults():
    results = suggest("xyzzy")
    assert len(results) == 3
