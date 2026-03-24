from easysh.explain import explain


def test_simple_command():
    result = explain("ls")
    assert len(result) == 1
    assert "list" in result[0].lower() or "ls" in result[0].lower()


def test_compound_command():
    result = explain("git add -A && git commit -m \"fix bug\"")
    assert len(result) == 2


def test_unknown_command():
    result = explain("foobar --baz")
    assert result == []


def test_git_push():
    result = explain("git push")
    assert len(result) == 1
    assert "push" in result[0].lower() or "remote" in result[0].lower()


def test_rm_command():
    result = explain("rm file.txt")
    assert len(result) == 1
    assert "delet" in result[0].lower() or "remov" in result[0].lower()


def test_compound_dedup():
    # same command repeated should not produce duplicate explanations
    result = explain("git add -A && git add -A")
    assert len(result) == 1


def test_cd_command():
    result = explain("cd src")
    assert len(result) == 1
    assert "direct" in result[0].lower() or "cd" in result[0].lower() or "navig" in result[0].lower()
