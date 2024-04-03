from pro_filer.actions.main_actions import show_preview


def test_show_preview_with_data(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 3 files and 2 directories" in captured.out
    assert (
        "First 5 files: ['src/__init__.py', "
        "'src/app.py', "
        "'src/utils/__init__.py']"
        in captured.out
    )
    assert "First 5 directories: ['src', 'src/utils']" in captured.out


def test_show_preview_no_data(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 0 files and 0 directories" in captured.out
