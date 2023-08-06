from text_manipulations import shave_marks


def test_shave_marks_do_shave_marks():
    assert shave_marks("curaçao") == "curacao"


def test_shave_marks_leave_words_intact():
    assert shave_marks("curacao") == "curacao"
